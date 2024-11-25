import pygame
import sys
import customtkinter as tk

# Global colors for buttons and screen
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
button_color = RED
button_hover_color = DARK_RED
button_text_color = (255, 255, 255)

# Initialize Tkinter root and Pygame screen in a frame
def initialize_tkinter_with_pygame():
    root = tk.CTk()
    root.title("Tree with Buttons")
    root.geometry("800x600")

    # Frame to hold Pygame display
    pygame_frame = tk.CTkFrame(root, width=800, height=600)
    pygame_frame.pack()

    # Run the Pygame interface inside Tkinter
    run_game_console(root, pygame_frame)

    root.mainloop()

def open_instructions_window(root):
    """
    Opens a separate instructions window on top of the main application.
    """
    tk.set_appearance_mode("system")
    tk.set_default_color_theme("green")

    def switchframe(frame):
        frame.tkraise()

    instructions_window = tk.CTkToplevel(root)  # Toplevel window makes it a separate window
    instructions_window.title("Instructions")
    instructions_window.geometry("500x500")
    instructions_window.transient(root)  # Keep it above the main window
    instructions_window.grab_set()  # Make it modal

    frame1 = tk.CTkFrame(instructions_window)
    frame2 = tk.CTkFrame(instructions_window)
    frame3 = tk.CTkFrame(instructions_window)

    for frame in (frame1, frame2, frame3):
        frame.grid(row=0, column=0, sticky='nsew')

    label1 = tk.CTkLabel(frame1, text="How to play:\n\n"
                                      "You start with a word of four, five, or six letters...\n\n"
                                      "and a goal word of equal length.",
                         font=('Roboto', 14), wraplength=500)
    label1.pack(pady=50)

    nextbutton1 = tk.CTkButton(frame1, text="Next", command=lambda: switchframe(frame2), font=('Roboto', 12))
    nextbutton1.pack(side=tk.RIGHT, padx=50, pady=20)

    backbutton1 = tk.CTkButton(frame1, text="Back", font=('Roboto', 12), command=instructions_window.destroy)
    backbutton1.pack(side=tk.LEFT, padx=50, pady=20)

    label2 = tk.CTkLabel(frame2, text="You will be given options to choose from...", font=('Roboto', 14), wraplength=500)
    label2.pack(pady=50)

    nextbutton2 = tk.CTkButton(frame2, text="Next", command=lambda: switchframe(frame3), font=('Roboto', 12))
    nextbutton2.pack(side=tk.RIGHT, padx=50, pady=20)
    backbutton2 = tk.CTkButton(frame2, text="Back", font=('Roboto', 12), command=lambda: switchframe(frame1))
    backbutton2.pack(side=tk.LEFT, padx=50, pady=20)

    label3 = tk.CTkLabel(frame3, text="Goal: Move from the start to goal word in the fewest steps.", font=('Roboto', 14), wraplength=500)
    label3.pack(pady=50)

    example_button = tk.CTkButton(frame3, text="See Example", font=('Roboto', 12))
    example_button.pack(side=tk.LEFT, padx=50, pady=20)

    start_button = tk.CTkButton(frame3, text="Get Started", font=('Roboto', 12), command=instructions_window.destroy)
    start_button.pack(side=tk.RIGHT, padx=50, pady=20)

    switchframe(frame1)
    instructions_window.wait_window()  # Modal dialog behavior

class Button:
    def __init__(self, x, y, radius, text, font):
        self.x = x
        self.y = y
        self.radius = radius
        self.text = text
        self.font = font
        self.clicked = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = button_hover_color if self.is_hovered(mouse_pos) else button_color
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        text_surface = self.font.render(self.text, True, button_text_color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius).collidepoint(mouse_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered(event.pos):
            self.clicked = True
            return True
        return False

def run_game_console(root, pygame_frame):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    font_default = pygame.font.SysFont('Arial', 20)
    buttons = [
        Button(200, 500, 50, "DEMO", font_default),
        Button(400, 500, 50, "4-WORDS", font_default),
        Button(600, 500, 50, "INSTRUCTIONS", font_default),
    ]

    running = True
    while running:
        screen.fill((135, 206, 250))

        for button in buttons:
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for button in buttons:
                if button.is_clicked(event):
                    if button.text == "INSTRUCTIONS":
                        open_instructions_window(root)  # Pass the root to open the instructions

        pygame.display.update()

    pygame.quit()
    sys.exit()

initialize_tkinter_with_pygame()
