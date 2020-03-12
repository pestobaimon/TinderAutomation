from skimage.io import imread, imsave, imshow, show
import matplotlib.pyplot as plt
import pynder
from helpers import get_access_token, get_login_credentials
from io_helper import save_image
from image_viewer import ImageViewer

email, password, FBID = get_login_credentials()
session = pynder.Session(XAuthToken='d4d5bfc1-63e8-4a2b-bcd1-d456bf147781')

while True:
    users = session.nearby_users()
    for user in users:
        photos = user.get_photos()
        print("Fetched user photos..")

        imgviewer = ImageViewer(photos)
        imgviewer.display_images()

        # for photo in photos:
        #     print(photo)
        #     image = imread(photo)
        #     print('here')
        #     imshow(image)
        #     print('here2')
        #     show()
        #     print('here3')

        #     input_string = "Press J to like. Press K to dislike."

        #     save_image(image, photo, imgviewer.wait())