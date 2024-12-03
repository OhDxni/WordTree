import pytest
from Project_Code.helper_functions import letter_difference, depth_selector, load_json, save_json
from Project_Code.game_logic import Game, PathFinder
from Project_Code.word_processing import WordProcessing
from Project_Code.graph import Graph
"""
THIS FILE INCLUDES THE TESTS FOR OUR CODE
"""

#-------------------------------------------------------------------------------------------------------------------------
"""
Tests for the helper_functions.py file functions
1 - letter_difference(curr_word, neighbour)
2 - save_json(data, filepath)
3 - load_json(filepath)
4 - depth_selector(word_len)
"""

# tests for letter_difference
def test_letter_difference():
   assert letter_difference("word", "dogs") == 3
   assert letter_difference("word", "work") == 1
   with pytest.raises(ValueError, match= "Words must have the same length!"):
      letter_difference("car", "unique")      # to test when different letter inputs
   with pytest.raises(ValueError, match= "Please insert a word!"):
      letter_difference("", "word")



 # def test_save_json():
def test_save_json():
   with pytest.raises(FileNotFoundError):
      save_json("Some data", "unexisting/File/Path")


# tests for load_json():
def test_load_json():
   with pytest.raises(FileNotFoundError):
      load_json("Unexisting/File/Path")


# tests for depth selector
def test_depth_selector_valid():
   result1 = depth_selector(4)
   assert (4 <= result1 <= 8)
   result2 = depth_selector(5)
   assert (5 <= result2 <= 9)
   result3 = depth_selector(6)
   assert (6 <= result3 <= 10)
   with pytest.raises(ValueError, match= "This word length is not accepted!"):
      depth_selector(10)



#-------------------------------------------------------------------------------------------------------------------------
"""
Tests for game_logic.py
- class Game ( functions included:
         - current_move
         - make move)
- class PathFinder ( functions included:
         - end_word_selector
         - choose words)
"""

def test_current_move():
   game = Game()


def test_make_move():
   game = Game()



def test_end_word_selector():
   path = PathFinder()

def test_choose_words():
   path = PathFinder(game)
   with pytest.raises(FileNotFoundError):
      path.choose_words(3)







#-------------------------------------------------------------------------------------------------------------------------

"""
Tests for graph.py
- class Graph ( functions included:
         - create_adj_list
         - save_adj_list
         - load_adj_list
         - a_pain_algorith)
"""
def test_create_adj_list() :
   graph = Graph()

def test_save_adj_list():
   graph = Graph()

def test_load_adj_list():
   graph = Graph()

def test_a_pain_algorith():
   graph = Graph()


#-------------------------------------------------------------------------------------------------------------------------

"""
Tests for word_processing.py
- class WordProcessing( functions included:
         - process_words
         - create_all_words
         - all_words_to_partitions
         - prune_partitions
         - filter_partitions
         - write_partitions)
"""

def test_process_words():
   word = WordProcessing()


def test_create_all_words():
   word = WordProcessing()


def test_all_words_to_partitions():
   word = WordProcessing()


def test_prune_partitions():
   word = WordProcessing()

def test_filter_partitions():
   word = WordProcessing

def test_write_partitions():
   word = WordProcessing















#
# def test_all_possible_next_words_mind(self):  # testing so see if it finds correct neighbours
#     word = "MIND"
#     expected_neighbours = ('BIND', 'FIND', 'HIND', 'KIND', 'LIND', 'RIND', 'SIND', 'TIND', 'WIND', 'MAND', 'MEND', 'MILD', 'MINA', 'MINE', 'MING', 'MINI', 'MINK', 'MINO', 'MINT', 'MINX', 'MINY')
#     result = all_possible_next_words(word)
#     self.assertEqual(result, expected_neighbours)      # check to see if result matches expected
#
# def invalid_word(self):  # testing for a word  not from database
#     word = "ZXYS"
#     expected_neighbours = ()
#     result = all_possible_next_words(word)
#     self.assertEqual(result, expected_neighbours)
#


# if __name__ = "__main__":
#     unittest.main()




