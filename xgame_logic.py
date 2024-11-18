import random
import heapq
from xhelper_functions import letter_difference
from xdatabase_management import find_neighbours, all_possible_next_words
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
        #print("curr", curr_word, "cost", curr_cost, "neighbours", neighbours)

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

# print(a_pain_algorith("GOATEE", "KAYOES"))
# ----------------------------------------------------------------------------------------------------------------------
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
        words = []  # Initialize an empty list to hold the words
        for line in file:  # Loop through each line in the file
            stripped_line = line.strip()  # Remove leading and trailing whitespace from the line
            if stripped_line:  # Check if the line is not empty after stripping
                words.append(stripped_line)  # Add the stripped line to the words list

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
class Game:
    def __init__(self, mode):
        """
        Initialises all variables; changes after each step in the game

        :param mode: the chosen word length; either 4, 5 or 6
        :type mode: int
        """
        self.mode = mode
        self.start_word, self.end_word = choose_words(mode)
        self.curr_word = self.start_word
        self.curr_neighbours = all_possible_next_words(self.curr_word)

    def current_move(self):
        """
        Retrieves information of the last played move

        :return: dictionary containing the current word, its neighbours and the final word of the last move
        :rtype: dict
        """
        curr_info = {}
        curr_info["curr_word"] = self.curr_word
        curr_info["curr_neighbours"] = self.curr_neighbours
        curr_info["end_word"] = self.end_word
        return curr_info

    def make_move(self, user_input):
        """
        Equals one move in the game, based on the given user input. Also contains check for win condition.

        :param user_input: user input selecting a word from the list of current neighbours
        :type user_input: str
        :return: bool
        """
        user_input = user_input.strip().upper()

        # REDUNDANT FOR FRONT END
        if user_input not in self.curr_neighbours:
            print("!!!!! Neighbour not in adj_list !!!!!")
            return False

        self.curr_word = user_input

        if self.curr_word == self.end_word:
            print("Yippieee! You got to the end word!")
            return True
        else:
            self.curr_neighbours = all_possible_next_words(self.curr_word)
# ----------------------------------------------------------------------------------------------------------------------