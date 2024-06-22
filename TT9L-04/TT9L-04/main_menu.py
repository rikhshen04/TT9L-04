import tkinter as tk
from tkinter import messagebox, simpledialog
import os
from calculator import BudgetCalculator
from bill_manager import BillManagerApp
from loan_calculator import LoanCalculator

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker App")
        self.root.geometry("600x500")