"""
This Tkinter application provides a multi-page instruction guide for a word game.
Users are introduced to the game's rules and objectives, transitioning between pages
using "Next" buttons. The final page includes options to see an example or start
the game. The application is designed to enhance user understanding and engagement
before gameplay begins.

Functions:
- switchframe(frame): Raises the specified frame to the top, making it visible to the user.
"""

import tkinter as tk


def switchframe(frame):
    """
    Raises the given frame to the top, making it visible.

    :param frame: The frame to be raised.
    """
    frame.tkraise()


first = tk.Tk()
first.title("Instructions")
first.geometry("600x400")

frame1 = tk.Frame(first)
frame2 = tk.Frame(first)
frame3 = tk.Frame(first)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

# first page of the instructiosn
label1 = tk.Label(frame1, text="Here is how to play:\n\n"
                               "You are given a starting word of four five or six letters depending on your choice\n"

                               "you are also given a goal word\n""of equal length",
                  font=('Comic Sans MS', 14), wraplength=600)
label1.pack(pady=50)

nextbutton1 = tk.Button(frame1, text="Next", command=lambda: switchframe(frame2), bg="orange", fg="white",
                        font=('Arial', 12))
nextbutton1.pack(pady=20)

# second page
label2 = tk.Label(frame2,
                  text="You will be given options to choose from \n" "which alter exactly one letter \n" "in the given word.\n" "For example, a valid choice given\n"
                       "the word 'dog' would be 'bog'.",
                  font=('Comic Sans MS', 14), wraplength=500)
label2.pack(pady=50)

nextbutton2 = tk.Button(frame2, text="Next", command=lambda: switchframe(frame3), bg="orange", fg="white",
                        font=('Arial', 12))
nextbutton2.pack(pady=20)

# third page
label3 = tk.Label(frame3, text="The goal of the game is to go from the given word\n to the goal word\n"
                               "passing through as little intermediate words as possible.",
                  font=('Comic Sans MS', 14), wraplength=500)
label3.pack(pady=50)

see_example = tk.Button(frame3, text="See an Example", bg="blue", fg="white", font=('Arial', 12))
see_example.pack(side=tk.LEFT, padx=50, pady=20)

get_started = tk.Button(frame3, text="Get Started", bg="green", fg="white", font=('Arial', 12))
get_started.pack(side=tk.RIGHT, padx=50, pady=20)

switchframe(frame1)
first.mainloop()
