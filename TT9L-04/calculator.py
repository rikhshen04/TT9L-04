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

    def calculate_budget(self):
        try:
            salary = float(self.entries["salary"].get())
            self.expenses = {key: float(entry.get() or 0) for key, entry in self.entries.items() if key != "salary"}

            self.total_expenses = sum(self.expenses.values())
            self.remaining_salary = salary - self.total_expenses

            self.result_label.config(text=f"Total Expenses: RM{self.total_expenses:.2f}\nRemaining Salary: RM{self.remaining_salary:.2f}")

            self.create_pie_chart(self.expenses)

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def create_pie_chart(self, expenses):
        labels, sizes = zip(*expenses.items())
        fig, ax = plt.subplots()

        # Plot pie chart with automatic percentage labels and avoiding overlap
        wedges, texts, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct=lambda pct: f"{pct:.1f}%\n" if pct > 5 else "",
            startangle=140,
            colors=plt.cm.Paired(range(len(expenses)))
        )

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        ax.set_title("Expense Distribution", fontsize=14)

        # Beautify the pie chart text
        plt.setp(texts, size=10, weight="bold")
        plt.setp(autotexts, size=8, weight="bold", color="white")

        # Clear existing widgets in chart_frame if any
        if self.chart_frame.winfo_children():
            for widget in self.chart_frame.winfo_children():
                widget.destroy()

        # Create and draw new chart
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def download_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            try:
                self.create_pdf(file_path)
                messagebox.showinfo("Success", "PDF report generated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not create PDF: {e}")

    def create_pdf(self, file_path):
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica", 14)
        c.drawString(30, height - 30, "Budget Calculator Report")
        
        c.setFont("Helvetica", 12)
        c.drawString(30, height - 60, f"Monthly Salary: RM{self.entries['salary'].get()}")

        y = height - 90
        for label_text, var_name in self.input_fields:
            if var_name != "salary":
                c.drawString(30, y, f"{label_text} {self.entries[var_name].get()}")
                y -= 20

        c.drawString(30, y, f"Total Expenses: RM{self.total_expenses:.2f}")
        y -= 20
        c.drawString(30, y, f"Remaining Salary: RM{self.remaining_salary:.2f}")

        c.save()
