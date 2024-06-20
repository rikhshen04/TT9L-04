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