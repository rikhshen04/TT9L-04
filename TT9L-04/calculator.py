import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pytesseract
from PIL import Image
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class BudgetCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Calculator")
        self.root.geometry("600x800")

        self.setup_styles()
        self.create_widgets()
        self.pack_widgets()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#f8f9fa', foreground='#495057', font=('Arial', 12))
        self.style.configure('TButton', background='#007bff', foreground='white', font=('Arial', 12), padding=10)
        self.style.configure('TEntry', fieldbackground='#fff', font=('Arial', 12))