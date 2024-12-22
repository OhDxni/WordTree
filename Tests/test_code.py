import pytest
from Project_Code.helper_functions import letter_difference, depth_selector, load_json, save_json
from Project_Code.game_logic import Game, PathFinder
from Project_Code.word_processing import WordProcessing
from Project_Code.graph import Graph
from unittest.mock import patch
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
   assert letter_difference("word", "work") == 1
   with pytest.raises(ValueError, match= "Words must have the same length!"):
      letter_difference("car", "unique")                     # to test when different lengths inputs
   with pytest.raises(ValueError, match= "Please insert a word!"):
      letter_difference("", "word")



def test_save_json():
   with pytest.raises(FileNotFoundError):
      save_json("Some data", "unexisting/File/Path")



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

# Mock adjacency list for tests
@pytest.fixture
def adj_list():
    return {
        "WORD": ["WARD", "WORM"],
        "WARD": ["WORD", "CARD"],
        "WORM": ["WORD", "WARM"],
        "CARD": ["WARD", "CARP"],
        "CARP": ["CARD", "CAMP"],
        "WARM": ["WORM", "FARM"],
    }


# Mock load_json function
@pytest.fixture
def mock_load_json():
    with patch("Project_Code.helper_functions.load_json") as mocked_load_json:
        mocked_load_json.return_value = ["WORD", "WARD", "WORM", "CARD", "CARP", "CAMP", "WARM", "FARM"]
        yield mocked_load_json

# Mock depth_selector function
@pytest.fixture
def mock_depth_selector():
    with patch("Project_Code.helper_functions.depth_selector") as mocked_depth_selector:
        mocked_depth_selector.return_value = 2
        yield mocked_depth_selector


def test_end_word_selector1(adj_list):
    pathfinder = PathFinder(game=type("MockGame", (), {"adj_list": adj_list}))

    result = pathfinder.end_word_selector("WORD", 2)
    assert result in ["CARD", "WORD", "WARM"]           # words at depth 2 for WORD in the mock adj loist maade for testing



def test_game_initialization(adj_list):
    with patch.object(PathFinder, 'choose_words', return_value=("WORD", "WARM")):
        game = Game(mode= 4, adj_list= adj_list)

        assert game.start_word == "WORD"
        assert game.end_word == "WARM"
        assert game.start_word != game.end_word
        assert game.start_word in adj_list
        assert game.end_word in adj_list
        assert game.curr_word == "WORD"
        assert game.curr_neighbours == adj_list["WORD"]


def test_current_move(adj_list):
    with patch.object(PathFinder, 'choose_words', return_value=("WORD", "WARM")):
        game = Game(mode= 4, adj_list= adj_list)

    expected_result = {"curr_word" : "WORD", "curr_neighbours" : ["WARD" , "WORM"] , "end_word" : "WARM" }
    assert game.current_move() == expected_result



def test_make_move_valid(adj_list):
    with patch.object(PathFinder, 'choose_words', return_value=("WORD", "WARM")):
        game = Game(mode= 4, adj_list= adj_list)
    valid_move = "WORD"
    assert game.curr_word == "WORD"
    assert game.curr_neighbours == ["WARD", "WORM"]  # neighbors of "WARD", seeing if shows correctly


def test_make_move_invalid(adj_list):
    with patch.object(PathFinder, 'choose_words', return_value=("WORD", "WARM")):
        game = Game(mode= 4, adj_list= adj_list)
    invalid_move = "WRONG"
    assert game.make_move(invalid_move) is False
    assert game.curr_word == "WORD"
    assert game.curr_neighbours == ["WARD", "WORM"]


def test_make_move_winning(adj_list):
    with patch.object(PathFinder, 'choose_words', return_value= ("WORD", "WARM")):
        game = Game(mode= 4, adj_list= adj_list)
    winning_move = "WARM"
    assert game.make_move(winning_move) is True     # winning the game






# Test choose_words method in PathFinder
def test_choose_words():

# Test end_word_selector in PathFinder
def test_end_word_selector():


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

def test_save_adj_list():

def test_load_adj_list():

def test_a_pain_algorith():


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

















