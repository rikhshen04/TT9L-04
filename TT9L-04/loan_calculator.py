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

    def create_widgets(self):
        # Create a container frame
        container = ttk.Frame(self.master, padding="30 30 30 30", style='Container.TFrame')
        container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Style configuration
        style = ttk.Style()
        style.configure('TLabel', background='#2e2e2e', foreground='white', font=('Arial', 12))
        style.configure('TScale', background='#2e2e2e')
        style.configure('TButton', background='#ff5722', foreground='white', font=('Arial', 12), padding=10)
        style.configure('Container.TFrame', background='#2e2e2e')

        # Title
        title_label = ttk.Label(container, text="Calculate Loan Interest", font=('Arial', 24))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

