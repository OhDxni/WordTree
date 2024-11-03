import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.2)

def create_word_grid(root, word_list, rows, columns, title):

    frame = ctk.CTkFrame(root)
    frame.pack(pady=10)
    ctk.CTkLabel(frame, text=title, font=("Roboto", 14)).pack()


    grid_frame = ctk.CTkFrame(frame)
    grid_frame.pack()


    grid_words = [word_list[i:i + columns] for i in range(0, len(word_list), columns)]

    def on_button_click(word):
        print(f"You clicked: {word}")

    for r, row_words in enumerate(grid_words):
        for c, word in enumerate(row_words):
            button = ctk.CTkButton(grid_frame, text=word, width=100, height=40,
                                   font=("Roboto", 12),
                                   command=lambda w=word: on_button_click(w))
            button.grid(row=r, column=c, padx=5, pady=5)

def main():
    root = ctk.CTk()
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
