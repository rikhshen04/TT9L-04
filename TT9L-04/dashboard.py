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

    def open_calculator(self):
        calculator_window = tk.Toplevel(self.master)
        calculator_window.title("Calculator")
        calculator_window.geometry("400x600")
        budget_calculator = BudgetCalculator(calculator_window)

    def open_bill_manager(self):
        bill_manager_window = tk.Toplevel(self.master)
        bill_manager_window.title("Bill Manager")
        bill_manager_window.geometry("600x400")
        bill_manager_app = BillManagerApp(bill_manager_window)

    def open_loan_calculator(self):
        loan_calculator_window = tk.Toplevel(self.master)
        loan_calculator_window.title("Loan Calculator")
        loan_calculator_window.geometry("500x500")
        loan_calculator_app = LoanCalculator(loan_calculator_window)
