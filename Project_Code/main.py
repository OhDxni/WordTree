from Project_Code.graph import Graph
from Project_Code.word_processing import WordProcessing
from Project_Code.game_logic import Game
import customtkinter as tk
from tkinter import *
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

def button_clicked():
    button_text = button.cget("text")
    print(button_text)


def quit_game(window):
    window.destroy()


# Start game (class)
if start_game:
    # window when start game
    tk.set_appearance_mode("system")
    tk.set_default_color_theme("green")
    root = tk.CTk()
    root.geometry("470x900")
    root.protocol("WM_DELETE_WINDOW", lambda: quit_game(root))

    # Adding a scrollbar to the window
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    # mode = int(input("Which mode (4, 5, 6)? "))
    mode = 4   #I WILL CHANGE TO MULTIPLE OPTIONS
    game = Game(mode, graph.adj_list)

    # if shortest_path_print:
    #     print(graph.a_pain_algorith(game.curr_word, game.end_word))

    steps = 0
    while game.curr_word != game.end_word:
        steps += 1
        print("\ncurr", game.curr_word)
        label = tk.CTkLabel(root, text=str(game.curr_word), font=("Roboto", 20))
        label.pack(pady=20)

        # print("neighbours", game.curr_neighbours)

        for neighbour in game.curr_neighbours:
            print(neighbour)
            button = tk.CTkButton(master=root,
                               text=f"{neighbour}",
                               command=button_clicked,
                               font=("Arial", 12),
                            )
            button.pack(pady=10, padx=10)

        # replace end word with button
        # print("end", game.end_word)

        # user_input = input("Pick word from neighbours: ").strip().upper()

        label = tk.CTkLabel(root, text=str(game.end_word), font=("Roboto", 20))
        label.pack(pady=20)

        #this part lowkey doesnt work
        if button_clicked():
            user_choice = button.cget("text")
            print("im here")

        move = game.make_move(user_choice)
        if move is False:
            continue
        if move is True:
            print(f"Yippieee! You got to the end word in {steps} steps!")
            break

