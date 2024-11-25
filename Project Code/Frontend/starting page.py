"""
Creatimg a basic GUI for game featuring a start page with a logo and a button to initiate the game.

Functions:
- start_game(): Initiates the game when the Start button is clicked.
                Currently, it prints a message to the console, but this
                function can be expanded to include the actual game logic.
"""
import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Game Enter Page")
root.geometry("800x600")

logo = PhotoImage(file="logo.png")

# Create a label to display the logo
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=100)

def start_game():
    """
    Initiates the game when the Start button is clicked.

    This function will contain the logic to start the game.
    For now, it simply prints a message to the console.

    :return: None
    """
    print("Start button clicked")
    # Add logic to start the game here

# Create a Start button
start_button = tk.Button(root, text="Start", font=("Arial", 24), command=start_game)
start_button.pack(pady=20)  # Position the button below the logo

# Start the Tkinter event loop
root.mainloop()