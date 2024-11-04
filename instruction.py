"""
This Tkinter application provides a multi-page instruction guide for a word game.
Users are introduced to the game's rules and objectives, transitioning between pages
using "Next" buttons. The final page includes options to see an example or start
the game. The application is designed to enhance user understanding and engagement
before gameplay begins.

Functions:
- switchframe(frame): Raises the specified frame to the top, making it visible to the user.
"""

#import tkinter as tk
import customtkinter as tk

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

# first page of the instructiosn
label1 = tk.CTkLabel(frame1, text="Here is how to play:\n\n"
                               "You are given a starting word of four five or six letters\n\n" "depending on your choice\n\n"

                               "you are also given a goal word\n\n""of equal length",
                  font=('Roboto', 14), wraplength=500)
label1.pack(pady=50)

nextbutton1 = tk.CTkButton(frame1, text="Next", command=lambda: switchframe(frame2),
                        font=('Roboto', 12))
nextbutton1.pack(side=tk.RIGHT, padx=50, pady=20)

backbutton1 = tk.CTkButton(frame1, text="Back", font=('Roboto', 12), command=lambda: [first.withdraw(), run_game_console])
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

get_started = tk.CTkButton(frame3, text="Get Started", font=('Roboto', 12))
get_started.pack(side=tk.RIGHT, padx=50, pady=20)

switchframe(frame1)
first.mainloop()
