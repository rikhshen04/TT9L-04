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
