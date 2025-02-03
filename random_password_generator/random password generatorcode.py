import random
import tkinter as tk
from tkinter import messagebox


def generate_password():
    uppercase_letters = "ABCDEFGHIKJLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=`~\\|[]{};:,<.>/?"

    upper, lower, digits, special = upper_var.get(), lower_var.get(), digits_var.get(), special_var.get()
    
    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if digits:
        all += numbers
    if special:
        all += symbols

    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for length.")
        return

    if len(all) == 0:
        messagebox.showerror("Selection Error", "Please select at least one character type.")
        return
    
    if length <= 0:
        messagebox.showerror("Length Error", "Please enter a positive length for the password.")
        return
    
    password = "".join(random.sample(all, length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Symbols", variable=special_var).grid(row=4, column=0, columnspan=2, sticky="w")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=6, column=0, columnspan=2)

root.mainloop()
