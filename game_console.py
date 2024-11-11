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


def run_game_console():
    """
    Initializes and runs the Pygame application to display a tree with buttons
    and manage user interactions through a graphical interface.
    """
    pygame.init()

    # pygame.protocol("WM_DELETE_WINDOW", pygame.quit())

    screen = pygame.display.set_mode((800, 600))
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
    font_very_small = pygame.font.SysFont('Arial', 12)
    font_small = pygame.font.SysFont('Arial', 16)
    font_default = pygame.font.SysFont('Arial', 20)

    words_4 = ["tree", "love", "bird", "blue", "ship", "fire", "rock", "snow"]
    words_5 = ["apple", "grape", "peach", "lemon", "plumb", "berry", "melon", "olive"]
    words_6 = ["banana", "cherry", "orange", "apricot", "guava", "papaya", "quince", "figtree"]

    def open_word_grid(word_list, title):

        root = tk.CTk()
        root.title(title)
        root.geometry("600x400")
        tk.set_default_color_theme("green")

        def create_word_grid(root, word_list, rows, columns):

            frame = tk.CTkFrame(root)
            frame.pack(pady=10)

            grid_frame = tk.CTkFrame(frame)
            grid_frame.pack()

            grid_words = [word_list[i:i + columns] for i in range(0, len(word_list), columns)]

            def on_button_click(word):
                print(f"You clicked: {word}")

            for r, row_words in enumerate(grid_words):
                for c, word in enumerate(row_words):
                    button = tk.CTkButton(
                        grid_frame, text=word, width=100, height=40,
                        font=("Roboto", 12),
                        command=lambda w=word: on_button_click(w)
                    )
                    button.grid(row=r, column=c, padx=5, pady=5)

        create_word_grid(root, word_list, rows=2, columns=4)

        def go_back():
            root.destroy()
            run_game_console()

        back_button = tk.CTkButton(root, text="← Go Back", width=100, height=40,
                                   font=("Roboto", 12), command=go_back)
        back_button.pack(pady=20)
        root.mainloop()

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
        first.geometry("500x500")

        frame1 = tk.CTkFrame(first)
        frame2 = tk.CTkFrame(first)
        frame3 = tk.CTkFrame(first)

        for frame in (frame1, frame2, frame3):
            frame.grid(row=0, column=0, sticky='nsew')

        # first page of the instructions
        label1 = tk.CTkLabel(frame1, text="Here is how to play:\n\n"
                                          "You are given a starting word of four five or six letters\n\n" "depending on your choice\n\n"
    
                                          "you are also given a goal word\n\n""of equal length",
                             font=('Roboto', 14), wraplength=500)
        label1.pack(pady=50)

        nextbutton1 = tk.CTkButton(frame1, text="Next", command=lambda: switchframe(frame2),
                                   font=('Roboto', 12))
        nextbutton1.pack(side=tk.RIGHT, padx=50, pady=20)

        backbutton1 = tk.CTkButton(frame1, text="Back", font=('Roboto', 12),
                                   command=lambda: [first.withdraw(), run_game_console()])
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
        backbutton2 = tk.CTkButton(frame2, text="Back", font=('Roboto', 12), command=lambda: switchframe(frame1))
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
        pygame.draw.rect(screen, BROWN, (390, 350, 20, 200))  # Center trunk
        pygame.draw.rect(screen, (80, 50, 30), (400, 350, 10, 200))  # Darker side for depth

        # Draw branches, more spaced out
        pygame.draw.line(screen, BROWN, (400, 350), (150, 300), 15)  # Leftmost branch
        pygame.draw.line(screen, BROWN, (400, 350), (650, 300), 15)  # Rightmost branch
        pygame.draw.line(screen, BROWN, (400, 300), (220, 230), 10)  # Middle-left branch
        pygame.draw.line(screen, BROWN, (400, 300), (580, 230), 10)  # Middle-right branch
        pygame.draw.line(screen, BROWN, (400, 270), (400, 170), 10)  # Top branch

        # Draw some foliage on the branches
        pygame.draw.circle(screen, GREEN, (150, 300), 50)  # Leftmost foliage
        pygame.draw.circle(screen, DARK_GREEN, (150, 300), 30)  # Darker inner foliage

        pygame.draw.circle(screen, GREEN, (650, 300), 50)  # Rightmost foliage
        pygame.draw.circle(screen, DARK_GREEN, (650, 300), 30)  # Darker inner foliage

        pygame.draw.circle(screen, GREEN, (220, 230), 40)  # Left middle foliage
        pygame.draw.circle(screen, DARK_GREEN, (220, 230), 20)  # Darker inner foliage

        pygame.draw.circle(screen, GREEN, (580, 230), 40)  # Right middle foliage
        pygame.draw.circle(screen, DARK_GREEN, (580, 230), 20)  # Darker inner foliage

        pygame.draw.circle(screen, GREEN, (400, 170), 50)  # Top foliage
        pygame.draw.circle(screen, DARK_GREEN, (400, 170), 30)  # Darker inner foliage

        # Add dark green grass at the bottom of the tree
        pygame.draw.rect(screen, GRASS_GREEN, (0, 550, 800, 50))
        for i in range(0, 800, 40):
            pygame.draw.circle(screen, GRASS_GREEN, (i, 550), 30)


    # Function to draw clouds
    def draw_clouds(screen):
        """
        Draws clouds on the given screen using circles.

        :param screen: The Pygame surface on which to draw the clouds.
        """
        # Draw clouds using circles
        pygame.draw.circle(screen, CLOUD_COLOR, (150, 100), 30)
        pygame.draw.circle(screen, CLOUD_COLOR, (180, 100), 40)
        pygame.draw.circle(screen, CLOUD_COLOR, (220, 100), 30)

        pygame.draw.circle(screen, CLOUD_COLOR, (600, 150), 30)
        pygame.draw.circle(screen, CLOUD_COLOR, (630, 150), 40)
        pygame.draw.circle(screen, CLOUD_COLOR, (670, 150), 30)

        pygame.draw.circle(screen, CLOUD_COLOR, (400, 80), 25)
        pygame.draw.circle(screen, CLOUD_COLOR, (430, 80), 35)
        pygame.draw.circle(screen, CLOUD_COLOR, (470, 80), 25)


    # Create round buttons
    buttons = [
        Button(200, 500, 50, "DEMO", font_default),
        Button(400, 500, 50, "4-WORDS", font_default),
        Button(600, 500, 50, "INSTRUCTIONS", font_very_small),
        Button(300, 440, 50, "5-WORDS", font_default),
        Button(500, 440, 50, "6-WORDS", font_default)
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
                        open_word_grid(words_4, "4-Letter Words")
                    elif button.text == "5-WORDS":
                        pygame.quit()
                        open_word_grid(words_5, "5-Letter Words")
                    elif button.text == "6-WORDS":
                        pygame.quit()
                        open_word_grid(words_6, "6-Letter Words")
                    else:
                        print(f"{button.text} clicked!")


        pygame.display.update()


    pygame.quit()
    sys.exit()

# run_game_console()