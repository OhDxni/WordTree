import random
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
def load_words_from_file(filepath):
    """
    xxx
    :param filepath:
    :return:
    """
    words = set()

    # writes the words in file to words (set)
    with open(filepath, "r") as txt:
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


# ----------------------------------------------------------------------------------------------------------------------