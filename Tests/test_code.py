#import pytest
from Project_Code.helper_functions import letter_difference, depth_selector

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
def test_letter_difference():
   assert letter_difference("word", "dogs") == 3
   assert letter_difference("word", "word") == 0
   assert letter_difference("cat", "dog") == 3


# def test_save_json():


# def test_load_json():


def test_depth_selector_valid():
   result1 = depth_selector(4)
   assert (4 <= result1 <= 8)

   result2 = depth_selector(5)
   assert (5 <= result2 <= 9)

   result3 = depth_selector(6)
   assert (6 <= result3 <= 10)


def test_depth_selector_invalid():
   with pytest.raises(KeyError):
       depth_selector(3)


   with pytest.raises(KeyError):
       depth_selector("three")


#-------------------------------------------------------------------------------------------------------------------------
"""
Tests for game_logic.py
- class Game (
         - init
         - current_move
         - make move)
- class PathFinder (
         - end_word_selector
         - choose words)
"""



#-------------------------------------------------------------------------------------------------------------------------

"""
Tests for graph.py
- class Graph (
         - create_adj_list
         - save_adj_list
         - load_adj_list
         - a_pain_algorith)
"""

#-------------------------------------------------------------------------------------------------------------------------

"""
Tests for word_processing.py
- class WordProcessing(
         - _process_words
         - create_all_words
         - all_words_to_partitions
         - prune_partitions
         - filter_partitions
         - write_partitions)
"""
















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




