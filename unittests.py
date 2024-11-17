import unittest
from unittest.mock import patch
from graph_traversal import all_possible_next_words
from graph_traversal import choose_words
from graph_traversal import find_neighbours

"""
This file includes the unittests for our functions and code.
"""

# 1- testing to see if the find find_all_next_word finds the correct neighbours, when called

class TestGraphTraversal(unittest.TestCase):
    def test_all_possible_next_words_mind(self):  # testing so see if it finds correct neighbours
        word = "MIND"
        expected_neighbours = ('BIND', 'FIND', 'HIND', 'KIND', 'LIND', 'RIND', 'SIND', 'TIND', 'WIND', 'MAND', 'MEND', 'MILD', 'MINA', 'MINE', 'MING', 'MINI', 'MINK', 'MINO', 'MINT', 'MINX', 'MINY')
        result = all_possible_next_words(word)
        self.assertEqual(result, expected_neighbours)      # check to see if result matches expected

    def invalid_word(self):  # testing for a word  not from database
        word = "ZXYS"
        expected_neighbours = ()
        result = all_possible_next_words(word)
        self.assertEqual(result, expected_neighbours)


# if __name__ = "__main__":
#     unittest.main()


