"""
Implementing GUI. It includes functionalities for the start page, login page,
and registration page, allowing users to interact with the game.

Functions:
- open_start_page(): Initializes and displays the start page of the application,
                     featuring the game logo, a welcome message, and a Start button.
- open_login_window(): Creates and displays the login window for user authentication,
                       allowing users to input their credentials to access the game.
- login(): Prototype function for handling user login, including user credential
           verification and database interactions (currently a placeholder).
- open_register_window(): Opens the registration window for new users to create an
                          account, allowing them to input their desired username and password.
- register(): Prototype function for handling user registration, including validation
              of inputs and storing new user credentials in the database (currently a placeholder).
- go_back_to_login_page(root2): Hides the registration window and reopens the login window,
                                 enabling users to navigate back.
- go_back_to_start_page(login_root): Hides the login window and reopens the start page,
                                      allowing users to return to the main menu.
"""

import customtkinter
import tkinter as tk
from tkinter import PhotoImage
from game_console import run_game_console
# from RegisterWindow import open_register_window, create_root2
from hashlib import sha256
# h = sha256()
# h.update(b'python1990K00L')
# hash = h.hexdigest()
# print(hash)

root = customtkinter.CTk()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

# def create_toplevel_roots():
#     # Create a new root window for login
#     global login_root
#     login_root = customtkinter.CTkToplevel()
#     # login_root = customtkinter.CTk()
#     login_root.geometry("500x500")
#     login_root.title('Login to the game')
#     login_root.withdraw()


logo_image = None

# Function to open the start page
def open_start_page():
    """
    Creates and displays the start page of the application.

    :return: None
    """
    # Create the main window (Start page)
    global logo_image
    root.geometry('800x600')
    root.title("Game Enter Page")


    # Create a frame to organize the logo, welcome text, and the button
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Load the logo image and retain it as a global variable
    # logo_image = tk.PhotoImage(file="logo.png")  # Use `tk.PhotoImage` directly
    # label_logo = customtkinter.CTkLabel(master=frame, image=logo_image, text="")
    # label_logo.image = logo_image  # Explicitly attach image to label to prevent garbage collection
    # label_logo.pack(pady=10)

    # Load the logo image using tkinter's PhotoImage
    # logo = PhotoImage(file="logo.png")  # Ensure the path to the image is correct
    logo_image = PhotoImage(file="logo.png")  # Ensure the path is correct

    # Create a label for the logo image
    label_logo = customtkinter.CTkLabel(master=frame, image=logo_image, text="")  # Show the image without text
    label_logo.image = logo_image  # Keep a reference to avoid garbage collection
    label_logo.pack(pady=10)  # Padding for logo

    # Add the welcome message between the logo and the button
    welcome_label = customtkinter.CTkLabel(master=frame, text="WELCOME TO WORD TREE", font=("Roboto", 24))
    welcome_label.pack(pady=10)  # Padding for welcome message

    # Create a Start button that opens the login window
    start_button = customtkinter.CTkButton(master=frame, text="Start", font=("Roboto", 24), command=open_login_window)
    start_button.pack(pady=10)  # Padding for Start button

    # Start the main loop for the Start page
    root.mainloop()


