"""
Pygame Tree with Buttons Application

This application creates a graphical interface using Pygame to display a tree scene with buttons.
When buttons are clicked, it opens a Tkinter window showing instructions on how to play a word game.

Function:
- run_game_console: Initializes and runs the Pygame application to display a tree with buttons
  and manage user interactions through a graphical interface.

Nested Functions:
- fetch_user_data(user): Fetches the best scores from user database.
- quit_game: Closes all windows and halts the program.
- reset_steps: Resets the number of steps.
- display_leaderboard_and_personal_best(congrats_frame, username, mode): shows the leaderboard and personal best.
- congratulations(mode, game): Shows a congratulation message and shortest path possible after finished game.
- open_word_grid(mode, title): Opens and manages the game.
- clear_all_inside_frame: Deletes all widgets from the grid_frame.
- options: Populates the window of the game with all the correct and necessary widgets.
- word_chosen(name): Executes the move in the game.
- demo(): Give the users a simplified version of the final game with three-letter words and text to guide them
        to the correct end
- open_demo_page(): Gets rid of the disclaimer frame and starts the demo.
- show_page_1(): Shows the first page of the demo.
- go_to_page_2(): Destroys page one and shows page 2.
- show_page_2(): Shows the second page of the demo.
- go_to_page_3(): Destroys page two and goes to page three.
- show_page_3(): Shows page three of the demo.
- show_congratulations(): Destroys page three of demo and shows congrats message.
- show_congratulations_page(): Displays the congratulations screen.
- open_instructions_window: Opens a Tkinter window that displays game instructions.
- draw_tree: Draws a stylized tree on the given Pygame surface.
- draw_clouds: Draws clouds on the given Pygame surface.
- Button (Class): Represents a clickable button in the game, handling drawing, hovering, and clicking functionality.
"""

import pygame
import sys
import customtkinter as tk
from Project_Code.graph import Graph
from Project_Code.word_processing import WordProcessing
from Project_Code.game_logic import Game
from users_database import *


steps = 0    # Initializes steps outside any function to keep it as global variable


