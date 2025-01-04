import random
from collections import deque
from pathlib import Path
from Project_Code.helper_functions import depth_selector, load_json

project_root = (Path(__file__).resolve().parents[1]).as_posix()

class Game:
    def __init__(self, mode, adj_list):
        """
        Initialises all variables; changes after each step in the game

        :param mode: the chosen word length; either 4, 5 or 6
        :type mode: int
        """
        self.mode = mode                    # chosen mode eiher 4,5,6 leter words
        self.adj_list = adj_list
        self.path_finder = PathFinder(self)

        self.start_word, self.end_word = self.path_finder.choose_words(mode)
        self.curr_word = self.start_word
        self.curr_neighbours = self.adj_list[self.curr_word]

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
            return True
        else:
            self.curr_neighbours = self.adj_list[self.curr_word]


class PathFinder():
    def __init__(self, game):
        self.game = game

    def end_word_selector(self, start_word, depth):
        """
        This function finds and returns a word at a specified depth from the starting word; the adjacency
        list is on which a BFS-type traversal is used to find said (end-)word.

        :param start_word: The word where the search for the end word should start.
        :type start_word: str
        :param depth: The desired depth of where the end word should be found
        :type depth: int
        :return:
        """
        adj_list = self.game.adj_list

        curr_depth = 0
        queue = deque([(start_word, curr_depth)])
        visited = set()

        while queue:
            curr_word, curr_depth = queue.popleft()
            # print(curr_word, curr_depth)

            if curr_depth == depth:
                return curr_word

            for neighbour in adj_list[curr_word]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, curr_depth + 1))

    def choose_words(self, word_len):
        """
        This function chooses 2 words from a partitioning depending on word length chosen
        and makes sure the words are different enough, meaning at maximum 1 similar letter in the word

        :param word_len: the chosen word length; either 4, 5 or 6
        :type word_len: int
        :return: list of 2 words that will be used as start and end of the game
        :rtype: lst
        """
        try:
            words = load_json(f"{project_root}/databases/partitions_{word_len}.json")
        except FileNotFoundError:
            raise FileNotFoundError("Please turn on 'generate_partitions' in main.py")

        chosen_depth = depth_selector(word_len)
        start_word = random.choice(words)  # choose a random word for start
        end_word = self.end_word_selector(start_word, chosen_depth)

        return start_word, end_word




