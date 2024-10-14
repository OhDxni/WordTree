import customtkinter
from RegisterWindow import *

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

#Creating a root window
root = customtkinter.CTk()
root.geometry("500x400")

def login():
    #here we can implement the login function
    #connecting data to the database
    print("login prototype")

def registerWindow():
    root.destroy()
    root2.mainloop()

#This is a frame for the login window, I can later change the size
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


# adding additional elements to the frame, so the login window

# Adding a text at the top that says "Login to the game"
label = customtkinter.CTkLabel(master=frame, text="Login to the game", font=("Roboto", 24))
label.pack(pady=12, padx=10)

#Adding username and password entries
#Setting username
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
#Setting password
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*") #Encoding the password so it doesn't show it, instead star symbols
entry2.pack(pady=12, padx=10)

#designing the login button
button = customtkinter.CTkButton(master=frame, text="Login", command=login) #command connects it to the function login that we will later implement
button.pack(pady=12, padx=10)

#designing the "Remember me" check box
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

#label asking the user if they do not have an account yet
label = customtkinter.CTkLabel(master=frame, text="Do you not have an account yet? Then register below:", font=("Roboto", 12))
label.pack(pady=12, padx=10)

#button redirecting the user tothe register window
button = customtkinter.CTkButton(master=frame, text="Register here", command=registerWindow)
button.pack(pady=0, padx=10)

root.mainloop() #calling the function