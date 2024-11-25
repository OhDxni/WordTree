from Project_Code.Backend.graph import Graph
from Project_Code.Backend.word_processing import WordProcessing
from Project_Code.Backend.game_logic import Game

wp = WordProcessing()
wp.load_all_words()  # Sets wp.all_words; if all_words has not been created it does so automatically

graph = Graph(wp.all_words)
graph.load_adj_list()  # Sets graph.adj_list; if adj_list has not been created it does so automatically

# Flags
generate_partitions = 1
start_game = 1
shortest_path_print = 1

# Create partitions
if generate_partitions:
    wp.all_words_to_partitions(graph.adj_list)  # Sets partitions
    wp.prune_partitions()  # Sets pruned_partitions
    wp.filter_partitions()  # Sets filtered partitions
    wp.write_partitions()  # Writes partitions

# Start game (class)
if start_game:
    mode = int(input("Which mode (4, 5, 6)? "))
    game = Game(mode, graph.adj_list)

    if shortest_path_print:
        print(graph.a_pain_algorith(game.curr_word, game.end_word))

    steps = 0
    while game.curr_word != game.end_word:
        steps += 1
        print("\ncurr", game.curr_word)
        print("neighbours", game.curr_neighbours)
        print("end", game.end_word)
        user_input = input("Pick word from neighbours: ").strip().upper()

        move = game.make_move(user_input)
        if move is False:
            continue
        if move is True:
            print(f"Yippieee! You got to the end word in {steps} steps!")
            break

