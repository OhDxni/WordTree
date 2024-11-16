import random
from collections import deque # BFS
from generate_linked_database import create_adj_list
import heapq    # A*
import sqlite3  # Needed to read in the database
import time

# Connects sqlite3 package to the database file, and creates a cursor object based on it
database = sqlite3.connect("databases/linked_database.db")
cursor_obj = database.cursor()
# ----------------------------------------------------------------------------------------------------------------------
def find_neighbours(word):
    """
    Finds all neighbours of a certain word.

    :param word: Word from which you want to know all neighbours
    :type word: str
    :return neighbours_list: A list with all neighbours from "word"
    :rtype words: lst
    """
    # Execute on the cursor object is just a database query, where the parameter "word" gets used as "?"
    cursor_obj.execute("SELECT Neighbours FROM linked_database WHERE Word = ?", (word,))
    neighbours = cursor_obj.fetchone() # Gets neighbours in the form of a tuple

    # The query returns a tuple, so this converts it to a list
    if neighbours is not None:
        neighbours_list = neighbours[0].split(",")
        return neighbours_list

    # Needs to return an empty list in case the base case of the algorithm is triggerd
    else:
        return []

# print(find_neighbours("BOAT"))

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

def a_pain_algorith(start_word, end_word):
    """
    A* algorithm which finds the shortest path between a start and end word based
    on the amount of different letters between the words (hamming distance), which is
    calculated using the letter_difference function. Here, the find_neighbours function
    is used as well to find the neighbours of the start and current word.

    :param start_word: Starting word from which you want to find the shortest path
    :type start_word: str
    :param end_word: The final word you want to get to from the starting word
    :type end_word: str
    :return path: A list with all words needed to get from the starting word to the
    end word, including both the start and end words themselves
    :rtype path: lst
    """
    expected_cost = 0 + letter_difference(start_word, end_word)
    start_cost = 0
    path = [start_word]

    # First, the priority queue is constructed using above defined variables. Here it is
    # important to have the expected_cost at the FRONT of the tuple, because that's what
    # heapq will use to minimise the lenght of the path (cost). I put all of them in the
    # variable iteratable because I find that a bit more intuitive looking instead of
    # jamming the entire thing in the heappush statement.
    iteratable = (expected_cost, start_word, start_cost, path)
    priority_queue = []
    heapq.heappush(priority_queue, iteratable) # Pushes iteratable to priority_queue
    visited = set() # Set to keep track of visited neighbours

    while priority_queue:
        expected_cost, curr_word, curr_cost, path = heapq.heappop(priority_queue)

        # Base case: if end has been reached, return entire path
        if curr_word == end_word:
            return path, len(path)-1        # -1 to not include starting word in path length

        visited.add(curr_word)
        neighbours = find_neighbours(curr_word)
        print("curr", curr_word, "cost", curr_cost, "neighbours", neighbours)

        # Iterate over each neighbour, check if it's in visited, and if not determine cost and push
        for neighbour in neighbours:
            if neighbour not in visited:
                # New cost is +1 because its just one extra step/depth, while expected_cost is
                # calculated using the new cost and the remaining letter difference.
                new_cost = curr_cost + 1
                expected_cost = new_cost + letter_difference(curr_word, end_word)

                temp_path = path + [neighbour]
                heapq.heappush(priority_queue, (expected_cost, neighbour, new_cost, temp_path))
    return "Sorry, a path between the starting and end word wasn't found."

#print(a_pain_algorith("DEEK", "JOWS"))

# ----------------------------------------------------------------------------------------------------------------------

def bfs_traversal(adj):
    """
    Uses BFS traversal to find all the different partitions in an adjacency list
    :param adj: adjacency list of which partitions will be found
    :type adj: dictionary
    :return: partitions: set of partitions
    :rtype: partitions: set
    """
    visited = set()
    partitions = []
    for word in adj:                # Go through words in adjacency list
        if word not in visited:
            partition = set()       # creates a new partition for every new non visited element
            q = deque([word])

            while q:                            # fully explores a partition
                curr_word = q.popleft()
                if curr_word not in visited:    # checks if the word is visited
                    visited.add(curr_word)      # adds to visited list
                    partition.add(curr_word)    # adds to current partition
                    if curr_word in adj.keys():
                        for neighbour in adj[curr_word]:
                            q.append(neighbour) #appends all connections of the current word to the queue
            partitions.append(partition)        # when current partition is fully explored append it to list of partitions
    with open("databases/partitions.txt", "w", newline= "\n") as file:
        file.write(str(partitions))             # writes the partitions into a file
    return partitions

### Needs to go into function or main file
# words_filepath = "databases/all_words.txt"      # gets the filepath for use in adjlist
# words = set()                                   # creates a set to use in adjlist
#
# # writes the words in file to words (set)
# with open(words_filepath, "r") as txt:
#     for word in txt:
#         word = word.replace("\n", "").upper()
#         words.add(word)

