import os.path
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# Function for calculation of password
def low():
    entry.delete(0, END)
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")

# Function to generate the password
def generate():
    password1 = low()
    entry.insert(10, password1)

# Function to copy password to clipboard
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

# Check if the file exists and create it if not
def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

# Function to save new passwords
def appendNew():
    file = open("info.txt", 'a')
    userName = entry1.get()
    website = entry2.get()
    Random_password = entry.get()
    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + Random_password + "\n"
    web = "Website: " + website + "\n"
    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close()

# Function to read saved passwords
def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)

# Initialize the GUI
checkExistence()
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of the GUI
root.title("Python Password Manager")

# Labels and input fields
c_label = Label(root, text="Length")
c_label.grid(row=1)
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# Radio buttons for strength
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')

# Combo box for password length
combo = Combobox(root, textvariable=var1)
combo['values'] = tuple(range(8, 33))
combo.current(0)
combo.grid(column=1, row=1)

# Entry fields for username, website, and password
userName = Label(root, text="Enter username here")
userName.grid(row=2)
entry1 = Entry(root)
entry1.grid(row=2, column=1)

website = Label(root, text="Enter website address here")
website.grid(row=3)
entry2 = Entry(root)
entry2.grid(row=3, column=1)

Random_password = Label(root, text="Generated password")
Random_password.grid(row=4)
entry = Entry(root)
entry.grid(row=4, column=1)

# Save and Show buttons
save_button = Button(root, text="Save", command=appendNew)
save_button.grid(row=2, column=2)
show_button = Button(root, text="Show all passwords", command=readPasswords)
show_button.grid(row=2, column=3)

# Start the GUI loop
root.mainloop()