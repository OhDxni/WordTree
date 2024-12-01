"""
Implementing GUI. It includes functionalities for the start page, login page,
and registration page, allowing users to interact with the game.

Functions:
- open_start_page(): Initializes and displays the start page of the application,
                     featuring the game logo, a welcome message, and a Start button.
- open_login_window(): Creates and displays the login window for user authentication,
                       allowing users to input their credentials to access the game.
- login(): Function for handling logging into the game, user authentification
           and connection with the user database.
- open_register_window(): Opens the registration window for new users to create an
                          account, allowing them to input their desired username and password.
- register(): Function for handling user registration, including validation
              of inputs and storing new user credentials in the database.
"""

import customtkinter
from tkinter import PhotoImage, messagebox
# from testing_game_console import run_game_console
from Project_Code.game_console import run_game_console
from hashlib import sha256
from users_database import *


root = customtkinter.CTk()
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


logo_image = None    #initializing logo_image


# Function to open the start page
def open_start_page():
    """
    Creates and displays the start page of the application.

    :return: None
    """
    global logo_image
    root.title("Game Enter Page")
    root.geometry('1920x1080+0+0')     #sets the size, the wondow has corners in the corners of the screen

    # Create a frame to organize the logo, welcome text, and the button
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Load the logo image and retain it as a global variable
    logo_image = PhotoImage(file="../databases/logo.png")  # Ensure the path is correct

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
    root.bind("<Return>", lambda event: open_login_window())
    # Start the main loop for the Start page
    root.mainloop()


def open_login_window():
    """
    Creates and displays the login window for user authentication.

    :return: None
    """
    root.withdraw()  # Close the start window
    # Create a new root window for login
    global login_root
    login_root = customtkinter.CTkToplevel()
    login_root.geometry("500x500+575+100")
    login_root.title('Login to the game')

    login_root.protocol("WM_DELETE_WINDOW", root.destroy)    # binding the x in the top-right corner of the window to halting of the program


    # This is a frame for the login window
    frame = customtkinter.CTkFrame(master=login_root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # Adding a text at the top that says "Login to the game"
    label = customtkinter.CTkLabel(master=frame, text="Login to the game", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    # Adding username and password entries
    username_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    username_entry.pack(pady=12, padx=10)

    password_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")  # Hide the password
    password_entry.pack(pady=12, padx=10)

    # Designing the login button
    button = customtkinter.CTkButton(master=frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))  # lambda ensures that the function does not get executed when creating a button, get() get the actual imput of the fields
    button.pack(pady=12, padx=10)
    login_root.bind("<Retur"
                    "n>", lambda event: login(username_entry.get(), password_entry.get())) # Makes enter trigger the login button

    # label asking the user if they do not have an account yet
    label = customtkinter.CTkLabel(master=frame, text="Do you not have an account yet? Then register below:",
                                   font=("Roboto", 12))
    label.pack(pady=12, padx=10)

    # button redirecting the user to the register window
    button = customtkinter.CTkButton(master=frame, text="Register here", command=open_register_window)
    button.pack(pady=0, padx=10)


    # "Go Back" button to go back to the start page
    back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=lambda: [login_root.withdraw(), root.deiconify()])  # Executes two functions at once
    back_button.pack(pady=12, padx=10)
    login_root.deiconify()

    login_root.mainloop()  # Starting the login window loop


def login(username, password):
    """
    Checks the validity of user input (username and password)
    and logs the user into the system.

    :param username: username input
    :param password: password input
    :return: None
    """
    # opens the connection with the user database
    conn = sqlite3.connect('../../databases/users_db.db')
    cursor = conn.cursor()

    #checks if the username is in the database
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()    # fetches the tuple containing the encoded password of the user
    if user_data:
        # if data found, checks if the hash of the typed password is the same as the hash saved
        stored_password = user_data[0]
        if sha256(password.encode()).hexdigest() == stored_password:
            login_root.withdraw()
            # if everything correct, go to run_game_console
            run_game_console()

        else:
            # if password not the same, give error "Wrong password"
            messagebox.showerror("Error", "Wrong password")


    # if username not found, show an error with a message "Username not found"
    else:
        messagebox.showerror("Error", "Username not found")

    # closes the connection
    conn.close()



def open_register_window():
    """
    Creates and displays the registration window for new users.

    :return: None
    """
    login_root.withdraw()
    global register_root
    register_root = customtkinter.CTkToplevel()
    register_root.geometry("500x400+575+140")

    register_root.protocol("WM_DELETE_WINDOW", root.destroy)

    # This is a frame for the login window, I can later change the size
    frame2 = customtkinter.CTkFrame(master=register_root)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)

    # Adding a text at the top
    label = customtkinter.CTkLabel(master=frame2, text="Register in the system to later access your statistics",
                                   font=("Roboto", 15))
    label.pack(pady=12, padx=10)

    # Adding username and two password entries
    # Setting username
    username_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Username")
    username_entry.pack(pady=12, padx=10)
    # Setting password
    password_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Password",
                                    show="*")  # Encoding the password so it doesn't show it, instead star symbols
    password_entry.pack(pady=12, padx=10)
    # Confirming password
    password_confirm = customtkinter.CTkEntry(master=frame2, placeholder_text="Confirm password",
                                    show="*")  # Encoding the password so it doesn't show it, instead star symbols
    password_confirm.pack(pady=12, padx=10)

    # designing the login button
    button = customtkinter.CTkButton(master=frame2, text="Register",
                                     command=lambda: register(username_entry.get(), password_entry.get(), password_confirm.get()))
    button.pack(pady=12, padx=10)

    # "Go Back" button to go back to the login page
    back_button = customtkinter.CTkButton(master=frame2, text="Back to login",
                                          command=lambda: [register_root.withdraw(), login_root.deiconify()])
    back_button.pack(pady=12, padx=10)

    register_root.mainloop()

def register(username, password, password_confirmation):
    """
    Handles user registration, including username and password checks.

    :param username: username input
    :param password: password input
    :param password_confirmation: confirmation of the password input
    :return: None
    """
    conn = sqlite3.connect('../../databases/users_db.db')    # opening a connection with the database
    cursor = conn.cursor()

    #checks if the username already exists
    cursor.execute('SELECT username FROM users WHERE username = ?;', (username,))

    if cursor.fetchone():
        #if yes give an error "Username already exists"
        messagebox.showerror("Error", "Username already exists")

    # checks if the input is correct for the username (not too short/long)
    elif len(username) < 5 or len(username) > 15:
        messagebox.showerror("Register Error", "Username too short or too long")

    # checks if the passwords match
    elif password != password_confirmation:
        messagebox.showerror("Error", "Passwords do not match")

    else:
        # creates a hash for the password
        hashed_password = sha256(password.encode()).hexdigest()
        #saves the username and hash of password in the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        #gos to run_game_console
        register_root.withdraw()
        run_game_console()

    # closes the connection
    conn.close()


open_start_page()