# ----------------------------------------------------------------------------------------------------------------------
# function to select 2 words from a selected partition file and make sure they are at least
def choose_words(word_len):
    """
    This function chooses 2 words from a partitioning depending on word length chosen
    and makes sure the words are different enough, meaning at maximum 1 similar letter in the word
    :param word_len: the chosen word length; either 4, 5 or 6
    :type word_len: int
    :return: list of 2 words that will be used as start and end of the game
    :rtype: lst
    """

    filename = f"databases\partitions_{word_len}.txt"     # access the correct partitioning set from the right file
    with open(filename, "r") as file:                     # open the file, get the set
        words = eval(file.read().strip())

    words_list = list(words)                              # convert set to list

    while True:
        start_word = random.choice(words_list)            # choose a random word for start
        end_word = random.choice(words_list)              # random word as end

        if start_word == end_word:                        # making sure the words are not the same
            continue                                      # if same word, do while loop again, generating new start, end
        # checking that there is only one letter in common
        count = 0                                         # counter to make sure common letters not over 1
        for let1 in start_word:                           # loop through the words of start
            for let2 in end_word:                         # loop thrpugh words of end
                if let1 == let2:
                    count += 1                            # if they have same letters, up the count
                    if count > 1:                         # if more than one common letter, regenerate 2 words
                        break                             # exit let1 for loop, start again by generating new start and end
        else:
            start_and_end = []
            start_and_end.append(start_word)
            start_and_end.append(end_word)

            return start_and_end                          # return start and end word as a list
# print(choose_words(6))

# ----------------------------------------------------------------------------------------------------------------------
# Connects sqlite3 package to the database file, and creates a cursor object based on it
# database = sqlite3.connect("databases/linked_database.db")
# cursor_obj = database.cursor()
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
# Note that the print statements in this function should be replaced with/work alongside the buttons!
def game(word_len):
    """
    Function which allows the actual game to be played. Makes use of choose_words() to select
    a random beginning and starting word, and uses all_possible_next_words() to get all neighbours
    from the current word.
    :param word_len: the chosen word length; either 4, 5 or 6
    :type word_len: int
    :return: boolean value to indicate the traversal was succesful
    """
    # start_and_end = choose_words(word_len)
    # start_word, end_word = start_and_end
    start_word, end_word = "BOAT", "BOOK"

    curr_word = start_word
    while curr_word != end_word:
        neighbours = all_possible_next_words(curr_word)
        print("\ncurr", curr_word)
        print("neighbours",  neighbours)
        print("end", end_word)
        user_input = input("Pick word from neighbours: ").strip().upper()

        # Check to make sure chosen word is valid; note this is REDUDANT assuming the buttons work properly
        # it is not possible for the user to pick a word which isn't in the adj_list
        if user_input not in neighbours:
            print("!!!!! Neighbour not in adj_list !!!!!")
            continue

        curr_word = user_input

    # Check to make sure end word has been reached (redundant, but used for now to return True in case of win
    if curr_word == end_word:
        print("Yippieee! You got to the end word!")
        return True

game(4)
# ----------------------------------------------------------------------------------------------------------------------

#
# def partition_filter(set):
#     """
#     Loops through all partitions and only returns sizeable ones
#     :param set: set of partitions which will be filtered
#     :type set: set
#     :return: filtered list of partitions
#     :rtype: list
#     """
#     partitions = [] # Creates a list for the partitions
#     for partition in set: # Loops through the partitions
#         if len(partition) > 40: # Checks if the partitions are large enough and appends them to the list if so
#             partitions.append(partition)
#     return partitions
#
# # The following function should be in databaseToTextfile.py
# def partition_to_file(partition, filename):
#     with open(filename, 'w') as outfile:
#         for word in partition:
#             outfile.write(word.lower().strip()+ "\n")
#
# adj = create_adj_list(words) # gets the adj list
# partitions = bfs_traversal(adj) #excecution of the partitioning
# print(len(partitions)) # Prints the length of the unfiltered partitions
# partitions = partition_filter(partitions) # Filters the partitions
# print(len(partitions)) # Prints the length of the filtered partitions
# partition = partitions[0]
# partition_to_file(partition, "databases/partition_6.txt")
# partition = partitions[1]
# partition_to_file(partition, "databases/partition_5.txt")
# partition = partitions[2]
# partition_to_file(partition, "databases/partition_4.txt")







# def bfs_algorith(start_word, end_word):
#     iteratable = (start_word, [start_word])
#     queue = deque([iteratable]) # Initialises queue with starting word and path
#
#     visited = set() # Initialises set to keep track of the words that have been visited
#
#     while queue:
#         curr_word, path = queue.popleft() # Get first entry in the queue
#
#         if curr_word == end_word:
#             return path
#
#         visited.add(curr_word)
#         neighbours = find_neighbours(curr_word) # Uses find_neighbours function to find neighbours
#         # print("curr", curr_word, "neighbours", neighbours)
#
#         # If neighbour has not been visited yet, add it to the path and continue exploring
#         for neighbour in neighbours:
#             if neighbour not in visited:
#                 temp_path = path + [neighbour]
#                 queue.append((neighbour, path))
#
#     return "Sorry, a path between the starting and end word wasn't found."
# bfs_algorith("COWS", "MILK")

