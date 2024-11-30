import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# Initialize main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("800x600")
root.configure(bg="#f0f0f0")  # Light gray background for a better look

# Global Variables
expenses = []
monthly_budget = 500  # Default budget value
categories = ["Groceries", "Rent", "Utilities", "Entertainment", "Transportation"]
recurring_var = tk.BooleanVar()
dark_mode = tk.BooleanVar()

# Function to validate date format (DD-MM-YYYY)
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# Function to add expense
def add_expense():
    date = date_entry.get()
    if not validate_date(date):
        messagebox.showwarning("Invalid Date", "Please enter a valid date in DD-MM-YYYY format.")
        return
    
    category = category_combobox.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Amount", "Please enter a valid amount.")
        return
    
    notes = notes_entry.get()
    recurring = recurring_var.get()

    expense = {"Date": date, "Category": category, "Amount": amount, "Notes": notes, "Recurring": recurring}
    expenses.append(expense)
    update_expense_list()
    check_budget()

    messagebox.showinfo("Expense Added", f"Expense added: {amount} in {category} on {date}")

# Function to update expense list
def update_expense_list():
    listbox.delete(0, tk.END)
    for expense in expenses:
        listbox.insert(tk.END, f"{expense['Date']} - {expense['Category']} - ${expense['Amount']}")

# Function to export expenses to CSV
def export_to_csv():
    if not expenses:
        messagebox.showwarning("No Data", "No expenses to export!")
        return

    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Notes", "Recurring"])
        for expense in expenses:
            writer.writerow([expense["Date"], expense["Category"], expense["Amount"], expense["Notes"], expense["Recurring"]])
    
    messagebox.showinfo("Export", "Data has been exported to expenses.csv")

# Function to check budget
def check_budget():
    total_expense = sum(expense["Amount"] for expense in expenses)
    if total_expense > monthly_budget:
        messagebox.showwarning("Budget Exceeded", "You have exceeded your monthly budget!")
    else:
        messagebox.showinfo("Budget Status", f"You are within the budget. Total: ${total_expense:.2f}")

# Function to toggle theme
def toggle_theme():
    if dark_mode.get():
        root.config(bg="black")
        dark_mode.set(False)
    else:
        root.config(bg="#f0f0f0")
        dark_mode.set(True)

# Function to set budget
def set_budget():
    global monthly_budget
    try:
        new_budget = float(budget_entry.get())
        monthly_budget = new_budget
        messagebox.showinfo("Budget Updated", f"Monthly budget updated to: ${new_budget}")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number for the budget.")

# UI Styling
label_font = ("Arial", 12)
button_font = ("Arial", 10, "bold")
entry_font = ("Arial", 11)

# UI Components
# Row 0: Date Entry
date_label = tk.Label(root, text="Date (DD-MM-YYYY):", font=label_font, bg="#f0f0f0")
date_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
date_entry = tk.Entry(root, font=entry_font)
date_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Row 1: Category Combobox
category_label = tk.Label(root, text="Category:", font=label_font, bg="#f0f0f0")
category_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
category_combobox = ttk.Combobox(root, values=categories, font=entry_font)
category_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Row 2: Amount Entry
amount_label = tk.Label(root, text="Amount:", font=label_font, bg="#f0f0f0")
amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
amount_entry = tk.Entry(root, font=entry_font)
amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Row 3: Notes Entry
notes_label = tk.Label(root, text="Notes:", font=label_font, bg="#f0f0f0")
notes_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
notes_entry = tk.Entry(root, font=entry_font)
notes_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Row 4: Recurring Checkbox
recurring_checkbox = tk.Checkbutton(root, text="Mark as Recurring", variable=recurring_var, font=label_font, bg="#f0f0f0")
recurring_checkbox.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Row 5: Buttons in a Row
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=5, column=0, columnspan=2, pady=10)

add_button = tk.Button(button_frame, text="Add Expense", font=button_font, command=add_expense)
add_button.grid(row=0, column=0, padx=5)

export_button = tk.Button(button_frame, text="Export Data", font=button_font, command=export_to_csv)
export_button.grid(row=0, column=1, padx=5)

budget_button = tk.Button(button_frame, text="Set Budget", font=button_font, command=set_budget)
budget_button.grid(row=0, column=2, padx=5)

theme_button = tk.Button(button_frame, text="Toggle Theme", font=button_font, command=toggle_theme)
theme_button.grid(row=0, column=3, padx=5)

# Row 6: Expense Listbox
listbox_label = tk.Label(root, text="Expenses List:", font=label_font, bg="#f0f0f0")
listbox_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
listbox = tk.Listbox(root, width=50, height=10, font=entry_font)
listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Row 8: Budget Input
budget_label = tk.Label(root, text="Set Monthly Budget:", font=label_font, bg="#f0f0f0")
budget_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")
budget_entry = tk.Entry(root, font=entry_font)
budget_entry.grid(row=8, column=1, padx=10, pady=10, sticky="w")

# Run the application
root.mainloop()
