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
