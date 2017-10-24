from PIL import Image

from musicbot import constants


def edit():
    img_size = (100, 100)

    img = Image.open(constants.EDIT_IMAGE)
    img = img.convert('RGBA').rotate(45, expand=1)
    img.thumbnail(img_size)
    img_w, img_h = img_size
    background = Image.open(constants.SLAM_IMAGE_PATH + 'slam.png', 'r')
    bg_w, bg_h = background.size
    offset = ((int((bg_w - img_w) / 2) - 100), int((bg_w - img_w) / 2) - 20)
    background.paste(img, offset, img)
    background.save(constants.SLAM_IMAGE_PATH + 'out.png')