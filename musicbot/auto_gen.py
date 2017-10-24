import os
import random
from musicbot import constants

random_tracker = dict()

def is_randomable(request_tag):
    """
    Check if requested tag is in random list
    :param request_tag: 
    :return: boolean
    """

    return os.path.isdir(constants.IMAGE_PATH + request_tag)

def folder(request_folder):
    """
    Select random image from given folder
    :return: image name
    """
    shuffle_list = []

    for source_tag in os.listdir(constants.IMAGE_PATH + request_folder):
        source_tag = source_tag.split(".png")[0]
        shuffle_list.append(source_tag)

    random.shuffle(shuffle_list)

    # Test Prints
    print("REQUESTED TAG IS:", request_folder)
    print("CURRENT PICK:", shuffle_list[0])
    if request_folder in random_tracker.keys():
        print("LAST PICK:", random_tracker[request_folder])
    # Ends here

    if request_folder in random_tracker.keys() and source_tag[0] == random_tracker[request_folder]:
        r = random.randint(0, 101)
        print("R is: ", r)
        if r > 50:
            random.shuffle(source_tag)
    else:
        random_tracker[request_folder] = shuffle_list[0]

    return str(shuffle_list[0])