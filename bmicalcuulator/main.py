import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import csv
import os

# Path for saving user data
DATA_FILE = "bmi_data.csv"

# Function to calculate BMI and store the result
def calculate_bmi():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if name and height > 0 and weight > 0:
            bmi = weight / (height ** 2)
            bmi_result_label.config(text=f"Your BMI: {bmi:.2f}")
            category = categorize_bmi(bmi)
            bmi_category_label.config(text=f"Category: {category}")
            save_data(name, weight, height, bmi)
        else:
            messagebox.showerror("Input Error", "Name, height, and weight must be valid positive numbers.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Function to save data to a CSV file
def save_data(name, weight, height, bmi):
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, weight, height, bmi])
    messagebox.showinfo("Success", f"BMI data for {name} has been saved.")

# Function to load historical data from the CSV file
def load_data():
    if not os.path.exists(DATA_FILE):
        messagebox.showinfo("No Data", "No data available yet.")
        return []

    data = []
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Function to display historical BMI records for a user
def view_history():
    user_name = name_entry.get().strip()
    if not user_name:
        messagebox.showerror("Input Error", "Please enter a name to view history.")
        return

    data = load_data()
    user_data = [row for row in data if row[0] == user_name]

    if user_data:
        history_window = tk.Toplevel(root)
        history_window.title(f"{user_name}'s BMI History")

        tree = ttk.Treeview(history_window, columns=("Weight", "Height", "BMI"), show="headings")
        tree.heading("Weight", text="Weight (kg)")
        tree.heading("Height", text="Height (m)")
        tree.heading("BMI", text="BMI")

        for row in user_data:
            tree.insert("", tk.END, values=row[1:])

        tree.pack(fill="both", expand=True)
    else:
        messagebox.showinfo("No Data", f"No data found for {user_name}.")

# Function to plot BMI trend for a user
def plot_bmi_trend():
    user_name = name_entry.get().strip()
    if not user_name:
        messagebox.showerror("Input Error", "Please enter a name to view trend.")
        return

    data = load_data()
    user_data = [row for row in data if row[0] == user_name]

    if user_data:
        bmis = [float(row[3]) for row in user_data]
        timestamps = list(range(1, len(bmis) + 1))

        plt.figure()
        plt.plot(timestamps, bmis, marker='o', linestyle='-', color='b')
        plt.title(f"{user_name}'s BMI Trend")
        plt.xlabel("Record Number")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("No Data", f"No data found for {user_name}.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator with User Data Storage")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Style Configuration
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10, "bold"), padding=10)
style.configure("TLabel", font=("Helvetica", 10), padding=5)
style.configure("TEntry", padding=5)

# Labels and Entry fields
name_label = ttk.Label(root, text="Enter Name:")
name_label.pack(pady=5)

name_entry = ttk.Entry(root, width=30)
name_entry.pack(pady=5)

weight_label = ttk.Label(root, text="Enter Weight (kg):")
weight_label.pack(pady=5)

weight_entry = ttk.Entry(root, width=30)
weight_entry.pack(pady=5)

height_label = ttk.Label(root, text="Enter Height (m):")
height_label.pack(pady=5)

height_entry = ttk.Entry(root, width=30)
height_entry.pack(pady=5)

# Calculate Button with style
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Labels to display BMI result and category
bmi_result_label = ttk.Label(root, text="Your BMI:")
bmi_result_label.pack(pady=5)

bmi_category_label = ttk.Label(root, text="Category:")
bmi_category_label.pack(pady=5)

# Buttons for viewing history and plotting trends with style
view_history_button = ttk.Button(root, text="View History", command=view_history)
view_history_button.pack(pady=5)

view_trend_button = ttk.Button(root, text="View BMI Trend", command=plot_bmi_trend)
view_trend_button.pack(pady=5)

# Run the GUI
root.mainloop()
