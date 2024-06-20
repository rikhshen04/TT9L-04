import tkinter as tk
from calculator import BudgetCalculator
from bill_manager import BillManagerApp
from loan_calculator import LoanCalculator

class Dashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.master.title("Dashboard")
        self.master.geometry("400x300")

        tk.Label(self, text="Welcome to the Menu!").pack(pady=20)

        tk.Button(self, text="Open Calculator", command=self.open_calculator).pack(pady=10)
        tk.Button(self, text="Open Bill Manager", command=self.open_bill_manager).pack(pady=10)
        tk.Button(self, text="Open Loan Calculator", command=self.open_loan_calculator).pack(pady=10)
        tk.Button(self, text="Logout", command=self.logout).pack(pady=10)