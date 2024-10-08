import customtkinter
import tkinter as tk
from tkinter import PhotoImage

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

def open_login_window():
    root.destroy()

    # Creating a root window for login
    login_root = customtkinter.CTk()
    login_root.geometry("500x350")
    login_root.title('Login to the game')

    def login():
        print("login prototype")

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

    login_root.mainloop()


# Create the main window (Start page)
root = customtkinter.CTk()
root.geometry('800x600')
root.title("Game Enter Page")

# Create a frame to organize the logo and the button
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Load the logo image using tkinter's PhotoImage
logo = PhotoImage(file="logo.png")  # Ensure the path to the image is correct

# Create a label for the logo image
label_logo = customtkinter.CTkLabel(master=frame, image=logo, text="")  # Show the image without text
label_logo.image = logo  # Keep a reference to avoid garbage collection
label_logo.pack(pady=20)  # Add some padding around the image

# Create a Start button that opens the login window
start_button = customtkinter.CTkButton(master=frame, text="Start", font=("Roboto", 24), command=open_login_window)
start_button.pack(pady=20)  # Add padding to separate the button from the image


root.mainloop()

















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
# root.mainloop() #calling the function