# Function to open the login window
def open_login_window():
    """
    Creates and displays the login window for user authentication.

    :return: None
    """
    root.withdraw()  # Close the start window
    # Create a new root window for login
    global login_root
    login_root = customtkinter.CTkToplevel()
    # login_root = customtkinter.CTk()
    login_root.geometry("500x500")
    login_root.title('Login to the game')

    def login():
        print("login prototype")
    #open database
    #check if the username is in the database
        #if it is not throw an exception with a message "Username not found. If you do not have an account yet, register to the system"
    #if found, check if the hash of the typed passwored is the same as the hash saved
        #if not the same, give error "Wrong password"
    #if everything correct, go to run_game_console


    # def register_window():
    #     login_root.withdraw()
    #     open_register_window()

    # This is a frame for the login window
    frame = customtkinter.CTkFrame(master=login_root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # Adding a text at the top that says "Login to the game"
    label = customtkinter.CTkLabel(master=frame, text="Login to the game", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    # Adding username and password entries
    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")  # Encode the password
    entry2.pack(pady=12, padx=10)

    # Designing the login button
    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    # Designing the "Remember me" check box
    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
    checkbox.pack(pady=12, padx=10)

    # label asking the user if they do not have an account yet
    label = customtkinter.CTkLabel(master=frame, text="Do you not have an account yet? Then register below:",
                                   font=("Roboto", 12))
    label.pack(pady=12, padx=10)

    # button redirecting the user tothe register window
    button = customtkinter.CTkButton(master=frame, text="Register here", command=open_register_window)
    button.pack(pady=0, padx=10)


    # "Go Back" button to go back to the start page
    back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=lambda: go_back_to_start_page(login_root))
    # back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=go_back(login_root, open_start_page()))
    back_button.pack(pady=12, padx=10)
    login_root.deiconify()

    login_root.mainloop()  # Starting the login window loop


    # def create_root2():
    #     global root2
    #     root2 = customtkinter.CTkToplevel()
    #     root2.geometry("500x400")
    #     root2.withdraw()

def register():
    """
    Handles user registration, including username and password checks.

    :return: None
    """
    # connecting data to the database
    print("new user registered prototype")
    #check if the username already exists
        #if yes give an error "This username is already taken"
    #check if the input is correct for the username (not too short/long, does not use ',', etc.)
        #if incorrect give an error
    #Check if the first password is correct (not too short/long, does not use ',', etc.)
        #if incorrect give an error
    #check if the first and second passwords are the same
        # if not give an error
    #create a hash for the password
    #open the database
        #save the username and hash of password in the database
    #close the database
    #go to run_game_console


def open_register_window():
    """
    Creates and displays the registration window for new users.

    :return: None
    """
    login_root.withdraw()
    # root2.deiconify()
    root2 = customtkinter.CTkToplevel()
    root2.geometry("500x400")
    # print("Register window opened")
    # This is a frame for the login window, I can later change the size
    frame2 = customtkinter.CTkFrame(master=root2)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)

    # adding additional elements to the frame, so the login window

    # Adding a text at the top that says "Login to the game"
    label = customtkinter.CTkLabel(master=frame2, text="Register in the system to later access your statistics",
                                   font=("Roboto", 15))
    label.pack(pady=12, padx=10)

    # Adding username and password entries
    # Setting username
    entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)
    # Setting password
    entry2 = customtkinter.CTkEntry(master=frame2, placeholder_text="Password",
                                    show="*")  # Encoding the password so it doesn't show it, instead star symbols
    entry2.pack(pady=12, padx=10)
    # Confirming password
    entry3 = customtkinter.CTkEntry(master=frame2, placeholder_text="Confirm password",
                                    show="*")  # Encoding the password so it doesn't show it, instead star symbols
    entry3.pack(pady=12, padx=10)

    # designing the login button
    button = customtkinter.CTkButton(master=frame2, text="Register",
                                     command=register)  # command connects it to the function login that we will later implement
    button.pack(pady=12, padx=10)

    # "Go Back" button to go back to the login page
    back_button = customtkinter.CTkButton(master=frame2, text="Back to login",
                                          command=lambda: go_back_to_login_page(root2))
    # back_button = customtkinter.CTkButton(master=frame2, text="Go Back", command=go_back(root2, login_root))
    back_button.pack(pady=12, padx=10)

    root2.mainloop()


# def go_back(origin_root, destination_root):
#     origin_root.withdraw()
#     destination_root.deiconify()
def go_back_to_login_page(root2):
    """
    Hides the registration window and shows the login window again.

    :param root2: The registration window that will be hidden.
    :return: None
    """
    root2.withdraw()  # Close the login window
    login_root.deiconify()  # Reopen the start page

    # open_register_window()


def go_back_to_start_page(login_root):
    """
    Hides the login window and shows the start page again.

    :param login_root: The login window that will be hidden.
    :return: None
    """
    login_root.withdraw()  # Close the login window
    root.deiconify()    # Reopen the start page

# create_root2()
open_start_page()
