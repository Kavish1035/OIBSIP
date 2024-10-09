import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


# Function to generate password
def generate_password():
    length = password_length.get()
    include_upper = upper_case_var.get()
    include_numbers = number_var.get()
    include_special = special_char_var.get()

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4.")
        return

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "!@#$%^&*()-_+="

    all_characters = lower
    if include_upper:
        all_characters += upper
    if include_numbers:
        all_characters += numbers
    if include_special:
        all_characters += special

    if not all_characters:
        messagebox.showerror("Error", "No characters selected for password generation.")
        return

    password = ''.join(random.choice(all_characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Function to copy password to clipboard
def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")


# Tkinter GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("600x600")

# Labels and Inputs
tk.Label(root, text="Password Length:").pack(pady=10)
password_length = tk.IntVar(value=12)
tk.Spinbox(root, from_=4, to_=64, textvariable=password_length).pack()

# Checkboxes for complexity options
upper_case_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_case_var).pack()
number_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=number_var).pack()
special_char_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_char_var).pack()

# Entry to display generated password
password_entry = tk.Entry(root, width=30, font=("Arial", 12))
password_entry.pack(pady=20)

# Buttons for generate and copy
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_password).pack()

# Main loop
root.mainloop()
