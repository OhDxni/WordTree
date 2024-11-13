
"""
This file is used to create text files that are used as the main word databases
for the game, categorizing words by length and also creating databases for partitionings.
"""


def sort_words_by_length_6(input_file, output_file):
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


sort_words_by_length_6("databases/370k_Word_File.csv", "databases/6_letter_valid_words.txt")


#-----------------------------------------------------------------------------------------------------------------

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


words_len5("databases/370k_Word_File.csv", "databases/5_letter_valid_words.txt")

#----------------------------------------------------------------------------------------------------------------

def words_len_4(input_file, output_file):
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


words_len_4("databases/4letterwords.txt", "databases/4_letter_valid_words.txt")

#----------------------------------------------------------------------------------------------------------------

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

### Generate all_words.txt
four = "databases/4_letter_valid_words.txt"
five = "databases/5_letter_valid_words.txt"
six = "databases/6_letter_valid_words.txt"
merge_files(four, five, six)

# --------------------------------------------------------------------------------------------------------------

def load_partitions_from_file(filename):
    """
    This function loads partitions from partition.txt to a list of sets,
    that have a length of over 40 words in a partition.
    :param filename: file containing partitions
    :type filename: str
    :return: list of sets, each set contains words in a partition
    :rtype: list[set[str]]
    """
    with open(filename, "r") as file:
        partitions = eval(file.read())              # evaluate string to Pythong object (list of sets)

    partitions_sets = []                            # list to store the partitions
    for partition in partitions:
        if len(partition) > 40:                     # make sure length iof partition is over 40
            partitions_sets.append(set(partition))  # turn each partition into a set and append to list

    return partitions_sets                          # return all the partitioned sets

# --------------------------------------------------------------------------------------------------------------

def filter_partitions_by_word_length(partitions):
    """
    This function filters the partition sets of already over len 40 into a dictionary
    dependnig on the word_lengths it has

    :param partitions: list of partition sets containing words
    :type partitions: list[set[str]]
    :return: Dictionary with keys 4, 5, and 6 for word lengths, each containing a list of partitions
    :rtype: dict[int, list[set[str]]]
    """
    filtered_partitions = {4:[],                # making keys for each word length to store their partitions
                           5:[],
                           6:[]}

    for partition in partitions:                # loop through partitions
        first_word = next(iter(partition))      # get the first element of the partition
        word_len = len(first_word)              # find the length of that word

        if word_len in filtered_partitions:     # make sure that length is already as a key in dictionary
            filtered_partitions[word_len].append(partition) # append the partition to the correct key/word length

    return filtered_partitions

# --------------------------------------------------------------------------------------------------------------

def write_partition_to_file(filtered_partitions):
    """
    This function writes the partitions to separate files for 4, 5, and 6-letter words.

    :param filtered_partitions: dictionary containing partitions for word lengths 4, 5, and 6
    :type filtered_partitions: dict[int, list[set[str]]]
    :return: None
    """
    for length in [4,5,6]:                                  # loop through neccesaary word lengths
        filename = f"databases/partitions_{length}.txt"     # create a filename based on length

        with open(filename, "w") as output_file:            # open new file
            for partition in filtered_partitions[length]:   # loop through partitions for x-letter words
                for word in partition:                      # write every word in partition to a new line
                    output_file.write(word.upper().strip() + "\n")

# --------------------------------------------------------------------------------------------------------------
# Using the functions to create the partitions_.txt files for every word length
partitions = load_partitions_from_file("databases/partitions.txt")    # get the partitions over length 40
filtered_partition = filter_partitions_by_word_length(partitions)     # filter them into dictionary of 3,4,5- letter word partitions
write_partition_to_file(filtered_partition)                           # create 3 new files based on word length including its partition over length 40

# --------------------------------------------------------------------------------------------------------------
