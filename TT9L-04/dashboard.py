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