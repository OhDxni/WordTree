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
"""

import customtkinter
import tkinter as tk
from tkinter import PhotoImage, messagebox
# from testing_game_console import run_game_console
from game_console import run_game_console
from hashlib import sha256
from users_database import *


root = customtkinter.CTk()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
logo_image = None

# def center_window(window):
#     screen_width = window.winfo_screenwidth()
#     screen_height = window.winfo_screenheight()
#     x = (screen_width - window.winfo_reqwidth()) // 2
#     # y = ((screen_height - window.winfo_reqheight()) // 2) #- window.geometry()//2
#     window.geometry(f"+{x}")
#     # window.geometry(f"+{x}+{y}")

# def center(win):
#     """
#     centers a tkinter window
#     :param win: the main window or Toplevel window to center
#     """
#     win.update_idletasks()
#     width = win.winfo_width()
#     frm_width = win.winfo_rootx() - win.winfo_x()
#     win_width = width + 2 * frm_width
#     height = win.winfo_height()
#     titlebar_height = win.winfo_rooty() - win.winfo_y()
#     win_height = height + titlebar_height + frm_width
#     x = win.winfo_screenwidth() // 2 - win_width // 2
#     y = win.winfo_screenheight() // 2 - win_height // 2
#     win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     win.deiconify()

# Function to open the start page
def open_start_page():
    """
    Creates and displays the start page of the application.

    :return: None
    """
    global logo_image
    # root.geometry('800x600')
    # root.geometry('1920x1080')
    # root.geometry('750x250')
    root.title("Game Enter Page")
    x = root.winfo_screenwidth() // 2
    y = int(root.winfo_screenheight() * 0.1)
    root.geometry('800x600+' + str(x) + '+' + str(y))
    # center_window(root)
    # root.eval('tk::PlaceWindow . center')
    # center(root)
    # root.attributes('-fullscreen', True)
    # print(root.winfo_reqwidth())
    # print(root.winfo_screenwidth())

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

# def quit_all_roots():
#     try:
#         root2.quit()
#     except:
#         pass
#     login_root.quit()
#     root.quit()



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
    # center_window(login_root)

    # login_root.protocol("WM_DELETE_WINDOW", quit_all_roots)


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

    # # Designing the "Remember me" check box
    # checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
    # checkbox.pack(pady=12, padx=10)

    # label asking the user if they do not have an account yet
    label = customtkinter.CTkLabel(master=frame, text="Do you not have an account yet? Then register below:",
                                   font=("Roboto", 12))
    label.pack(pady=12, padx=10)

    # button redirecting the user to the register window
    button = customtkinter.CTkButton(master=frame, text="Register here", command=open_register_window)
    button.pack(pady=0, padx=10)


    # "Go Back" button to go back to the start page
    back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=lambda: [login_root.withdraw(), root.deiconify()])  # Executes two functions at once
    # back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=go_back(login_root, open_start_page()))
    back_button.pack(pady=12, padx=10)
    login_root.deiconify()

    login_root.mainloop()  # Starting the login window loop


def login(username, password):
    print("login prototype")
    #open database
    conn = sqlite3.connect('users_db.db')
    cursor = conn.cursor()

    #check if the username is in the database
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()    # fetches the tuple containing the encoded password of the user
    if user_data:
        # if found, check if the hash of the typed password is the same as the hash saved
        stored_password = user_data[0]
        if sha256(password.encode()).hexdigest() == stored_password:
            print("Login successful!")
            login_root.withdraw()
            # if everything correct, go to run_game_console
            run_game_console()

            print("it executed")
        else:
            # if not the same, give error "Wrong password"
            messagebox.showerror("Error", "Wrong password")


    # if username not found, show an error with a message "Username not found"
    else:
        messagebox.showerror("Error", "Username not found")
    # while logged_in == True:
    #     run_game_console()

    # close the connection
    conn.close()



def open_register_window():
    """
    Creates and displays the registration window for new users.

    :return: None
    """
    login_root.withdraw()
    # root2.deiconify()
    global register_root
    register_root = customtkinter.CTkToplevel()
    register_root.geometry("500x400")

    # root2.protocol("WM_DELETE_WINDOW", quit_all_roots)

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

    :return: None
    """
    # connecting data to the database
    print("new user registered prototype")
    conn = sqlite3.connect('users_db.db')    # opening a connection with the database
    cursor = conn.cursor()

    #check if the username already exists
    cursor.execute('SELECT username FROM users WHERE username = ?;', (username,))

    if cursor.fetchone():
        #if yes give an error "Username already exists"
        messagebox.showerror("Error", "Username already exists")

    # check if the input is correct for the username (not too short/long)
    elif len(username) < 5 or len(username) > 15:
        messagebox.showerror("Register Error", "Username too short or too long")

    # check if the passwords match
    elif password != password_confirmation:
        messagebox.showerror("Error", "Passwords do not match")

    else:
        # create a hash for the password
        hashed_password = sha256(password.encode()).hexdigest()
        #save the username and hash of password in the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        #go to run_game_console
        register_root.withdraw()
        run_game_console()

    # close the connection
    conn.close()


open_start_page()



