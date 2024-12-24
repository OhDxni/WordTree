class Game:
    def __init__(self, mode, adj_list, start_word, end_word):
        """
        Initialises all variables; changes after each step in the game

        :param mode: the chosen word length; either 4, 5 or 6
        :type mode: int
        """
        self.mode = mode
        self.adj_list = adj_list

        self.start_word = start_word
        self.end_word = end_word
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
            print("\033[31mYou made a typo; please try again! :)\033[0m")
            return False

        self.curr_word = user_input

        if self.curr_word == self.end_word:
            return True
        else:
            self.curr_neighbours = self.adj_list[self.curr_word]