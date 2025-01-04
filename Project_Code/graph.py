import string
import heapq
from pathlib import Path
from Project_Code.helper_functions import save_json, load_json, letter_difference

project_root = (Path(__file__).resolve().parents[1]).as_posix()

class Graph():
    def __init__(self, all_words):
        self.all_words = all_words
        self.adj_list = None  # Initialise adj_list as None in case it doesn't exist yet (used for load_adj_list)

    def create_adj_list(self):
        """
        Create adjacency list where all words with a single changed character are connected.

        :return adj_list: returns adjacency list of all connected words in the form of a dictionary.
        :rtype adj_list: dict
        """
        adj_list = {}
        alphabet = string.ascii_uppercase

        for word in self.all_words:
            word = word.upper() # Make entire word uppercase
            adj_list[word] = [] # You intialise the value as a list, because a word will probably have several neighbours

            for index_char in range(len(word)): # Iterate over the index of each character in the word
                for letter in alphabet: # Iterate over each letter in the alphabet

                    # For the current index, try out all letters and see if the newly created word is in the words list
                    neighbour = word[:index_char] + letter + word[index_char+1:]
                    if neighbour in self.all_words and neighbour != word:
                        adj_list[word].append(neighbour)

            if not adj_list[word]:                     # if there are any connecting words, add them to the dictionary
                del adj_list[word]

        self.adj_list = adj_list
        return self.adj_list

    def save_adj_list(self):
        """
        A function to quickly save the adjacency list from the json file.
        """
        save_json(self.adj_list, f"{project_root}/databases/adj_list.json")

    def load_adj_list(self):
        """
        A function to quickly load the adjacency list from the json file.
        """
        try:  # Tries to load it; without try it always triggers the if-case (because adj_list set to None)
            self.adj_list = load_json(f"{project_root}/databases/adj_list.json")
        except (AttributeError, FileNotFoundError):
            if self.adj_list is None:
                self.adj_list = self.create_adj_list()
                self.save_adj_list()

    def a_pain_algorith(self, start_word, end_word):
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
        if len(start_word) != len(end_word):
            raise KeyError("Wrong word lengths")

        expected_cost = 0 + letter_difference(start_word, end_word)
        start_cost = 0
        path = [start_word]
        adj_list = self.adj_list

        # First, the priority queue is constructed using above defined variables. Here it is
        # important to have the expected_cost at the FRONT of the tuple, because that's what
        # heapq will use to minimise the length of the path (cost). I put all of them in the
        # variable iterable because I find that a bit more intuitive looking instead of
        # jamming the entire thing in the heappush statement.
        iteratable = (expected_cost, start_word, start_cost, path)
        priority_queue = []
        heapq.heappush(priority_queue, iteratable)  # Pushes iteratable to priority_queue
        visited = set()  # Set to keep track of visited neighbours

        while priority_queue:
            expected_cost, curr_word, curr_cost, path = heapq.heappop(priority_queue)

            # Base case: if end has been reached, return entire path
            if curr_word == end_word:
                return path, len(path) - 1  # -1 to not include starting word in path length

            visited.add(curr_word)
            neighbours = adj_list[curr_word]
            # print("curr", curr_word, "cost", curr_cost, "neighbours", neighbours)

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