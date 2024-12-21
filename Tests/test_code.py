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


# Mock data for testing
@pytest.fixture
def adj_list():
    return {
        "WORD": ["WARD", "WORM"],
        "WARD": ["WORD", "CARD"],
        "WORM": ["WORD", "WARM"],
        "CARD": ["WARD", "CARP"],
        "CARP": ["CARD", "CAMP"],
        "WARM": ["WORM", "FARM"]
    }


# Mock Game fixture
@pytest.fixture
def game(adj_list):
    return Game(mode=4, adj_list=adj_list)


# Mock load_json for PathFinder
@pytest.fixture
def mock_load_json():
    with patch("Project_Code.helper_functions.load_json") as mocked_load_json:
        mocked_load_json.return_value = ["WORD", "WARD", "WORM", "CARD", "CARP"]
        yield mocked_load_json


# Test Game Initialization
def test_game_initialization(adj_list):
    game = Game(mode=4, adj_list=adj_list)
    assert game.mode == 4
    assert game.adj_list == adj_list
    assert game.start_word in adj_list
    assert game.end_word in adj_list


# Test current_move method
def test_current_move(game):
    move_info = game.current_move()
    assert "curr_word" in move_info
    assert "curr_neighbours" in move_info
    assert "end_word" in move_info
    assert move_info["curr_word"] == game.start_word
    assert move_info["curr_neighbours"] == game.adj_list[game.start_word]
    assert move_info["end_word"] == game.end_word


# Test make_move method for a successful move
def test_make_move_success(game):
    valid_move = game.adj_list[game.start_word][0]
    result = game.make_move(valid_move)
    assert result is False
    assert game.curr_word == valid_move
    assert game.curr_neighbours == game.adj_list[valid_move]


# Test make_move method for an invalid move
def test_make_move_invalid(game):
    invalid_move = "INVALID"
    result = game.make_move(invalid_move)
    assert result is False
    assert game.curr_word == game.start_word


# Test make_move method for a winning move
def test_make_move_win(game):
    game.curr_word = game.end_word
    result = game.make_move(game.end_word)
    assert result is True


# Test choose_words method in PathFinder
def test_choose_words(mock_load_json, adj_list):
    game = Game(mode=4, adj_list=adj_list)
    pathfinder = PathFinder(game)

    start_word, end_word = pathfinder.choose_words(4)
    assert start_word in adj_list
    assert end_word in adj_list
    assert start_word != end_word

    # Test missing file scenario
    mock_load_json.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        pathfinder.choose_words(4)


# Test end_word_selector in PathFinder
def test_end_word_selector(game):
    pathfinder = PathFinder(game)
    result = pathfinder.end_word_selector("WORD", 2)
    assert result in game.adj_list

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

















