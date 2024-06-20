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

        # Principal input
        principal_label = ttk.Label(container, text="Principal Amount (RM):")
        principal_label.grid(row=1, column=0, sticky=tk.W)
        self.principal_value_label = ttk.Label(container, text="50000")
        self.principal_value_label.grid(row=1, column=1, sticky=tk.E)
        self.principal_scale = ttk.Scale(container, from_=1000, to=100000, orient=tk.HORIZONTAL, command=lambda val: self.update_and_calculate(self.principal_scale, self.principal_value_label))
        self.principal_scale.set(50000)
        self.principal_scale.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Rate input
        rate_label = ttk.Label(container, text="Annual Interest Rate (%):")
        rate_label.grid(row=3, column=0, sticky=tk.W)
        self.rate_value_label = ttk.Label(container, text="5")
        self.rate_value_label.grid(row=3, column=1, sticky=tk.E)
        self.rate_scale = ttk.Scale(container, from_=1, to=20, orient=tk.HORIZONTAL, command=lambda val: self.update_and_calculate(self.rate_scale, self.rate_value_label))
        self.rate_scale.set(5)
        self.rate_scale.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

         # Years input
        years_label = ttk.Label(container, text="Loan Term (Years):")
        years_label.grid(row=5, column=0, sticky=tk.W)
        self.years_value_label = ttk.Label(container, text="15")
        self.years_value_label.grid(row=5, column=1, sticky=tk.E)
        self.years_scale = ttk.Scale(container, from_=1, to=30, orient=tk.HORIZONTAL, command=lambda val: self.update_and_calculate(self.years_scale, self.years_value_label))
        self.years_scale.set(15)
        self.years_scale.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))

        # Calculate button
        calculate_button = ttk.Button(container, text="Calculate", command=self.calculate_interest, style='TButton')
        calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

        # Result label
        self.result_label = ttk.Label(container, text="Total Monthly Payment: RM0.00", font=('Arial', 14))
        self.result_label.grid(row=8, column=0, columnspan=2, pady=10)

