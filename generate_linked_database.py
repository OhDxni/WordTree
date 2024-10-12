import string

"""
You start with a database with all four-letter words.
You want to create and adjacency list (gather all the neighbours) of a certain word; where
in this case the neighbours will be the words with a one-letter difference.

To create an adjacency list, you iterate through each word in the x-letter valid guesses file.
You then take each charachter, and replace it with every single letter in the alphabet. If
one of them matches the word in the x-letter guesses file, you add the word in the adj. list.

This file contains three functions:
- process_words: processes words to be used in create_adj_list.
- create_adj_list: creates the adjaceny list.
- create_linked_databse: writes adjacency list to .txt file.
"""
def create_linked_database(words_filepath):
    """
    Creates adjacency list ("database") where all neighbouring words are linked to each other
    using a dictionary. Results are stored in a .txt file named "linked_databse.txt".

    :param words_filepath: Filepath to file with ALL 4-, 5- and 6- letter words.
    :type: str
    """
    # Use process_words() to process words to prepare them for create_adj_list()
    words = process_words(words_filepath)

    # Use create_adj_list() to create the adjacency list
    adj_list = create_adj_list(words)

    # Write results to text file
    with open(f"databases/linked_database.txt", "w") as txt:
        txt.write(str(adj_list))
    txt.close()

def process_words(words_filepath):
    """
    Converts the x-letter word databases into a format that can be used with the
    create_adj_list function.

    :param words_filepath: Filepath to file with ALL 4-, 5- and 6- letter words.
    :type words_filepath: str

    :return words: A list with all uppercase x-letter words and "\n" removed
    :rtype words: lst
    """
    words = set()
    with open(words_filepath, "r") as txt:
        for word in txt:
            word = word.replace("\n", "").upper()
            words.add(word)
    txt.close()
    return words

def create_adj_list(words):
    """
    Create adjacency list where all words with a single changed charachter are connected.

    :param words: a list with all 4-, 5- and 6-letter words.
    :type words: lst

    :return adj_list: returns adajceny list of all connected words in the form of a dictionary.
    :rtype adj_list: dict
    """
    adj_list = {}
    alphabet = string.ascii_uppercase

    for word in words:
        word = word.upper() # Make entire word uppercase
        adj_list[word] = [] # You intialise the value as a list, because a word will probably have several neighbours

        for index_char in range(len(word)): # Iterate over the index of each character in the word
            for letter in alphabet: # Iterate over each letter in the alphabet

                # For the current index, try out all letters and see if the newly created word is in the words list
                neighbour = word[:index_char] + letter + word[index_char+1:]
                if neighbour in words and neighbour != word:
                    adj_list[word].append(neighbour)
    return adj_list

### Generate linked_database.txt
all_words = "databases/all_words.txt"
create_linked_database(all_words)