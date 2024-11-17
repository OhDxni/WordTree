from xword_processing import words_len4, words_len5, words_len6, merge_files
from xdatabase_management import create_adj_list, create_linked_database
from xpartioning import bfs_traversal, filter_partitions_by_word_length, write_partition_to_file
from xgame_logic import game
from xhelper_functions import load_words_from_file

def main():
    create_all_words = True
    create_database = False
    generate_partitions = False
    start_game = False

    # All words file creation
    if create_all_words:
        output_4 = "databases/4_letter_valid_words.txt"
        output_5 = "databases/5_letter_valid_words.txt"
        output_6 = "databases/6_letter_valid_words.txt"
        words_len4("databases/4letterwords.txt", output_4)
        words_len5("databases/370k_Word_File.csv", output_5)
        words_len6("databases/370k_Word_File.csv", output_6)
        merge_files(output_4, output_5, output_6)  # Outputs in all_words.txt

    # Initialising all_words.txt
    all_words_filepath = "databases/all_words.txt"
    all_words = load_words_from_file(all_words_filepath)

    # Database creation
    if create_database:
        create_linked_database(all_words)
        print("Database created :)\n")

    # Generate partitions
    if generate_partitions:
        adj_list = create_adj_list(all_words)
        partitions = bfs_traversal(adj_list)
        filtered_partitions = filter_partitions_by_word_length(partitions)
        write_partition_to_file(filtered_partitions)
        print("Partitions generated :)\n")

    # Start game
    if start_game:
        word_length = int(input("Which mode (4, 5, 6)? "))
        activating_game = game(word_length)
        if activating_game is True:
            print("Yippieee! You got to the end word!")
        else: print("You lost")

if __name__ == "__main__":
    main()