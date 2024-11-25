
"""
Initialize and display the main start page- logo, a welcome message, and a button to
navigate to the login window.

Functions:
- open_start_page(): Initializes and opens the main start page of the game.
                     Sets up the application window with a logo, a welcome
                     message, and a Start button that opens the login window.
"""
import customtkinter
from tkinter import PhotoImage
from myloginWindow import open_login_window


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

# Function to open the start page
def open_start_page():
    """
    Initializes and opens the main start page of the game.

    This function sets up the main application window, including
    the logo, welcome message, and a Start button that opens
    the login window.

    :return: None
    """
    # Create the main window (Start page)
    global root
    root = customtkinter.CTk()
    root.geometry('800x600')
    root.title("Game Enter Page")

    # Create a frame to organize the logo, welcome text, and the button
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Load the logo image using tkinter's PhotoImage
    logo = PhotoImage(file="logo.png")  # Ensure the path to the image is correct

    # Create a label for the logo image
    label_logo = customtkinter.CTkLabel(master=frame, image=logo, text="")  # Show the image without text
    label_logo.image = logo  # Keep a reference to avoid garbage collection
    label_logo.pack(pady=10)  # Padding for logo

    # Add the welcome message between the logo and the button
    welcome_label = customtkinter.CTkLabel(master=frame, text="WELCOME TO WORD TREE", font=("Roboto", 24))
    welcome_label.pack(pady=10)  # Padding for welcome message

    # Create a Start button that opens the login window
    start_button = customtkinter.CTkButton(master=frame, text="Start", font=("Roboto", 24), command=open_login_window)
    start_button.pack(pady=10)  # Padding for Start button

    # "Go Back" button to go back to the start page
    # back_button = customtkinter.CTkButton(master=frame, text="Go Back",
    #                                       command=lambda: go_back_to_start_page(login_root))
    # back_button.pack(pady=12, padx=10)

    # Start the main loop for the Start page
    root.mainloop()

    # def go_back_to_start_page(login_root):
    #     login_root.destroy()  # Close the login window
    #     open_start_page()  # Reopen the start page

open_start_page()

