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
    difference = 0

    for x, y in zip(curr_word, neighbour):
        if x != y:
            difference += 1
    return difference
# ----------------------------------------------------------------------------------------------------------------------
def load_words_from_file(words_filepath):
    """
    Converts the x-letter word databases into a format that can be used with the
    create_adj_list function.

    :param words_filepath: Filepath to file with ALL 4-, 5- and 6- letter words.
    :type words_filepath: str

    :return words: A list with all uppercase x-letter words and "\n" removed
    :rtype words: lst
    """
    words = set()

    # writes the words in file to words (set)
    with open(words_filepath, "r") as txt:
        for word in txt:
            word = word.replace("\n", "").upper()
            words.add(word)
    return words
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

    probabilities_dict = {
        4: [0.3, 0.3, 0.2, 0.15, 0.05],
        5: [0.3, 0.3, 0.2, 0.15, 0.05],
        6: [0.3, 0.3, 0.2, 0.15, 0.05]
    }

    picked_word_length = depths_dict[word_len]
    picked_probabilities = probabilities_dict[word_len]

    chosen_depth = random.choices(picked_word_length, weights=picked_probabilities)
    return chosen_depth[0]
# print(depth_selecter(4))
# ----------------------------------------------------------------------------------------------------------------------