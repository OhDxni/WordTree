

# 5- letter words are already ordered in csv file  and dont need
# to be dealt with,they can be accessed immediately during a game
# when file called to for example check words or something

def sort_words_by_length_6(input_file, output_file):
    """
    This function reads words from the input file of 370k words and
    find the 6-letter words to add to a new file, where one word on every line
    """
    with open(input_file, 'r') as f:
        words = f.read().strip().splitlines()  # Read all lines and split into words

    # Write the 4-letter words to the output file
    with open(output_file, 'w') as outfile:         # Open the new file
        for word in words:                          # Add the words one by one on new lines
            if len(word) == 6:                      # Ensure that the word is exactly 4 letters long
                outfile.write(word.strip() + "\n")  # Write each 6-letter word to the new file



def words_len_4(input_file, output_file):
    """
    This function reads words from an input file containing ONLY 4-letter words
    and writes them to a new file where one word on every line.
    """
    with open(input_file, 'r') as f:
        words = f.read().strip().split()  # Split by spaces to get individual words

    # Write the 4-letter words to the output file
    with open(output_file, 'w') as outfile:         # open new file
        for word in words:                          # add the words one by one on new lines
            outfile.write(word.strip() + "\n")      # Write each word to the new file


sort_words_by_length_6("databases/370k_Word_File.csv", "databases/6_letter_valid_guesses.txt")
words_len_4("databases/4letterwords.txt", "databases/4_letter_valid_guesses.txt")

