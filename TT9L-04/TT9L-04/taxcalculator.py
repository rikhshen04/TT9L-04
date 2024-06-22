import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

# Create the main application window
root = tk.Tk()
root.title("Tax Calculator")
root.geometry("900x700")

# Enable resizing
root.resizable(True, True)

# Styles
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#1f77b4", foreground="#ffffff")
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("Treeview", font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# Tax brackets
tax_brackets = [
    (0, 10000, 0.1),    # 10% for income up to $10,000
    (10000, 30000, 0.15),  # 15% for income between $10,000 and $30,000
    (30000, 100000, 0.2),  # 20% for income between $30,000 and $100,000
    (100000, float('inf'), 0.25)  # 25% for income above $100,000
]

# Frames
frame_input = ttk.Frame(root, padding="10 10 10 10")
frame_input.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
frame_result = ttk.Frame(root, padding="10 10 10 10")
frame_result.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
frame_chart = ttk.Frame(root, padding="10 10 10 10")
frame_chart.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

# Configure grid weights for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
frame_result.grid_rowconfigure(0, weight=1)
frame_result.grid_columnconfigure(0, weight=1)
frame_chart.grid_rowconfigure(0, weight=1)
frame_chart.grid_columnconfigure(0, weight=1)

# Input fields
ttk.Label(frame_input, text="Annual Income:").grid(row=0, column=0, sticky="w")
income_entry = ttk.Entry(frame_input)
income_entry.grid(row=0, column=1)

ttk.Label(frame_input, text="Deductions:").grid(row=1, column=0, sticky="w")
deductions_entry = ttk.Entry(frame_input)
deductions_entry.grid(row=1, column=1)

ttk.Label(frame_input, text="Tax Credits:").grid(row=2, column=0, sticky="w")
credits_entry = ttk.Entry(frame_input)
credits_entry.grid(row=2, column=1)

ttk.Label(frame_input, text="Previous Year Tax:").grid(row=3, column=0, sticky="w")
previous_tax_entry = ttk.Entry(frame_input)
previous_tax_entry.grid(row=3, column=1)