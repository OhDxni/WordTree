

# 5- letter words are already ordered in csv file  and dont need
# to be dealt with,they can be accessed immediately during a game
# when file called to for example check words or something

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


# Merges all 4-, 5- and 6-letter words into one file (namely all_words.txt)
def merge_files(four, five, six):
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
# merge_files(four, five, six)