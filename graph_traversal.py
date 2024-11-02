from collections import deque # BFS
from generate_linked_database import create_adj_list
import heapq # A*
import sqlite3 # Needed to read in the database
import time

# Connects sqlite3 package to the database file, and creates a cursor object based on it
database = sqlite3.connect("databases/linked_database.db")
cursor_obj = database.cursor()
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
            return path, len(path)-1 # -1 to not include starting word in path length

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

# print(a_pain_algorith("FLOSS", "TEETH"))

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
    for word in adj: # Go through words in adjacency list
        if word not in visited:
            partition = set() # creates a new partition for every new non visited element
            q = deque([word])

            while q: # fully explores a partition
                curr_word = q.popleft()
                if curr_word not in visited: # checks if the word is visited
                    visited.add(curr_word) # adds to visited list
                    partition.add(curr_word) # adds to current partition
                    if curr_word in adj.keys():
                        for neighbour in adj[curr_word]:
                            q.append(neighbour) #appends all connections of the current word to the queue
            partitions.append(partition) # when current partition is fully explored append it to list of partitions
    with open("databases/partitions.txt", "w", newline= "\n") as file:
        file.write(str(partitions)) # writes the partitions into a file
    return partitions

words_filepath = "databases/all_words.txt" # gets the filepath for use in adjlist
words = set() # creates a set to use in adjlist

# writes the words in file to words (set)
with open(words_filepath, "r") as txt:
    for word in txt:
        word = word.replace("\n", "").upper()
        words.add(word)

adj = create_adj_list(words) # gets the adj list
start_time = time.time() # start timer
bfs_traversal(adj) #excecution of the partitioning
end_time = time.time()  # End the timer
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")

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

