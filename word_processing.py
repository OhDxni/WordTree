# ----------------------------------------------------------------------------------------------------------------------
def words_len4(input_file, output_file):
    """
    This function reads words from an input file containing ONLY 4-letter words
    and writes them to a new file where one word on every line, also making them lower case.

    :param input_file: input file containing words
    :type input_file: str
    :param output_file: file where 4-letter words will be saved
    :type output_file: str
    :return: None
    """
    with open(input_file, 'r') as f:
        words = f.read().strip().split()                    # Split by spaces to get individual words

    # Write the 4-letter words to the output file
    with open(output_file, 'w') as outfile:                 # open new file
        for word in words:                                  # add the words one by one on new lines
            outfile.write(word.lower().strip() + "\n")      # Write each word to the new file
# ----------------------------------------------------------------------------------------------------------------------
def words_len5(input_file, output_file):
    """
    This function reads words from the input file of 370k words and
    find the 5-letter words to add to a new file, where one word on every line

    :param input_file: input file containing words
    :type input_file: str
    :param output_file: file where 5-letter words will be saved
    :type output_file: str
    :return: None
    """
    with open(input_file, 'r') as f:
        words = f.read().strip().splitlines()

        # write the 4-letter words to the output file
        with open(output_file, 'w') as outfile:              # open the new file
            for word in words:                               # add the words one by one on new lines
                if len(word) == 5:                           # ensure that the word is exactly 4 letters long
                    outfile.write(word.strip() + "\n")       # write each 6-letter word to the new file
# ----------------------------------------------------------------------------------------------------------------------
def words_len6(input_file, output_file):
    """
    This function reads words from the input file of 370k words and
    find the 6-letter words to add to a new file, where one word on every line

    :param input_file: input file containing words
    :type input_file: str
    :param output_file: file where 6-letter words will be saved
    :type output_file: str
    :return: None
    """
    with open(input_file, 'r') as f:                            # open input file, read it, strip and split lines
        words = f.read().strip().splitlines()

        # write the 4-letter words to the output file
        with open(output_file, 'w') as outfile:                 # open the new file
            for word in words:                                  # add the words one by one on new lines
                if len(word) == 6:                              # ensure that the word is exactly 4 letters long
                    outfile.write(word.strip() + "\n")          # write each 6-letter word to the new file
# ----------------------------------------------------------------------------------------------------------------------
# Merges all 4-, 5- and 6-letter words into one file (namely all_words.txt)
def merge_files(four, five, six):
    """
    This function merges 4-, 5-, and 6-letter words from different files into a single file.

    :param four: file containing 4-letter words
    :type four: str
    :param five: file containing 5-letter words
    :type five: str
    :param six: file containing 6-letter words
    :type six: str
    :return: None
    """
    with open(four, "r") as txt4, \
    open(five, "r") as txt5, \
    open(six, "r") as txt6, \
    open("databases/all_words.txt", "w") as txtall:

        for file in (txt4, txt5, txt6):
            for line in file:
                txtall.write(line)
# ----------------------------------------------------------------------------------------------------------------------