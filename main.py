import tkinter as tk
from tkinter import messagebox
from wsgiref.util import guess_scheme

import ttkbootstrap as ttk
import random
from PIL import Image, ImageTk

root = ttk.Window(themename="pydata-dark")
root.geometry("900x500+800+300")
root.title("random game project ")
root.resizable(False, False)


def login():
    user = entry_username.get()
    passw = entry_password.get()
    if user == "admin" or passw == "admin":
        open_game_page()
    else:
        messagebox.showinfo("Error", "username or password incorrect!")


def open_game_page():
    root.withdraw()
    root_page2 = ttk.Toplevel(root)
    root_page2.geometry("600x500")
    root_page2.title("Game Page")
    root_page2.resizable(False, False)

    l_p2_title = ttk.Label(root_page2, text="Guess The Number", font="arial 12 bold", bootstyle="secondary")
    l_p2_title.pack(pady=10)

    l_p2_helper = ttk.Label(root_page2, text="the number between 1 and 3", font=(" calibri ", "9"), bootstyle="info")
    l_p2_helper.pack(pady=11)

    e_p2_input = ttk.Entry(root_page2, bootstyle="info", width=5)
    e_p2_input.pack(pady=15)

    var_random = random.randint(1, 3)
    var_counter = ttk.IntVar(value=0)

    l_p2_result = ttk.Label(root_page2, text="", bootstyle="danger" , font = "calibri 12 bold")
    l_p2_result.pack(pady=27)

    def check_game():
        try:
            guess = int(e_p2_input.get())
        except ValueError:
            l_p2_result.config(
                text="please enter a number! >.< ",
                bootstyle="danger")
            return
        var_counter.set(var_counter.get() + 1)

        if guess < var_random:
            l_p2_result.config(text="guessed less than random number :( ", bootstyle="danger")

        elif guess > var_random:
            l_p2_result.config(text=" guessed grade than random number :( ", bootstyle="danger")
        else:
            messagebox.showinfo("result", f' you win and guessed the correct number *,* {var_counter.get()}')

            root_page2.destroy()
            root.deiconify()

    b1_p2 = ttk.Button(root_page2, text="Check", bootstyle="success-outline", width=15, command=check_game)
    b1_p2.pack(pady=35)

    b2_p2 = ttk.Button(root_page2, text="Exit", bootstyle="warning-outline", width=15 , command=lambda: [root_page2.destroy(), root.deiconify()])
    b2_p2.pack(pady=31)

    root_page2.mainloop()


l_frame = ttk.Frame(root)
l_frame.place(x=0, y=0, width=450, height=500)

try:
    image = Image.open("image1.jpeg").resize((200, 200))
except:
    image = Image.new("RGB", (250, 250), "#222")
photo = ImageTk.PhotoImage(image)
l_image = tk.Label(l_frame, image=photo)
l_image.place(relx=0.5, rely=0.5, anchor="center")

r_frame = ttk.Frame(root)
r_frame.place(x=450, y=0, width=450, height=500)

l_welcome = ttk.Label(r_frame, text="Welcome to game", font=("Times New Roman", "20", "bold"), bootstyle="info")
l_welcome.place(x=220, y=40, anchor="center")

l_help = ttk.Label(r_frame, text="please sign in", font=("calibri", "14", "bold"), bootstyle="light")
l_help.place(x=155, y=115, anchor="center")

l_username = ttk.Label(r_frame, text="username: ", font=("calibri", "12"), bootstyle="light")
l_username.place(x=135, y=180, anchor="center")

l_password = ttk.Label(r_frame, text=" password:  ", font=("calibri", "12"), bootstyle="light")
l_password.place(x=135, y=230, anchor="center")

entry_username = ttk.Entry(r_frame, bootstyle="info")
entry_username.place(x=310, y=180, anchor="center")

entry_password = ttk.Entry(r_frame, bootstyle="info", show="*")
entry_password.place(x=310, y=230, anchor="center")

b_login = ttk.Button(r_frame, text="login", bootstyle="success-outline", width=10, command=login)
b_login.place(x=240, y=270)

l_passwordrecovery = ttk.Label(r_frame, text=" forgot password? ", font=("calibri", "8", "underline"),
                               bootstyle="warning", cursor="hand2")
l_passwordrecovery.place(x=247, y=320)

root.mainloop()





