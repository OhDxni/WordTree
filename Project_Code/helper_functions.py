import random
import json
# ----------------------------------------------------------------------------------------------------------------------
def letter_difference(curr_word, neighbour):
    """
    Finds the amount of different letters based on two words.

    :param curr_word: Current word you want to compare.
    :type curr_word: str
    :param neighbour: Neighbouring word you want to campare
    :type neighbour: str
    :return difference: The amount of different letters.
    :rtype words: int
    """
    if (len(curr_word) == 0) or (len(neighbour) == 0):
        raise ValueError("Please insert a word!")

    if len(curr_word) != len(neighbour):                             # having this to ensure correct functionality of code during testing
        raise ValueError("Words must have the same length!")

    difference = 0

    for x, y in zip(curr_word, neighbour):
        if x != y:
            difference += 1
    return difference


# ----------------------------------------------------------------------------------------------------------------------
def save_json(data, filepath):
    """
    Saves the data into a json file
    :param data:
    :param filepath:
    :return:
    """
    try:
        with open(filepath, "w") as file:
            json.dump(data, file)
    except FileNotFoundError:
        raise FileNotFoundError

# ----------------------------------------------------------------------------------------------------------------------
def load_json(filepath):
    """
    Loads the data from a json file
    :param filepath:
    :return:
    """
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError

# ----------------------------------------------------------------------------------------------------------------------
def depth_selector(word_len):
    """
    xxx

    :param word_len:
    :return:
    """
    depths_dict = {
        4: [4, 5, 6, 7, 8],
        5: [5, 6, 7, 8, 9],
        6: [6, 7, 8, 9, 10]
    }

    if word_len not in depths_dict:                             # for test cases neccessary to have
        raise ValueError("This word length is not accepted!")

    probabilities_dict = {
        4: [0.25, 0.35, 0.25, 0.10, 0.05],
        5: [0.25, 0.35, 0.25, 0.10, 0.05],
        6: [0.25, 0.35, 0.25, 0.10, 0.05]
    }

    picked_word_length = depths_dict[word_len]
    picked_probabilities = probabilities_dict[word_len]

    chosen_depth = random.choices(picked_word_length, weights=picked_probabilities)
    return chosen_depth[0]
# ----------------------------------------------------------------------------------------------------------------------