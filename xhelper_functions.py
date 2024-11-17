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