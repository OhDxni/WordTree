import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

def create_root2():
    global root2
    root2 = customtkinter.CTkToplevel()
    root2.geometry("500x400")
    root2.withdraw()

def register():
    #here we can implement the login function
    #connecting data to the database
    print("new user registered prototype")


def open_register_window():
    root2.deiconify()

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

    # "Go Back" button to go back to the login page
    back_button = customtkinter.CTkButton(master=frame2, text="Go Back",
                                          command=lambda: go_back_to_login_page(root2))
    # back_button = customtkinter.CTkButton(master=frame, text="Go Back", command=go_back(login_root, open_start_page()))
    back_button.pack(pady=12, padx=10)

    root2.mainloop()

def go_back_to_login_page(root2):
    root2.withdraw()  # Close the login window
    login_root.deiconify()  # Reopen the start page

# open_register_window()
