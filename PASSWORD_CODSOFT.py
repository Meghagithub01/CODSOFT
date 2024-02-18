import tkinter as tk
import random
from tkinter import *

root = Tk()
root.title("Password Generator")
root.geometry("550x550")
root.resizable(False, False)
root.configure(background="#FAF9F6")
#Title
Title= Label(root, text="Password Generator", fg="black", bg="white", font=('Times New Roman', 20, "bold", 'underline'))
Title.pack(anchor="center", pady=20)

#Username
username = Label(root, text="Enter Username:", fg="white", bg="black", font=('Times New Roman',14))
username.place(x=30, y=100)

username_entry = Entry(root, font=('Times New Roman', 12))
username_entry.place(y=100, x=210)
username_entry.pack

3  #Password
length_password = Label(root, text="Enter Password Length:", fg="white", bg="black", font=('Times New Roman',14))
length_password.place(x=30, y=150)

generated_password = Label(root, text="Generated Password:", fg="white", bg="black", font=('Times New Roman',14))
generated_password.place(x=30, y=200)

character_entry = Entry(root, font=('Times New Roman', 12))
character_entry.pack(pady=77, padx=210)

label_password = Label(root, width=20, font=('Times New Roman', 15))
label_password.place(x=210, y=200)

alphabets = 'abcdefghijklmnoopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_-+='
characters = alphabets + numbers +symbols

def generate_password():
    length = character_entry.get()
    password = "".join(random.sample(characters,int(length)))
    label_password.config(text=''+ password)

Button(root, text="Generate Password", command=generate_password, width=16, height=1, font=("arial", 14, "bold")).place(x=165, y=290)

root.mainloop()