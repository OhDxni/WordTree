import json
from game_logic import Game

# Load adj_list
with open("databases/adj_list.json", "r") as file:
    adj_list = json.load(file)

# Start game
word_set = {
            "WOOF": "WOOT",
            "COOF": "COAL",
            # "WOOF": "BAFF",  # diff = 4
            "SAND": "GRIT",  # diff = 4
            "SORT": "KIND",  # diff = 5
            "YELL": "ROAR",  # diff = 5
            "DUNK": "ITCH",  # diff = 7
            "AMID": "ISLE",  # diff = 8
            }

for round, (start_word, end_word) in enumerate(word_set.items()):
    game = Game(4, adj_list, start_word, end_word)
    if round in (0, 1):
        print("#################")
        print(f"# Round {round+1}: Easy #")
        print("#################")
    elif round in (2, 3):
        print("###################")
        print(f"# Round {round+1}: Medium #")
        print("###################")
    elif round == 4:
        print("#################")
        print(f"# Round {round+1}: Hard #")
        print("#################")
    elif round == 5:
        print("######################")
        print(f"# Round {round+1}: Very Hard #")
        print("######################")

    steps = 0
    user_answers = []
    while game.curr_word != game.end_word:
        steps += 1
        print(f"\n----------------------------------- STEP {steps}")
        print("Current word", game.curr_word)
        print("Words with a one-letter difference:", game.curr_neighbours)
        print("End word", game.end_word, "\n")
        user_input = input(f"Pick one of the following words with a one-letter difference: ").strip().upper()
        user_answers.append((game.curr_word, user_input))
        print(user_answers)

        move = game.make_move(user_input)
        if move is False:
            steps -= 1
            continue
        if move is True:
            print(f"Yippieee! You got to the end word in {steps} steps!")
            break

    with open("databases/user_answers.txt", "a") as file:
        file.write(f"{user_answers}\n")
        file.write(f"{steps}\n")