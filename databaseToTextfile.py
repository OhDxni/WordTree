#-----------------------------------------------------------------------------------------------------------------
def sort_words_by_length_6(input_file, output_file):
    """
    This function reads words from the input file of 370k words and
    find the 6-letter words to add to a new file, where one word on every line
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
    """
    with open(input_file, 'r') as f:
        words = f.read().strip().split()  # Split by spaces to get individual words

    # Write the 4-letter words to the output file
    with open(output_file, 'w') as outfile:         # open new file
        for word in words:                          # add the words one by one on new lines
            outfile.write(word.lower().strip() + "\n")      # Write each word to the new file


words_len_4("databases/4letterwords.txt", "databases/4_letter_valid_words.txt")

#----------------------------------------------------------------------------------------------------------------

def connecting_words_from_three_files(input_file1, input_file2, input_file3, output_file):
    """
    This function reads words from three input files, finds connecting words that differ by one letter,
    and stores the results as a dictionary in a new txt file.
    Each word is followed by its list of connecting words.
    """

    def find_connections(input_file):
        with open(input_file, 'r') as f:
            words = f.read().strip().splitlines()     # read, split into a list, strip of any leading, or trailing whitespace

        word_set = set(words)                         # convert list to set for quicker lookup
        connections = {}                              # dictionary to store connecting words

        # go through each word, try to find connections by substituting one letter at a time
        for word in words:
            connecting_words = []
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':          # iterate through all letters in the alphabet
                    if char != word[i]:                            # skip if same letter as one being replaced
                        new_word = word[:i] + char + word[i + 1:]  # substitute one letter
                        if (
                                new_word in word_set) and new_word not in connecting_words:  # check if the new word exists in the word set
                            connecting_words.append(new_word)      # add to list of connections

            if connecting_words:  # if there are any connecting words, add them to the dictionary
                connections[word] = connecting_words

        return connections

    connections1 = find_connections(input_file1)     # 4 letter connections
    connections2 = find_connections(input_file2)     # 5 letter connections
    connections3 = find_connections(input_file3)     # 6 lketter connections

    # combining connections from all three dictionaries into one with **
    combined_connections = {**connections1, **connections2, **connections3}

    # write the results to the output file
    with open(output_file, 'w') as f:
        for word, connects in combined_connections.items():
            f.write(f"{word}: {', '.join(connects)}\n")

    #return combined_connections


connecting_words_from_three_files("databases/4_letter_valid_words.txt",
                                  "databases/5_letter_valid_words.txt",
                                  "databases/6_letter_valid_words.txt",
                                  "databases/all_words_with_connections.txt")