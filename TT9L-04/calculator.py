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

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title_label = ttk.Label(self.scrollable_frame, text="Welcome to the Budget Calculator!", font=('Arial', 20))
        self.title_label.pack(pady=20)

        self.input_fields = [
            ("Monthly Salary (RM):", "salary"),
            ("House Loan (RM):", "house_loan"),
            ("Entertainment (RM):", "entertainment"),
            ("Car Loan (RM):", "car_loan"),
            ("Insurance (RM):", "insurance"),
            ("Utilities (RM):", "utilities"),
            ("Groceries (RM):", "groceries"),
            ("Savings (RM):", "savings"),
            ("Bills (RM):", "bills")
        ]

        self.entries = {}
        for label_text, var_name in self.input_fields:
            label = ttk.Label(self.scrollable_frame, text=label_text)
            label.pack(anchor='w', padx=10, pady=5)
            entry = ttk.Entry(self.scrollable_frame, style='TEntry')
            entry.pack(fill='x', padx=10, pady=5)
            self.entries[var_name] = entry

        self.receipt_button = ttk.Button(self.scrollable_frame, text="Upload Receipt", command=self.process_receipt, style='TButton')
        self.receipt_button.pack(pady=10)

        self.calculate_button = ttk.Button(self.scrollable_frame, text="Calculate", command=self.calculate_budget, style='TButton')
        self.calculate_button.pack(pady=10)

        self.result_label = ttk.Label(self.scrollable_frame, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)

        self.chart_frame = ttk.Frame(self.scrollable_frame)
        self.chart_frame.pack(pady=20, fill='both', expand=True)

        self.pdf_button = ttk.Button(self.scrollable_frame, text="Download PDF Report", command=self.download_pdf, style='TButton')
        self.pdf_button.pack(pady=10)

    def pack_widgets(self):
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def process_receipt(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            try:
                text = pytesseract.image_to_string(Image.open(file_path))
                self.extract_expense_data(text)
            except Exception as e:
                messagebox.showerror("Error", f"Could not process image: {e}")
            
    def extract_expense_data(self, text):
        lines = text.split('\n')
        amount = sum(float(match.group(1)) for line in lines if (match := re.search(r'RM(\d+\.\d{2})', line)))
        self.entries["groceries"].delete(0, tk.END)
        self.entries["groceries"].insert(0, str(amount))
        self.result_label.config(text=f"Extracted amount: RM{amount:.2f}")
