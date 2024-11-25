
"""
Creating a graphical user interface (GUI) for displaying grids of words
using the CustomTkinter library. It consists of the following key functions:
- create_word_grid: Generates a grid of buttons for the provided words.
- main: Initializes the application window and displays word grids for 4-, 5-, and 6-letter words.
"""
import customtkinter as tk


tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")
tk.set_widget_scaling(1.2)

def create_word_grid(root, word_list, rows, columns, title):
    """
    Creates a grid of buttons with words.

    This function generates a grid layout of buttons containing words from the provided
    word list. Each button is clickable and will print the word when clicked.

    :param root: The parent window in which to create the grid.
    :type root: ctk.CTk
    :param word_list: A list of words to be displayed on the buttons.
    :type word_list: list
    :param rows: The number of rows in the word grid.
    :type rows: int
    :param columns: The number of columns in the word grid.
    :type columns: int
    :param title: The title to be displayed above the grid.
    :type title: str
    """
    frame = tk.CTkFrame(root)
    frame.pack(pady=10)
    tk.CTkLabel(frame, text=title, font=("Roboto", 14)).pack()


    grid_frame = tk.CTkFrame(frame)
    grid_frame.pack()


    grid_words = [word_list[i:i + columns] for i in range(0, len(word_list), columns)]

    def on_button_click(word):
        """
        Callback function triggered when a button is clicked.
        This function handles the button click event and prints the clicked word.

        :param word: The word associated with the clicked button.
        :type word: str
        """
        print(f"You clicked: {word}")

    for r, row_words in enumerate(grid_words):
        for c, word in enumerate(row_words):
            button = tk.CTkButton(grid_frame, text=word, width=100, height=40,
                                   font=("Roboto", 12),
                                   command=lambda w=word: on_button_click(w))
            button.grid(row=r, column=c, padx=5, pady=5)

def main():
    """
    Main function to initialize the application window and create word grids.

    This function sets up the main application window, defines example word lists,
    and calls the `create_word_grid` function to display the grids for 4-, 5-, and 6-letter words.

    :param: None
    :type: None
    """
    root = tk.CTk()
    root.title("Wordle-like Button Grids")
    root.geometry("600x400")

    # Example word lists
    words_4 = ["tree", "love", "bird", "blue", "ship", "fire", "rock", "snow"]
    words_5 = ["apple", "grape", "peach", "lemon", "plumb", "berry", "melon", "olive"]
    words_6 = ["banana", "cherry", "orange", "apricot", "guava", "papaya", "quince", "figtree"]


    create_word_grid(root, words_4, rows=2, columns=4, title="4-Letter Words")
    create_word_grid(root, words_5, rows=2, columns=4, title="5-Letter Words")
    create_word_grid(root, words_6, rows=2, columns=4, title="6-Letter Words")

    root.mainloop()

if __name__ == "__main__":
    main()
