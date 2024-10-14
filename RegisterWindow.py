import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

#Creating a root window
root2 = customtkinter.CTk()
root2.geometry("500x400")

def register():
    #here we can implement the login function
    #connecting data to the database
    print("new user registered prototype")


#This is a frame for the login window, I can later change the size
frame = customtkinter.CTkFrame(master=root2)
frame.pack(pady=20, padx=60, fill="both", expand=True)


# adding additional elements to the frame, so the login window

# Adding a text at the top that says "Login to the game"
label = customtkinter.CTkLabel(master=frame, text="Register in the system to later access your statistics", font=("Roboto", 15))
label.pack(pady=12, padx=10)

#Adding username and password entries
#Setting username
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
#Setting password
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*") #Encoding the password so it doesn't show it, instead star symbols
entry2.pack(pady=12, padx=10)
#Confirming password
entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Confirm password", show="*") #Encoding the password so it doesn't show it, instead star symbols
entry3.pack(pady=12, padx=10)

#designing the login button
button = customtkinter.CTkButton(master=frame, text="Register", command=register()) #command connects it to the function login that we will later implement
button.pack(pady=12, padx=10)

