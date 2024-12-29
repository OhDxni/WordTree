"""
Pygame Tree with Buttons Application

This application creates a graphical interface using Pygame to display a tree scene with buttons.
When buttons are clicked, it opens a Tkinter window showing instructions on how to play a word game.

Function:
- run_game_console: Initializes and runs the Pygame application to display a tree with buttons
  and manage user interactions through a graphical interface.

Nested Functions:
- open_instructions_window: Opens a Tkinter window that displays game instructions.
- draw_tree: Draws a stylized tree on the given Pygame surface.
- draw_clouds: Draws clouds on the given Pygame surface.
- Button (Class): Represents a clickable button in the game, handling drawing, hovering, and clicking functionality.
"""

import pygame
import sys
# import tkinter as tk
import customtkinter as tk
from tkinter import *
from Project_Code.graph import Graph
from Project_Code.word_processing import WordProcessing
from Project_Code.game_logic import Game

steps = 0

def run_game_console():
    """
    Initializes and runs the Pygame application to display a tree with buttons
    and manage user interactions through a graphical interface.
    """
    pygame.init()

    # print(pygame.display.Info())

    # screen = pygame.display.set_mode((1920, 1080))
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    #keeps the game console in the fullscreen
    pygame.display.set_caption('Tree with Buttons')

    # pygame.bind('<Escape>', pygame.quit())

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

    words_4 = ["tree", "love", "bird", "blue", "ship", "fire", "rock", "snow"]
    words_5 = ["apple", "grape", "peach", "lemon", "plumb", "berry", "melon", "olive"]
    words_6 = ["banana", "cherry", "orange", "apricot", "guava", "papaya", "quince", "figtree"]

    def quit_game(window):
        """
        Closes all windows and halts the program when X is clicked
        """
        window.destroy()
        try:
            pygame.quit()
        except pygame.error:
            pass



     
    # def open_word_grid(word_length, title):
    #
    #     word_root = tk.CTk()
    #     word_root.title(title)
    #     word_root.geometry("1920x1080+0+0")
    #     tk.set_default_color_theme("green")
    #
    #     # Adding a scrollbar to the window
    #     scrollbar = Scrollbar(word_root)
    #     scrollbar.pack(side=RIGHT, fill=Y)
    #
    #     # Binding the x in the top-right corner of the screen with halting the program
    #     word_root.protocol("WM_DELETE_WINDOW", lambda: quit_game(word_root))
    #
    #     wp = WordProcessing()
    #     wp.load_all_words()
    #     graph = Graph(wp.all_words)
    #     graph.load_adj_list()
    #
    #     def create_word_grid(root, word_length, rows, columns):
    #         frame = tk.CTkFrame(word_root)
    #         frame.pack(pady=10)
    #
    #         grid_frame = tk.CTkFrame(frame)
    #         grid_frame.pack()
    #
    #         game = Game(word_length, graph.adj_list)
    #
    #         start_word = game.curr_word
    #         print("\ncurr", game.curr_word)
    #
    #         # start = tk.CTkButton(grid_frame, text=start_word, width=100, height=40,
    #         #                     font=("Roboto", 12))
    #         label = tk.CTkLabel(master=frame, text=start_word, font=("Roboto", 14))
    #         label.pack(pady=12, padx=10)
    #
    #         # steps = 0
    #         # while game.curr_word != game.end_word:
    #         #     steps += 1
    #         #     print("\ncurr", game.curr_word)
    #         #     start_word = game.curr_word
    #         #     label = tk.CTkLabel(master=frame, text="start_word", font=("Roboto", 24))
    #         #     label.pack(pady=12, padx=10)
    #         #     create_word_grid(word_root, word_length, rows=2, columns=4)
    #
    #         # print("neighbours", game.curr_neighbours)
    #         # print("end", game.end_word)
    #         # user_input = input("Pick word from neighbours: ").strip().upper()
    #
    #         # move = game.make_move(user_input)
    #         # if move is False:
    #         #     continue
    #         # if move is True:
    #         #     print(f"Yippieee! You got to the end word in {steps} steps!")
    #         # break
    #
    #         # grid_words = [word_list[i:i + columns] for i in range(0, len(word_list), columns)]
    #
    #         def on_button_click(word):
    #             print(f"You clicked: {word}")
    #
    #     #     for r, row_words in enumerate(grid_words):
    #     #         for c, word in enumerate(row_words):
    #     #             button = tk.CTkButton(
    #     #                 grid_frame, text=word, width=100, height=40,
    #     #                 font=("Roboto", 12),
    #     #                 command=lambda w=word: on_button_click(w)
    #     #             )
    #     #             button.grid(row=r, column=c, padx=5, pady=5)
    #     #
    #     create_word_grid(word_root, word_length, rows=2, columns=4)
    #
    #     def go_back():
    #         word_root.destroy()
    #         run_game_console()
    #
    #     back_button = tk.CTkButton(word_root, text="← Go Back", width=100, height=40,
    #                                font=("Roboto", 12), command=go_back)
    #     back_button.pack(pady=20)
    #     word_root.mainloop()



    def open_word_grid(mode, title):

        word_root = tk.CTk()
        word_root.title(title)
        word_root.geometry("1920x1080+0+0")
        tk.set_default_color_theme("green")

        # scrollbar = Scrollbar(word_root)
        # scrollbar.pack(side=RIGHT, fill=Y)   #, orient=tk.VERTICAL)


        word_root.protocol("WM_DELETE_WINDOW", lambda: quit_game(word_root))

        wp = WordProcessing()
        wp.load_all_words()
        graph = Graph(wp.all_words)
        graph.load_adj_list()

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


        buttons_text = []
        def button_clicked():
            # button_text = button.text
            button_text = button.cget("text")
            buttons_text.append(button_text)
            # print(button_text)


        # Start game (class)
        if start_game:
        # window when start game

            # frame = tk.CTkFrame(word_root)
            # frame.pack(pady=10)

            grid_frame = tk.CTkFrame(word_root)
            grid_frame.pack()

            game = Game(mode, graph.adj_list)

            # # start = tk.CTkButton(grid_frame, text=start_word, width=100, height=40, font=("Roboto", 12))
            # # label = tk.CTkLabel(master=frame, text=start_word, font=("Roboto", 14))
            # # label.pack(pady=12, padx=10)
            # label = tk.CTkLabel(word_root, text=str(start_word), font=("Roboto", 20))
            # label.pack(pady=20)
            # # graph = Graph(wp.all_words)
            # # graph.load_adj_list()  # Sets graph.adj_list; if adj_list has not been created it does so automatically

            # game = Game(mode, graph.adj_list)

        # if shortest_path_print:
        #     print(graph.a_pain_algorith(game.curr_word, game.end_word))
        # i=0

            def clear_all_inside_frame(frame):
                # Iterate through every widget inside the frame
                for widget in frame.winfo_children():
                    widget.destroy()  # deleting widget


            def options():
                global steps  # Declare steps as a global variable to modify its value
                steps += 1
                # start_word = game.curr_word
                # start_label = tk.CTkLabel(grid_frame, text=str(start_word), font=("Roboto", 20))
                # start_label.pack(pady=20)
                # end_word = game.end_word
                # end_label = tk.CTkLabel(grid_frame, text=str(end_word), font=("Roboto", 20))
                # end_label.pack(pady=20, side=BOTTOM)
                # scrollbar = Scrollbar(grid_frame)
                # scrollbar.pack(side=RIGHT, fill=Y)  # , orient=tk.VERTICAL)
                start_word = game.curr_word
                start_label = tk.CTkLabel(grid_frame, text=str(start_word), font=("Roboto", 20))
                start_label.grid(row=0, column=3, pady=(20, 10))  # Place in row 0, spanning 2 columns
                # start_label.grid(row=0, column=3, columnspan=2, pady=(20, 10))  # Place in row 0, spanning 2 columns

                # end_word = game.end_word
                # end_label = tk.CTkLabel(grid_frame, text=str(end_word), font=("Roboto", 20))
                # end_label.grid(row=1, column=0, columnspan=2, pady=(10, 20))  # Place in row 1, spanning 2 columns

                # Add the scrollbar to the right side
                # scrollbar = Scrollbar(grid_frame, orient="vertical")
                # scrollbar.grid(row=0, column=2, rowspan=2, sticky="ns")  # Place in column 2, spanning rows 0 and 1

                # Ensure other widgets (e.g., buttons) are placed in rows starting from 2

                # for neighbour in game.curr_neighbours:
                #     next_word = tk.CTkButton(master=grid_frame, text=f"{neighbour}", command=lambda: word_chosen(next_word), font=("Arial", 12))
                #     # next_word = tk.CTkButton(master=grid_frame, text=f"{neighbour}", command=lambda: word_chosen(neighbour), font=("Arial", 12))
                #     next_word.pack(pady=10, padx=10)

                files = []  # creates list to replace your actual inputs for troubleshooting purposes
                btn = []  # creates list to store the buttons ins

                # for i, word in zip(range(len(game.curr_neighbours), game.curr_neighbours)):  # this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
                #     files.append()
                for word in game.curr_neighbours:  # this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
                    files.append(word)

                columns = 7  # Adjust this value as needed

                for i in range(len(files)):  # this says for *counter* in *however many elements there are in the list files*
                    # the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in
                    # btn.append(Button(grid_frame, text=files[i], command=lambda c=i: print(btn[c].cget("text"))))
                    btn.append(tk.CTkButton(grid_frame, text=files[i], command=lambda c=i: word_chosen(btn[c].cget("text"))))
                    # btn[i].pack(pady=5, padx=10)  # this packs the buttons
                    # Calculate row and column positions
                    row = 1 + i // columns
                    column = i % columns

                    # Place the button in the grid
                    btn[i].grid(row=row, column=column, padx=10, pady=10)

                end_word = game.end_word
                end_label = tk.CTkLabel(grid_frame, text=str(end_word), font=("Roboto", 20))
                end_label.grid(row=2+len(files), column=3, pady=(10, 20))  # Place in row 1, spanning 2 columns
                # end_label.grid(row=2+len(files), column=3, columnspan=2, pady=(10, 20))  # Place in row 1, spanning 2 columns

            def word_chosen(name):

                # user_choice = None
                # for button_text in buttons_text:
                #     if button_clicked.cget("text") == button_text:
                #        user_choice = button_text

                user_choice = name
                print(user_choice)
                move = game.make_move(user_choice)
                if move is False:
                    clear_all_inside_frame(grid_frame)
                    options()
                elif move is True:
                    print(f"Yippieee! You got to the end word in {steps} steps!")
                    # print("Yippieee!")

                # def word_chosen(button_clicked):
                #
                #     user_choice = None
                #     for button_text in buttons_text:
                #         if button_clicked.cget("text") == button_text:
                #            user_choice = button_text
                #
                #     # user_choice = name
                #     print(user_choice)
                #     move = game.make_move(user_choice)
                #     if move is False:
                #         clear_all_inside_frame(grid_frame)
                #         options()
                #     elif move is True:
                #         # print(f"Yippieee! You got to the end word in {steps} steps!")
                #         print("Yippieee!")

            options()



            # steps = 0
            # while game.curr_word != game.end_word:
            #     steps += 1
            #     print("\ncurr", game.curr_word)
            #     label = tk.CTkLabel(word_root, text=str(game.curr_word), font=("Roboto", 20))
            #     label.pack(pady=20)
            #
            #     for neighbour in game.curr_neighbours:
            #         next_word = tk.CTkButton(master=word_root, text=f"{neighbour}", command=lambda: word_chosen(neighbour), font=("Arial", 12))
            #         next_word.pack(pady=10, padx=10)


        #         for neighbour in game.curr_neighbours:
        #             # print(neighbour)
        #             button = tk.CTkButton(master=word_root,
        #                                   text=f"{neighbour}",
        #                                   command=button_clicked,
        #                                   font=("Arial", 12),
        #                                   )
        #             button.pack(pady=10, padx=10)
        # #
        # #     # replace end word with button
        # #     # print("end", game.end_word)
        # #
        # #     # user_input = input("Pick word from neighbours: ").strip().upper()
        # #
        # #     label = tk.CTkLabel(word_root, text=str(game.end_word), font=("Roboto", 20))
        # #     label.pack(pady=20)
        #         user_choice = game.curr_neighbours[0]
        #         print(f"machine_choice is {user_choice}")
        #     # # this part lowkey doesnt work
        #
        #         for button in buttons:
        #         if button_clicked():
        #             user_choice = button.cget("text")
        #             # user_choice = button.text
        #             # print("im here")
        #             print(f"user_choice is {user_choice}")
        #         # move = game.make_move(user_choice)
        #         # print(move)
        #         # break
        #         move = game.make_move(user_choice)
        #         if move is False:
        #             continue
        #         if move is True:
        #             print(f"Yippieee! You got to the end word in {steps} steps!")
        #             break
        # #     i+=1


        # def create_word_grid(root, word_list, rows, columns):
        #
        #     frame = tk.CTkFrame(word_root)
        #     frame.pack(pady=10)
        #
        #     grid_frame = tk.CTkFrame(frame)
        #     grid_frame.pack()
        #
        #     grid_words = [word_list[i:i + columns] for i in range(0, len(word_list), columns)]
        #
        #     def on_button_click(word):
        #         print(f"You clicked: {word}")
        #
        #     for r, row_words in enumerate(grid_words):
        #         for c, word in enumerate(row_words):
        #             button = tk.CTkButton(
        #                 grid_frame, text=word, width=100, height=40,
        #                 font=("Roboto", 12),
        #                 command=lambda w=word: on_button_click(w)
        #             )
        #             button.grid(row=r, column=c, padx=5, pady=5)
        #
        # create_word_grid(word_root, word_list, rows=2, columns=4)
        #
        # def go_back():
        #     word_root.destroy()
        #     run_game_console()
        #
        # back_button = tk.CTkButton(word_root, text="← Go Back", width=100, height=40,
        #                            font=("Roboto", 12), command=go_back)
        # back_button.pack(pady=20)
        word_root.mainloop()

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
                                          "You are given a starting word of four five or six letters\n\n" "depending on your choice\n\n"
    
                                          "you are also given a goal word\n\n""of equal length",
                             font=('Roboto', 14), wraplength=500)
        label1.pack(pady=50)

        nextbutton1 = tk.CTkButton(frame1, text="Next", command=lambda: switchframe(frame2),
                                   font=('Roboto', 12))
        nextbutton1.pack(side=tk.RIGHT, padx=50, pady=20)

        backbutton1 = tk.CTkButton(frame1, text="<- Back", font=('Roboto', 12),
                                   command=lambda: [first.destroy(), run_game_console()])
        backbutton1.pack(side=tk.LEFT, padx=50, pady=20)

        # second page
        label2 = tk.CTkLabel(frame2,
                             text="You will be given options to choose from \n\n" "which alter exactly one letter \n\n" "in the given word.\n\n" "For example, a valid choice given\n\n"
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

        see_example = tk.CTkButton(frame3, text="See an Example", font=('Roboto', 12))
        see_example.pack(side=tk.LEFT, padx=50, pady=20)

        get_started = tk.CTkButton(frame3, text="Get Started", font=('Roboto', 12), command=lambda: [first.withdraw(), run_game_console()])   #goes back to game console
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
                    else:
                        print(f"{button.text} clicked!")


          # ##And that would also have to change for the new version
          #   for button in buttons:
          #       if button.is_clicked(event):
          #           if button.text == "INSTRUCTIONS":
          #               pygame.quit()
          #               open_instructions_window()
          #           elif button.text == "4-WORDS":
          #               pygame.quit()
          #               open_word_grid(4, "4-Letter Words")
          #           elif button.text == "5-WORDS":
          #               pygame.quit()
          #               open_word_grid(5, "5-Letter Words")
          #           elif button.text == "6-WORDS":
          #               pygame.quit()
          #               open_word_grid(6, "6-Letter Words")
          #           else:
          #               print(f"{button.text} clicked!")

        pygame.display.update()


    pygame.quit()
    sys.exit()

# run_game_console()