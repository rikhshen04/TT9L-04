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
