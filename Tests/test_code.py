import pytest
import tempfile
import os
import json
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

def test_save_json_success():
    """
    Test that the function successfully writes valid JSON data
    to a file without throwing an error.
    """
    test_data = {"key": "value", "nested": [1, 2, 3]}

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        filepath = tmp_file.name

    save_json(test_data, filepath) # Call save_json

    with open(filepath, "r") as file: # Read the file to check contents
        content = json.load(file)

    os.remove(filepath) # Clean up temporary file

    assert content == test_data # Check if the data matches up


def test_save_json_file_not_found():
    """
    Test that the function raises FileNotFoundError if the file path is invalid.
    """
    # Provide an invalid filepath to force FileNotFoundError
    invalid_filepath = "/non_existent_dir/some_file.json"

    # Check for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        save_json({"test": "data"}, invalid_filepath)

def test_load_json_success():
    """
    Test that the function successfully loads valid JSON data from a
    file without throwing an error
    """
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file: # Create a temporary file to check if load_json works
        filepath = tmp_file.name

    test_data = "test string" # Small test data

    with open(filepath, "w") as file: # Write the test data to the temp file
        json.dump(test_data, file)

    loaded_data = load_json(filepath) # Call load_json and store the results in loaded_data

    os.remove(filepath) # Remove temp file

    assert test_data == loaded_data # Check if the data matches up as it should

def test_load_json_file_not_found():
    """
    Test that the function raises FileNotFoundError if the file path is invalid.
    """
    # Provide an invalid filepath to force FileNotFoundError
    invalid_filepath = "/non_existent_dir/some_file.json"

    # Check for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        load_json(invalid_filepath)

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

@pytest.fixture
def mock_depth_selector():
    with patch("Project_Code.helper_functions.depth_selector") as mocked_depth_selector:
        mocked_depth_selector.return_value = 2
        yield mocked_depth_selector


def test_end_word_selector(adj_list):
    pathfinder = PathFinder(game= type("MockGame", (), {"adj_list": adj_list}))

    result = pathfinder.end_word_selector("WORD", 2)
    assert result in ["CARD", "WORD", "WARM"]           # words at depth 2 for WORD in the mock adj loist maade for testing

# def test_choose_words(adj_list, mock_depth_selector, mock_load_json):
#     pathfinder = PathFinder(game=type ("MockGame", (), {"adj_list": adj_list}))
#
#     mock_load_json.return_value = ["WORD", "WARD", "WORM", "CARD", "CARP", "WARM"]
#     mock_depth_selector.return_value = 2
#     start_word, end_word = pathfinder.choose_words(4)
#     assert start_word in adj_list
#     assert end_word in adj_list


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
    game.make_move("WORM")
    assert game.curr_word == "WORM"
    assert game.curr_neighbours == ["WORD", "WARM"]  # neighbors of "WORM", seeing if shows correctly


def test_make_move_invalid(adj_list):
    with patch.object(PathFinder, 'choose_words', return_value=("WORD", "WARM")):
        game = Game(mode= 4, adj_list= adj_list)
    invalid_move = "WRONG"
    assert game.make_move(invalid_move) is False
    assert game.curr_word == "WORD"
    assert game.curr_neighbours == ["WARD", "WORM"]


def test_make_move_winning(adj_list):
    with patch.object(PathFinder, 'choose_words', return_value= ("WORD", "WARD")):
        game = Game(mode= 4, adj_list= adj_list)
    winning_move = "WARD"
    assert game.make_move(winning_move) is True     # winning the game
    assert game.curr_word == "WARD"


#-------------------------------------------------------------------------------------------------------------------------

"""
Tests for graph.py
- class Graph ( functions included:
         - create_adj_list
         - save_adj_list
         - load_adj_list
         - a_pain_algorith)
"""


def test_graph_initialization():
    word_list = ["WORD", "WARD", "WORM", "CARD", "CARP", "CAMP", "WARM", "FARM", "WRONG"]
    graph = Graph(word_list)
    assert graph.all_words == word_list
    assert graph.adj_list is None


def test_create_adj_list() :
    word_list = ["WORD", "WARD", "WORM", "CARD", "CARP", "WARM", "WRONG"]
    graph = Graph(word_list)
    expected_result = { "CARD": ["WARD", "CARP"],
                        "CARP": ["CARD"],
                        "WARD": ["CARD", "WORD", "WARM"],
                        "WARM": ["WORM", "WARD"],
                        "WORD": ["WARD", "WORM"],
                        "WORM": ["WARM", "WORD"]}
    assert graph.create_adj_list() == expected_result


def test_save_adj_list():
    word_list = ["WORD", "WARD", "WORM", "CARD", "CARP", "WARM", "WRONG"]
    graph = Graph(word_list)
    raise KeyError("not complete")


def test_load_adj_list():
    word_list = ["WORD", "WARD", "WORM", "CARD", "CARP", "CAMP", "WARM", "FARM", "WRONG"]
    graph = Graph(word_list)
    raise KeyError("not complete")



def test_a_pain_algorith():
    word_list = ["WORD", "WARD", "WORM", "CARD", "CARP", "CAMP", "WARM", "FARM", "WRONG"]
    graph = Graph(word_list)
    graph.adj_list = {  "CARD": ["WARD", "CARP"],
                        "CARP": ["CARD"],
                        "WARD": ["CARD", "WORD", "WARM"],
                        "WARM": ["WORM", "WARD"],
                        "WORD": ["WARD", "WORM"],
                        "WORM": ["WARM", "WORD"]}
    expected_results = (["CARD", "WARD", "WARM", "WORM"], 3)
    assert graph.a_pain_algorith("CARD", "WORM") == expected_results
    with pytest.raises(KeyError, match= "Wrong word lengths"):
        graph.a_pain_algorith("CARD", "WRONG")


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
#
# def test_process_words():
#    word = WordProcessing()
#
#
# def test_create_all_words():
#    word = WordProcessing()
#
#
# def test_all_words_to_partitions():
#    word = WordProcessing()
#
#
# def test_prune_partitions():
#    word = WordProcessing()
#
# def test_filter_partitions():
#    word = WordProcessing
#
# def test_write_partitions():
#    word = WordProcessing
#
















