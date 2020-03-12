import numpy as np
import urllib.request
import cv2
import sys,tty
from io_helper import save_image

class ImageViewer():
	def __init__(self,urlin):
		self.urls = urlin

	# METHOD #1: OpenCV, NumPy, and urllib
	def url_to_image(self,url):
		# download the image, convert it to a NumPy array, and then read
		# it into OpenCV format
		resp = urllib.request.urlopen(url)
		image = np.asarray(bytearray(resp.read()), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
		# return the image
		return image

	# loop over the image URLs
	def display_images(self):
		for url in self.urls:
			# download the image URL and display it
			image = self.url_to_image(url)
			print(url)
			cv2.imshow("Image", image)
			input_string = "Press K to like. Press J to dislike. Press X to exit"
			print(input_string)
			key = cv2.waitKey(0)
			if key == 107: # k
				print('photo liked')
				liked = True
			elif key == 106: # J
				print('photo disliked')
				liked = False
			elif key == 120:
				exit(0)
			save_image(image, url, liked)

	def wait(self):
		key=0
		while(key != 106 or key != 107):
			tty.setcbreak(sys.stdin)
			key = ord(sys.stdin.read(1))
			if key == 106:
				print('photo liked')
				return True
			elif key == 107:
				print('photo disliked')
				return False
