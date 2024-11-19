import sqlite3  # Needed to read in the database
import string
import json
import csv
from helper_functions import load_words_from_file

# Connects sqlite3 package to the database file, and creates a cursor object based on it
database = sqlite3.connect("databases/linked_database.db")
cursor_obj = database.cursor()
# ----------------------------------------------------------------------------------------------------------------------
def all_possible_next_words(word):
    """
    This function, generates all the one letter difference words, to the word we need.
    (e.g., all_possible_next_word(MIND) -> KIND, MIND, ... and so on)
    :param word: the current word we need to find neighbours for
    :type word: str
    :return: all one letter difference words
    :rtype: tuple
    """
    # access database, find the word, print all its neighbours
    word = word.upper()
    cursor_obj.execute("SELECT Neighbours FROM linked_database WHERE Word = ?", (word,))
    neighbours = cursor_obj.fetchone()                  # Gets neighbours in the form of a tuple

    if neighbours is not None:
        neighbours_list = neighbours[0].split(",")
        return neighbours_list
# ----------------------------------------------------------------------------------------------------------------------
def create_linked_database(words_filepath):
    """
    Creates adjacency list ("database") where all neighbouring words are linked to each other
    using a dictionary. Results are stored in a .csv file named "linked_databse.csv".

    :param words_filepath: Filepath to file with ALL 4-, 5- and 6- letter words.
    :type: str
    """
    # Use process_words() to process words to prepare them for create_adj_list()
    words = load_words_from_file(words_filepath)

    # Use create_adj_list() to create the adjacency list
    adj_list = create_adj_list(words)

    # Write results to csv file
    with open("databases/linked_database.csv", "w", newline="") as file:
        file.write("Word,Neighbours\n")

        # Goes through all the keys and their values and writes each of them to a row
        # Here a csv.writer object is created to be able to use "writerow()"
        for word, neighbours in adj_list.items():
            all_neighbours = ",".join(neighbours) # Add all the values as a string together
            csv.writer(file).writerow([word, all_neighbours]) # Write the word to col1 and neighbours to col2
# ----------------------------------------------------------------------------------------------------------------------
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

        if not adj_list[word]:                     # if there are any connecting words, add them to the dictionary
            del adj_list[word]

    return adj_list
# ----------------------------------------------------------------------------------------------------------------------
def save_adj_list(words_filepath):
    words = load_words_from_file(words_filepath)
    adj_list = create_adj_list(words)
    with open(f"databases/adj_list_all_words.json", "w") as file:
        json.dump(adj_list, file)
# ----------------------------------------------------------------------------------------------------------------------
def load_adj_list():
    """
    xxx

    :return:
    """
    with open("databases/adj_list_all_words.json", "r") as file:
        return json.load(file)
# ----------------------------------------------------------------------------------------------------------------------