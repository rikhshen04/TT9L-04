# loan_calculator.py
import tkinter as tk
from tkinter import ttk

class LoanCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculate Loan Interest")
        self.master.geometry("500x500")
        self.master.configure(bg='#2e2e2e')

        self.create_widgets()
