import customtkinter
import tkinter as tk
from tkinter import PhotoImage
# from game_console import *
# from RegisterWindow import open_register_window


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

logo_image = None

# Function to open the start page
def open_start_page():
    # Create the main window (Start page)
    global root, logo_image
    root = customtkinter.CTk()
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
    root.destroy()  # Close the start window

    # Create a new root window for login
    login_root = customtkinter.CTkToplevel()
    # login_root = customtkinter.CTk()
    login_root.geometry("500x600")
    login_root.title('Login to the game')

    def login():
        print("login prototype")

    def register_window():
        login_root.destroy()
        open_register_window()

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
    button = customtkinter.CTkButton(master=frame, text="Register here", command=register_window)
    button.pack(pady=0, padx=10)


    # "Go Back" button to go back to the start page
    back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=lambda: go_back_to_start_page(login_root))
    # back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=go_back(login_root, open_start_page()))
    back_button.pack(pady=12, padx=10)

    login_root.mainloop()  # Starting the login window loop





def open_register_window():
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("green")

    # Creating a root window
    root2 = customtkinter.CTk()
    root2.geometry("500x400")

    def register():
        # here we can implement the login function
        # connecting data to the database
        print("new user registered prototype")

    # print("Register window opened")
    #This is a frame for the login window, I can later change the size
    frame2 = customtkinter.CTkFrame(master=root2)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)


    # adding additional elements to the frame, so the login window

    # Adding a text at the top that says "Login to the game"
    label = customtkinter.CTkLabel(master=frame2, text="Register in the system to later access your statistics", font=("Roboto", 15))
    label.pack(pady=12, padx=10)

    #Adding username and password entries
    #Setting username
    entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)
    #Setting password
    entry2 = customtkinter.CTkEntry(master=frame2, placeholder_text="Password", show="*") #Encoding the password so it doesn't show it, instead star symbols
    entry2.pack(pady=12, padx=10)
    #Confirming password
    entry3 = customtkinter.CTkEntry(master=frame2, placeholder_text="Confirm password", show="*") #Encoding the password so it doesn't show it, instead star symbols
    entry3.pack(pady=12, padx=10)

    #designing the login button
    button = customtkinter.CTkButton(master=frame2, text="Register", command=register) #command connects it to the function login that we will later implement
    button.pack(pady=12, padx=10)

    root2.mainloop()

# Function to go back to the start page

# def go_back(origin_root, destination):
#     origin_root.destroy()
#     destination()

def go_back_to_start_page(login_root):
    login_root.destroy()  # Close the login window
    open_start_page()     # Reopen the start page



open_start_page()


















# import customtkinter
#
# customtkinter.set_appearance_mode("system")
# customtkinter.set_default_color_theme("green")
#
# #Creating a root window
# root = customtkinter.CTk()
# root.geometry("500x350")
#
# def login():
#     #here we can implement the login function
#     #connecting data to the database
#     print("login prototype")
#
# #This is a frame for the login window, I can later change the size
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)
#
#
# # adding additional elements to the frame, so the login window
#
# # Adding a text at the top that says "Login to the game"
# label = customtkinter.CTkLabel(master=frame, text="Login to the game", font=("Roboto", 24))
# label.pack(pady=12, padx=10)
#
# #Adding username and password entries
# #Setting username
# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)
# #Setting password
# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*") #Encoding the password so it doesn't show it, instead star symbols
# entry2.pack(pady=12, padx=10)
#
# #designing the login button
# button = customtkinter.CTkButton(master=frame, text="Login", command=login) #command connects it to the function login that we will later implement
# button.pack(pady=12, padx=10)
#
# #designing the "Remember me" check box
# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
# checkbox.pack(pady=12, padx=10)
#
#op root.mainloop() #calling the function