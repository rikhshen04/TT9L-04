import tkinter as tk
from tkinter import messagebox, simpledialog
import os
from calculator import BudgetCalculator
from bill_manager import BillManagerApp
from loan_calculator import LoanCalculator

class Budgetcalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker App")
        self.root.geometry("600x500")

        self.large_font = ('Helvetica', 16)
        self.medium_font = ('Helvetica', 12)

        self.database_file = "logindatabase.txt"
        if not os.path.exists(self.database_file):
            with open(self.database_file, "w") as file:
                file.write("")

        self.style_widgets()  # Apply custom styles

        self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.create_login_frame()

        self.register_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.create_register_frame()

        self.dashboard_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.create_dashboard_frame()

        self.current_user = None  # To keep track of the logged-in user

        self.login_frame.pack()

        # List of money-saving tips
        self.saving_tips = [
            "Tip 1: Track your spending to identify areas where you can cut back.",
            "Tip 2: Create a budget and stick to it.",
            "Tip 3: Avoid impulse purchases by making a shopping list.",
            "Tip 4: Use cash instead of credit cards to limit overspending.",
            "Tip 5: Look for discounts and use coupons.",
            "Tip 6: Set savings goals and work towards them consistently.",
            "Tip 7: Cook at home instead of dining out.",
            "Tip 8: Cancel unused subscriptions and memberships.",
            "Tip 9: Buy generic brands instead of name brands.",
            "Tip 10: Save energy by turning off lights and electronics when not in use."
        ]

    def style_widgets(self):
        self.root.configure(bg="#343a40")  # Dark background for the root window
        self.root.option_add('*Font', 'Helvetica 12')  # Global font setting

    def create_login_frame(self):
        tk.Label(self.login_frame, text="Login", font=('Helvetica', 20), bg="#f0f0f0").pack(pady=10)
        tk.Label(self.login_frame, text="Username", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.login_username_entry = tk.Entry(self.login_frame, font=self.large_font, width=20)
        self.login_username_entry.pack(pady=5)
        tk.Label(self.login_frame, text="Password", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.login_password_entry = tk.Entry(self.login_frame, show='*', font=self.large_font, width=20)
        self.login_password_entry.pack(pady=5)
        tk.Button(self.login_frame, text="Login", font=self.large_font, command=self.login, width=15, height=2, bg="#28a745", fg="white").pack(pady=10)
        tk.Button(self.login_frame, text="Register", font=self.large_font, command=self.show_register_page, width=15, height=2, bg="#007bff", fg="white").pack(pady=5)

    def create_register_frame(self):
        tk.Label(self.register_frame, text="Register", font=('Helvetica', 20), bg="#f0f0f0").pack(pady=10)
        tk.Label(self.register_frame, text="Username", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.register_username_entry = tk.Entry(self.register_frame, font=self.large_font, width=20)
        self.register_username_entry.pack(pady=5)
        tk.Label(self.register_frame, text="Password", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.register_password_entry = tk.Entry(self.register_frame, show='*', font=self.large_font, width=20)
        self.register_password_entry.pack(pady=5)
        tk.Button(self.register_frame, text="Register", font=self.large_font, command=self.register, width=15, height=2, bg="#007bff", fg="white").pack(pady=10)
        tk.Button(self.register_frame, text="Back to Login", font=self.large_font, command=self.show_login_page, width=15, height=2, bg="#6c757d", fg="white").pack(pady=5)

    def create_dashboard_frame(self):
        tk.Label(self.dashboard_frame, text="Expense Tracker", font=('Helvetica', 20), bg="#f0f0f0").pack(pady=10)

        self.points_label = tk.Label(self.dashboard_frame, text="Points: 0", font=self.medium_font, bg="#f0f0f0")
        self.points_label.pack(anchor='ne', padx=10, pady=5)

        self.expense_listbox = tk.Listbox(self.dashboard_frame, font=self.medium_font, width=50, height=10)
        self.expense_listbox.pack(pady=10)

        self.expense_entry_frame = tk.Frame(self.dashboard_frame, bg="#f0f0f0")
        tk.Label(self.expense_entry_frame, text="Description", font=self.medium_font, bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.expense_description_entry = tk.Entry(self.expense_entry_frame, font=self.medium_font, width=20)
        self.expense_description_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.expense_entry_frame, text="Amount", font=self.medium_font, bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.expense_amount_entry = tk.Entry(self.expense_entry_frame, font=self.medium_font, width=20)
        self.expense_amount_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.expense_entry_frame, text="Add Expense", font=self.medium_font, command=self.add_expense, bg="#28a745", fg="white").grid(row=2, columnspan=2, pady=10)
        self.expense_entry_frame.pack(pady=10)

        self.buttons_frame = tk.Frame(self.dashboard_frame, bg="#f0f0f0")
        tk.Button(self.buttons_frame, text="Edit Expense", font=self.medium_font, command=self.edit_expense, bg="#ffc107", fg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Delete Expense", font=self.medium_font, command=self.delete_expense, bg="#dc3545", fg="white").grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="View All Expenses", font=self.medium_font, command=self.view_expenses, bg="#17a2b8", fg="white").grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Logout", font=self.medium_font, command=self.logout, bg="#6c757d", fg="white").grid(row=0, column=3, padx=5, pady=5)
        self.buttons_frame.pack(pady=10)

        self.tool_buttons_frame = tk.Frame(self.dashboard_frame, bg="#f0f0f0")
        tk.Button(self.tool_buttons_frame, text="Open Calculator", font=self.medium_font, command=self.open_calculator, bg="#007bff", fg="white").grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10)
        tk.Button(self.tool_buttons_frame, text="Open Bill Manager", font=self.medium_font, command=self.open_bill_manager, bg="#007bff", fg="white").grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=10)
        tk.Button(self.tool_buttons_frame, text="Open Loan Calculator", font=self.medium_font, command=self.open_loan_calculator, bg="#007bff", fg="white").grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=10)
        self.tool_buttons_frame.pack(pady=20)

    def open_calculator(self):
        calculator_window = tk.Toplevel(self.root)
        calculator_window.title("Calculator")
        calculator_window.geometry("400x600")
        budget_calculator = BudgetCalculator(calculator_window)

    def open_bill_manager(self):
        bill_manager_window = tk.Toplevel(self.root)
        bill_manager_window.title("Bill Manager")
        bill_manager_window.geometry("600x400")
        bill_manager_app = BillManagerApp(bill_manager_window)

    def open_loan_calculator(self):
        loan_calculator_window = tk.Toplevel(self.root)
        loan_calculator_window.title("Loan Calculator")
        loan_calculator_window.geometry("500x400")
        loan_calculator = LoanCalculator(loan_calculator_window)

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if not username or not password:
            messagebox.showerror("Login Failed", "Check Username and Password")
            return

        found = False
        with open(self.database_file, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            stored_username, stored_password, stored_points = line.strip().split(",")
            if username == stored_username and password == stored_password:
                found = True
                points = int(stored_points) + 1
                lines[i] = f"{username},{password},{points}\n"
                with open(self.database_file, "w") as file:
                    file.writelines(lines)
                self.points = points
                self.current_user = username  # Set the current user
                self.show_dashboard()
                break

        if not found:
            messagebox.showerror("Login Failed", "Check Username and Password")

    def register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()

        if not username or not password:
            messagebox.showerror("Register Failed", "Username and Password cannot be empty")
            return

        with open(self.database_file, "r") as file:
            for line in file:
                stored_username, _, _ = line.strip().split(",")
                if stored_username == username:
                    messagebox.showerror("Register Failed", "Username already exists")
                    return

        with open(self.database_file, "a") as file:
            file.write(f"{username},{password},0\n")
        messagebox.showinfo("Register", "You have been registered!")
        self.show_login_page()

    def show_login_page(self):
        self.register_frame.pack_forget()
        self.login_frame.pack()
        self.login_username_entry.delete(0, tk.END)
        self.login_password_entry.delete(0, tk.END)

    def show_register_page(self):
        self.login_frame.pack_forget()
        self.register_frame.pack()
        self.register_username_entry.delete(0, tk.END)
        self.register_password_entry.delete(0, tk.END)

    def show_dashboard(self):
        self.login_frame.pack_forget()
        self.dashboard_frame.pack()
        self.points_label.config(text=f"Points: {self.points}")

        if self.points % 5 == 0:
            # Display a different saving tip each time points are a multiple of 5
            tip_index = (self.points // 5 - 1) % len(self.saving_tips)
            saving_tip = self.saving_tips[tip_index]
            messagebox.showinfo("Congratulations!", f"You have reached {self.points} points! Keep up the great work!\n\nSaving Tip: {saving_tip}")

        self.view_expenses()  # Load user-specific expenses

    def add_expense(self):
        description = self.expense_description_entry.get()
        amount = self.expense_amount_entry.get()

        if not description or not amount:
            messagebox.showerror("Error", "Description and Amount cannot be empty")
            return

        # Use user-specific expense file
        expense_file = f"{self.current_user}_expenses.txt"

        with open(expense_file, "a") as file:
            file.write(f"{description},{amount}\n")
        messagebox.showinfo("Success", "Expense added successfully!")
        self.expense_description_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)
        self.view_expenses()