import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("system-green")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("login prototype")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, test="Login to the game", text_fo)