def run_game_console(user_name):
    """
    Initializes and runs the Pygame application to display a tree with buttons
    and manage user interactions through a graphical interface.

    :param user_name: username of the user playing the game
    :type user_name: str
    """

    username = user_name

    def fetch_user_data(user):
        """
        Fetches the best scores from user database.

        :param user: the user whose data is being fetched
        :type user: str
        :return: tuple containing best scores
        :rtype: tuple
        """
        connection = sqlite3.connect(f"{project_root}/databases/users_db.db")     # Opens the connection with the user database
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT best_4, best_5, best_6 FROM users WHERE username = ?", (user,))
        user_data = db_cursor.fetchone()
        connection.close()
        return user_data

    pygame.init()

    # screen = pygame.display.set_mode((1920, 1080))
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    # keeps the game console in the fullscreen
    pygame.display.set_caption('Tree with Buttons')

    # Define colors
    WHITE = (255, 255, 255)
    BROWN = (101, 67, 33)
    GREEN = (34, 139, 34)
    DARK_GREEN = (0, 100, 0)
    GRASS_GREEN = (0, 128, 0)
    RED = (255, 0, 0)
    DARK_RED = (200, 0, 0)
    SKY_BLUE = (135, 206, 250)
    CLOUD_COLOR = (255, 255, 255)

    # Define button properties
    button_color = RED
    button_hover_color = DARK_RED
    button_text_color = (255, 255, 255)

    # Font for button text
    font_very_small = pygame.font.SysFont('Arial', 18)
    font_small = pygame.font.SysFont('Arial', 24)
    font_default = pygame.font.SysFont('Arial', 28)

    def quit_game(window):
        """
        Closes all windows and halts the program when X is clicked.

        :param window: the window that is currently opened and needs to be closed
        :type window: tk.CTkToplevel
        """
        window.destroy()
        try:
            pygame.quit()
        except pygame.error:
            pass

    def reset_steps():
        """
        Resets the number of steps user made in the game to zero.
        """
        global steps  # Sets steps (initialized in the beginning of the file) as a global variable
        steps = 0

    def display_leaderboard_and_personal_best(congrats_frame, username, mode):
        """
        Fetches and displays the leaderboard and user's personal best scores for the given mode.

        :param congrats_frame: frame on which the leaderboard appears
        :type congrats_frame: tk.CTkFrame
        :param username: the username of the user playing
        :type username: str
        :param mode: the length of the words in the game
        :type mode: int
        """

        # Connecting to the database
        connection = sqlite3.connect(f"{project_root}/databases/users_db.db")
        cursor = connection.cursor()

        # Fetch leaderboard data for the current mode
        column = f"best_{mode}"
        query = f"SELECT username, {column} FROM users WHERE {column} IS NOT NULL ORDER BY {column} ASC LIMIT 3"
        cursor.execute(query)
        leaderboard = cursor.fetchall()

        # Fetch the personal best for the current user
        cursor.execute(f"SELECT {column} FROM users WHERE username = ?", (username,))
        personal_best = cursor.fetchone()
        personal_best = personal_best[0] if personal_best else "N/A"

        connection.close()

        # Create a label for the leaderboard
        leaderboard_label = tk.CTkLabel(
            congrats_frame,
            text=f"Top 3 Scores for {mode}-Letter Words:",
            font=("Roboto", 14),
        )
        leaderboard_label.pack(pady=5)

        # Display leaderboard
        for rank, (user, score) in enumerate(leaderboard, start=1):
            tk.CTkLabel(
                congrats_frame,
                text=f"{rank}. {user}: {score} steps",
                font=("Roboto", 12)
            ).pack(pady=2)

        # Display personal best
        personal_best_label = tk.CTkLabel(
            congrats_frame,
            text=f"Your Personal Best: {personal_best} steps",
            font=("Roboto", 12),
            fg_color="green"
        )
        personal_best_label.pack(pady=5)

    def congratulations(mode, game):
        """
        Shows a congratulation message after finished game and allows for further navigation through the app.

        :param mode: the length of the word in the game
        :type mode: int
        :param game: instance of the game being played
        :type game: Game
        """
        congrats_root = tk.CTkToplevel()
        congrats_root.title("Congratulations!")
        congrats_root.geometry("470x370+600+170")
        tk.set_default_color_theme("green")

        congrats_root.protocol("WM_DELETE_WINDOW", lambda: quit_game(congrats_root))

        congrats_frame = tk.CTkFrame(congrats_root)
        congrats_frame.pack(expand=True)    # the frame should occupy any empty space

        congrats_message = tk.CTkLabel(master=congrats_frame, text=f"Congratulations! You reached the end word in {steps} steps.", font=("Roboto", 12))
        congrats_message.pack(pady=15, padx=10)

        graph = Graph([])  # Initialize with empty; adj_list will be loaded
        graph.load_adj_list()  # Load adjacency list

        try:
            shortest_path, shortest_steps = graph.a_pain_algorith(game.start_word, game.end_word)
            shortest_path_message = (f"Shortest Path: {', '.join(shortest_path)}\n"
                                     f"Steps: {shortest_steps}")
        except Exception as e:
            shortest_path_message = "Could not calculate the shortest path."

        shortest_path_label = tk.CTkLabel(
            master=congrats_frame,
            text=shortest_path_message,
            font=("Roboto", 12),
            wraplength=400
        )
        shortest_path_label.pack(pady=10, padx=10)

        # This part fetches user stats from the database, and if the current score is better,
        # it updates the best score in the database
        user_stats = fetch_user_data(username)  # Gets a tuple of one best score for each game setting(word length)
        connection1 = sqlite3.connect(f"{project_root}/databases/users_db.db")  # Opens the connection with the user database
        cursor1 = connection1.cursor()

        if mode == 4:
            if (user_stats[0] is None) or (
                    user_stats[0] > steps):  # If no best score yet, or steps smaller than current best score
                cursor1.execute("""
                     UPDATE users 
                     SET best_4 = ?
                     WHERE username = ?
                 """, (steps, username))  # Updates the best score in database
                connection1.commit()

        elif mode == 5:
            if (user_stats[1] is None) or (user_stats[1] > steps):
                cursor1.execute("""
                     UPDATE users 
                     SET best_5 = ?
                     WHERE username = ?
                 """, (steps, username))
                connection1.commit()

        elif mode == 6:
            if (user_stats[2] is None) or (user_stats[2] > steps):
                cursor1.execute("""
                     UPDATE users 
                     SET best_6 = ?
                     WHERE username = ?
                 """, (steps, username))
                connection1.commit()

        connection1.close()

        display_leaderboard_and_personal_best(congrats_frame, username, mode)  # running the leaderboard on the

        # button going back to the game console
        back = tk.CTkButton(congrats_frame, text="<-Back to the tree", font=('Roboto', 12),
                            command=lambda: [congrats_root.withdraw(), reset_steps(), run_game_console(username)])
        back.pack(pady=15, padx=10)

        congrats_root.mainloop()

    def open_word_grid(mode, title):
        """
        Opens and manages the game itself.

        :param mode: length of the words
        :type mode: int
        :param title: title of the window based on the length of words
        :type title: str
        """

        word_root = tk.CTkToplevel()    # Creates a top level root
        word_root.title(title)
        word_root.geometry("1920x1080+0+0")
        tk.set_default_color_theme("green")

        word_root.protocol("WM_DELETE_WINDOW", lambda: quit_game(word_root))

        wp = WordProcessing()
        wp.load_all_words()
        graph = Graph(wp.all_words)
        graph.load_adj_list()

        # Flags
        generate_partitions = 1
        start_game = 1

        # Create partitions
        if generate_partitions:
            wp.all_words_to_partitions(graph.adj_list)  # Sets partitions
            wp.prune_partitions()  # Sets pruned_partitions
            wp.filter_partitions()  # Sets filtered partitions
            wp.write_partitions()  # Writes partitions

        if start_game:

            grid_frame = tk.CTkFrame(word_root)
            grid_frame.pack()
            game = Game(mode, graph.adj_list)   # Initializes the game

            def clear_all_inside_frame():
                """
                Deletes all widgets from the grid_frame.
                """
                for widget in grid_frame.winfo_children():    # Iterates through every widget inside the frame
                    widget.destroy()    # Deletes the widget

            def options():
                """
                Populates the window of the game with correct widgets every time it is called.
                Current word appears at the top, below there are buttons representing neighbouring
                words that can be chosen, at the bottom there is the end word and a back button
                taking user to the game console.
                """
                global steps    # Sets steps (initialized in the beginning of the file) as a global variable
                steps += 1      # Increases the steps every time new options show up, so keeps count of the steps

                # Next steps are necessary to allow for creation of different number of buttons and to ensure
                # that when clicked they trigger response of that specific button
                neighbours_words = []      # Creates list that will store neighbours (as words)
                btn_storage = []           # Creates list that will store buttons of neighbours

                for word in game.curr_neighbours:  # Populates neighbour_words with the neighbours
                    neighbours_words.append(word)

                columns = 7  # Sets the maximum number of columns in the grid

                for i in range(len(neighbours_words)):    # Iterates over the number of neighbours
                    # Creates a button for every neighbour and stores it in an array, so we can call it later
                    btn_storage.append(tk.CTkButton(grid_frame, text=neighbours_words[i], command=lambda c=i: word_chosen(btn_storage[c].cget("text"))))

                    row = 1 + (i // columns)    # Allocates the row in the grid(+1 because the start word is in row 0
                    column = i % columns        # Allocates the column in the grid
                    btn_storage[i].grid(row=row, column=column, padx=10, pady=10)   # Puts the button in the right place

                # Creates other widgets for the window
                start_label = tk.CTkLabel(grid_frame, text=str(game.curr_word), font=("Roboto", 20))
                end_label = tk.CTkLabel(grid_frame, text=str(game.end_word), font=("Roboto", 20))
                back = tk.CTkButton(grid_frame, text="<-Back to the tree", font=('Roboto', 12), command=lambda: [word_root.withdraw(), reset_steps(), run_game_console(username)])

                # Places other widgets on the screen in the middle, differently depending on number of options

                # less than seven neighbours and even number
                if len(neighbours_words) < 7 and (len(neighbours_words) % 2) == 0:
                    middle_column = len(neighbours_words) // 2
                    # Places start word in row 0, spanning 2 columns (because even number of buttons)
                    start_label.grid(row=0, column=middle_column-1, columnspan=2, pady=(20, 10))
                    # Places end word in the row after the last button row, spanning 2 columns
                    end_label.grid(row=2 + len(neighbours_words), column=middle_column-1, columnspan=2, pady=(10, 20))
                    # Places back button at the bottom, spanning two columns
                    back.grid(row=3 + len(neighbours_words), column=middle_column-1, columnspan=2, pady=(10, 20))

                else:
                    middle_column = 3    # otherwise

                    # less than seven neighbours and odd number
                    if len(neighbours_words) < 7 and (len(neighbours_words) % 2) == 1:
                        middle_column = (len(neighbours_words)-1)//2    # Gets the column of middle button

                    start_label.grid(row=0, column=middle_column, pady=(20, 10))
                    end_label.grid(row=2 + len(neighbours_words), column=middle_column, pady=(10, 20))
                    back.grid(row=3 + len(neighbours_words), column=middle_column, pady=(10, 20))

            def word_chosen(name):
                """
                Executes the move based on which button the user clicked and decides
                if the game continues or if the user reached the end word.

                :param name: the text of the button that user clicked
                :type name: str
                """
                user_choice = name                      # Sets the user choice to the text on button clicked
                move = game.make_move(user_choice)      # Executes the move (returns True if end mord is reached)

                if move is True:                        # If end reached
                    print(f"Yippieee! You got to the end word in {steps} steps!")
                    word_root.withdraw()                # Hides the window with the game
                    congratulations(mode, game)               # Calls congratulations window
                else:                                   # If end word not reached
                    clear_all_inside_frame()            # Deletes all widgets from the frame
                    options()  # Populates the frame with new current word, neighbour buttons, end word and back button

            options()    # Runs options for the first time

        word_root.mainloop()

    def demo():
        """Give the users a simplified version of the final game with three-letter words and text to guide them
        to the correct end"""
        def open_demo_page():
            """Gets rid of the disclaimer frame and starts the demo."""
            first_frame.destroy()
            show_page_1()

        def show_page_1():
            """shows the first page of the demo"""

            def go_to_page_2():
                """destroys page one and shows page 2"""
                demo_frame_1.destroy()
                show_page_2()
            # create first frame
            demo_frame_1 = tk.CTkFrame(demo_root, width=800, height=600)
            demo_frame_1.pack(pady=10, fill="both", expand=True)

            # start word label
            tk.CTkLabel(demo_frame_1, text="Pot", font=("Roboto", 20)).pack(pady=10)

            button_frame = tk.CTkFrame(demo_frame_1)
            button_frame.pack(pady=10)

            # create buttons for each option
            tk.CTkButton(button_frame, text="Dot", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Pop", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Pet", font=("Roboto", 18), command=go_to_page_2).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Pit", font=("Roboto", 18)).pack(side="left", padx=5)

            # goal word label and instructions method
            tk.CTkLabel(demo_frame_1, text="Ten", font=("Roboto", 20)).pack(pady=10)
            tk.CTkLabel(demo_frame_1, text="With the start word being \"pot\" and the goal word being \"ten\", "
                                           "\n the best option here would be \"pet\". Please select this option to continue! ",
                        font=("Roboto", 16)).pack(pady=10)

        def show_page_2():
            """shows the second page of the demo."""

            def go_to_page_3():
                """destroys page two and goes to page three"""
                demo_frame_2.destroy()
                show_page_3()

            # create page two
            demo_frame_2 = tk.CTkFrame(demo_root, width=800, height=600)
            demo_frame_2.pack(pady=10, fill="both", expand=True)

            # create start word label
            tk.CTkLabel(demo_frame_2, text="Pet", font=("Roboto", 20)).pack(pady=10)

            button_frame = tk.CTkFrame(demo_frame_2)
            button_frame.pack(pady=10)

            # create buttons for each option
            tk.CTkButton(button_frame, text="Put", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Pen", font=("Roboto", 18), command=go_to_page_3).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Pep", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Pat", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Peg", font=("Roboto", 18)).pack(side="left", padx=5)

            # end word label and instruction method
            tk.CTkLabel(demo_frame_2, text="Ten", font=("Roboto", 20)).pack(pady=10)
            tk.CTkLabel(demo_frame_2,
                        text="In this case, the best option would be \"pen\" because it is one letter away from the goal."
                             "\n Please select this option to continue!", font=("Roboto", 16)).pack(pady=10)

        def show_page_3():
            """shows page three of the demo."""

            def show_congratulations():
                """destroys page three of demo and shows congrats message"""
                demo_frame_3.destroy()
                show_congratulations_page()

            # create frame three
            demo_frame_3 = tk.CTkFrame(demo_root, width=800, height=600)
            demo_frame_3.pack(pady=10, fill="both", expand=True)

            # create start word label
            tk.CTkLabel(demo_frame_3, text="Pen", font=("Roboto", 20)).pack(pady=10)

            button_frame = tk.CTkFrame(demo_frame_3)
            button_frame.pack(pady=10)

            # create buttons for options
            tk.CTkButton(button_frame, text="Ten", font=("Roboto", 18), command=show_congratulations).pack(side="left",
                                                                                                           padx=5)
            tk.CTkButton(button_frame, text="Pet", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Tea", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Men", font=("Roboto", 18)).pack(side="left", padx=5)
            tk.CTkButton(button_frame, text="Pin", font=("Roboto", 18)).pack(side="left", padx=5)

            # end word label and instruction message
            tk.CTkLabel(demo_frame_3, text="Ten", font=("Roboto", 20)).pack(pady=10)
            tk.CTkLabel(demo_frame_3, text="In this case, the best option is ten as it is the goal word"
                                           "\nplease select this option to complete the game!",
                        font=("Roboto", 16)).pack(pady=10)

        def show_congratulations_page():
            """Displays the congratulations screen."""
            congrats_frame = tk.CTkFrame(demo_root, width=800, height=600)
            congrats_frame.pack(pady=10, fill="both", expand=True)

            # congrats label
            tk.CTkLabel(congrats_frame, text="Demo Completed!", font=("Roboto", 30)).pack(pady=20)
            # option to do demo again
            tk.CTkButton(congrats_frame, text="Play Again", font=("Roboto", 20),
                         command=lambda: [congrats_frame.destroy(), show_page_1()]).pack(pady=10)
            # return to tree page button
            tk.CTkButton(congrats_frame, text="Back to tree", font=("Roboto", 20),
                         command=lambda: [demo_root.destroy(), run_game_console(username)]).pack(pady=10)

        # Root setup
        demo_root = tk.CTkToplevel()
        tk.set_appearance_mode("system")
        demo_root.title("Game Demo")
        demo_root.geometry("750x500+575+100")
        tk.set_default_color_theme("green")

        # Disclaimer frame
        first_frame = tk.CTkFrame(demo_root, width=800, height=600)
        first_frame.pack(pady=10, fill="both", expand=True)

        # message to explain the demo
        disclaimer_label = tk.CTkLabel(
            first_frame,
            text="Please note this demo contains a simplified version of the game for the sake of time and clarity.",
            font=("Roboto", 12),
            wraplength=700,
            justify="center"
        )
        disclaimer_label.pack(pady=20)

        # button to display the demo
        continue_button = tk.CTkButton(
            first_frame,
            text="Continue to Demo",
            command=open_demo_page
        )
        continue_button.pack(pady=20)

        demo_root.mainloop()

    def open_instructions_window():
        """
        Opens a Tkinter window that displays game instructions.
        The window has multiple frames to navigate through instructions.
        """

        tk.set_appearance_mode("system")
        tk.set_default_color_theme("green")

        def switchframe(frame):
            """
            Raises the given frame to the top, making it visible.

            :param frame: The frame to be raised.
            :type frame: tk.CTkFrame
            """
            frame.tkraise()

        first = tk.CTk()
        first.title("Instructions")
        first.geometry("470x320+600+170")

        first.protocol("WM_DELETE_WINDOW", lambda: quit_game(first))

        frame1 = tk.CTkFrame(first)
        frame2 = tk.CTkFrame(first)
        frame3 = tk.CTkFrame(first)

        for frame in (frame1, frame2, frame3):
            frame.grid(row=0, column=0, sticky='nsew')
            # frame.pack(expand=True)

        # first page of the instructions
        label1 = tk.CTkLabel(frame1, text="Here is how to play:\n\n"
                                          "You are given a starting word of four, five, or"
                                          "\n six letters, depending on your choice.\n\n"
    
                                          "You are also given a goal word\n""of equal length.",
                             font=('Roboto', 14), wraplength=500)
        label1.pack(pady=50)

        nextbutton1 = tk.CTkButton(frame1, text="Next", command=lambda: switchframe(frame2),
                                   font=('Roboto', 12))
        nextbutton1.pack(side=tk.RIGHT, padx=50, pady=20)

        backbutton1 = tk.CTkButton(frame1, text="<- Back", font=('Roboto', 12),
                                   command=lambda: [first.destroy(), run_game_console(username)])
        backbutton1.pack(side=tk.LEFT, padx=50, pady=20)

        # second page
        label2 = tk.CTkLabel(frame2,
                             text="You will be given options to choose from \n" "which alter exactly one letter \n" 
                                  "in the given word. \n\n" "For example, a valid choice given\n"
                                  "the word 'dog' would be 'bog'.",
                             font=('Roboto', 14), wraplength=500)
        label2.pack(pady=50)

        nextbutton2 = tk.CTkButton(frame2, text="Next", command=lambda: switchframe(frame3),
                                   font=('Roboto', 12))
        nextbutton2.pack(side=tk.RIGHT, padx=50, pady=20)
        backbutton2 = tk.CTkButton(frame2, text="<- Back", font=('Roboto', 12), command=lambda: switchframe(frame1))
        backbutton2.pack(side=tk.LEFT, padx=50, pady=20)

        # third page
        label3 = tk.CTkLabel(frame3, text="The goal of the game is to go from the given word\n\n to the goal word\n\n"
                                          "passing through as little intermediate words as possible.",
                             font=('Roboto', 14), wraplength=500)
        label3.pack(pady=50)

        see_example = tk.CTkButton(frame3, text="See an Example", font=('Roboto', 12), command=lambda: [first.withdraw(), demo()])
        see_example.pack(side=tk.LEFT, padx=50, pady=20)

        get_started = tk.CTkButton(frame3, text="Get Started", font=('Roboto', 12), command=lambda: [first.withdraw(), run_game_console(username)])   #goes back to game console
        get_started.pack(side=tk.RIGHT, padx=50, pady=20)

        switchframe(frame1)
        first.mainloop()

    # Button class to handle drawing and interaction
    class Button:
        """
       Represents a clickable button in the game.

       Attributes:
           x (int): X coordinate of the button's center.
           y (int): Y coordinate of the button's center.
           radius (int): Radius of the button.
           text (str): Text displayed on the button.
           font: Font object used to render the button's text.
           clicked (bool): State of the button (clicked or not).
       """
        def __init__(self, x, y, radius, text, font):
            self.x = x
            self.y = y
            self.radius = radius
            self.text = text
            self.font = font
            self.clicked = False

        def draw(self, screen):
            """
            Draws the button on the screen with the appropriate color and text.

            :param screen: The Pygame surface on which to draw the button.
            """
            mouse_pos = pygame.mouse.get_pos()
            color = button_hover_color if self.is_hovered(mouse_pos) else button_color
            pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

            text_surface = self.font.render(self.text, True, button_text_color)
            text_rect = text_surface.get_rect(center=(self.x, self.y))
            screen.blit(text_surface, text_rect)

        def is_hovered(self, mouse_pos):
            """
            Checks if the mouse is hovering over the button.

            :param mouse_pos: Current position of the mouse.
            :return: True if the mouse is over the button, False otherwise.
            """
            return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius).collidepoint(
                mouse_pos)

        def is_clicked(self, event):
            """
            Checks if the button has been clicked.

            :param event: The event to check.
            :return: True if the button is clicked, False otherwise.
            """
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_hovered(event.pos):
                    self.clicked = True
                    return True
            return False

    # Function to draw the tree
    def draw_tree(screen):
        """
       Draws a stylized tree on the given screen.

       :param screen: The Pygame surface on which to draw the tree.
       """
        # Draw the trunk with shading for a 3D effect
        pygame.draw.rect(screen, BROWN, (930, 550, 60, 400))  # Trunk
        pygame.draw.rect(screen, (80, 50, 30), (960, 550, 30, 400))  # Shading

        # Branches
        pygame.draw.line(screen, BROWN, (960, 550), (400, 450), 30)  # Left
        pygame.draw.line(screen, BROWN, (960, 550), (1520, 450), 30)  # Right
        pygame.draw.line(screen, BROWN, (960, 450), (600, 350), 20)  # Middle-left
        pygame.draw.line(screen, BROWN, (960, 450), (1320, 350), 20)  # Middle-right
        pygame.draw.line(screen, BROWN, (960, 400), (960, 200), 20)  # Top

        # Foliage
        foliage_positions = [
            (400, 450, 120), (1520, 450, 120), (600, 350, 100),
            (1320, 350, 100), (960, 200, 120)
        ]
        for x, y, size in foliage_positions:
            pygame.draw.circle(screen, GREEN, (x, y), size)
            pygame.draw.circle(screen, DARK_GREEN, (x, y), size - 40)

        # Grass
        pygame.draw.rect(screen, GRASS_GREEN, (0, 950, 1920, 130))
        for i in range(0, 1920, 80):
            pygame.draw.circle(screen, GRASS_GREEN, (i, 960), 50)

    # Function to draw clouds
    def draw_clouds(screen):
        """
        Draws clouds on the given screen using circles.

        :param screen: The Pygame surface on which to draw the clouds.
        """
        # Draw clouds using circles
        cloud_positions = [
            (400, 150, 50), (450, 150, 70), (510, 150, 50),
            (1300, 200, 50), (1350, 200, 70), (1410, 200, 50),
            (900, 100, 40), (960, 100, 60), (1020, 100, 40)
        ]
        for x, y, radius in cloud_positions:
            pygame.draw.circle(screen, CLOUD_COLOR, (x, y), radius)

    buttons = [
        Button(500, 850, 80, "DEMO", font_default),
        Button(960, 850, 80, "4-WORDS", font_default),
        Button(1420, 850, 80, "INSTRUCTIONS", font_small),
        Button(730, 750, 80, "5-WORDS", font_default),
        Button(1190, 750, 80, "6-WORDS", font_default)
    ]

    # Main loop
    running = True
    while running:
        screen.fill(SKY_BLUE)  # Sky background

        # Draw clouds
        draw_clouds(screen)

        # Draw tree
        draw_tree(screen)

        # Draw buttons (apple-like buttons)
        for button in buttons:
            button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for button in buttons:
                if button.is_clicked(event):
                    if button.text == "INSTRUCTIONS":
                        pygame.quit()
                        open_instructions_window()
                    elif button.text == "4-WORDS":
                        pygame.quit()
                        open_word_grid(4, "4-Letter Words")
                    elif button.text == "5-WORDS":
                        pygame.quit()
                        open_word_grid(5, "5-Letter Words")
                    elif button.text == "6-WORDS":
                        pygame.quit()
                        open_word_grid(6, "6-Letter Words")
                    elif button.text == "DEMO":
                        pygame.quit()
                        demo()
                    else:
                        print(f"{button.text} clicked!")

        pygame.display.update()

    pygame.quit()
    sys.exit()

#run_game_console()
