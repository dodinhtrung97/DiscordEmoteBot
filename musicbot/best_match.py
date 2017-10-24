import os
from musicbot import constants

def levenshtein(request_tag, source_tag, costs=(1, 1, 2)):
    """
    Calculate levenshtein distance, assumes insert, delete, substitution cost = 1
    :param request_tag: user input
    :param source_tag: source tag
    :return: levenshtein distance
    """
    rows = len(request_tag) + 1
    cols = len(source_tag) + 1
    delete, insert, substitute = costs

    dist = [[0 for x in range(cols)] for x in range(rows)]

    for row in range(1, rows):
        dist[row][0] = row * delete

    for col in range(1, cols):
        dist[0][col] = col * insert

    for col in range(1, cols):
        for row in range(1, rows):
            if request_tag[row - 1] == source_tag[col - 1]:
                cost = 0
            else:
                cost = substitute
            dist[row][col] = min(dist[row - 1][col] + delete,
                                 dist[row][col - 1] + insert,
                                 dist[row - 1][col - 1] + cost)

    return dist[row][col]


def decide_match(request_tag, type):
    """
    Returns appropriate image url
    :param request_tag: user input
    :param tag_list: source meme list
    :return: meme.url
    """
    best_score = float("inf")

    if type == ".png":
        path = constants.IMAGE_PATH
    else:
        path = constants.GIF_PATH

    for source_tag in os.listdir(path):
        source_tag = source_tag.split(type)[0]
        current_score = levenshtein(request_tag, source_tag)
        error_threshold = len(request_tag)/2
        # If current_score < some arbitrary number
        # Assumes that requested meme doesn't exist
        if current_score < best_score and current_score <= error_threshold:
            best_score = current_score
            best_match = source_tag

    try:
        return best_match
    except UnboundLocalError:
        return None


def decide_role(request_role, all_roles):
    """
    Returns appropriate image url
    :param request_tag: user input
    :param tag_list: source meme list
    :return: meme.url
    """
    best_score = float("inf")
    request_role = str(request_role).lower()
    best_match = None

    for role in all_roles:
        lower_role = str(role.name).lower().replace(" ", "")
        current_score = levenshtein(request_role, lower_role)
        error_threshold = len(request_role)/2
        # If current_score < some arbitrary number
        # Assumes that requested meme doesn't exist
        if current_score < best_score and current_score <= error_threshold:
            best_score = current_score
            best_match = role.name

    try:
        return best_match
    except UnboundLocalError:
        return None, "I appreciate your creativity but I can't assign you something that doesn't exist"
