import tkinter as tk
from tkinter import messagebox
import os
from dashboard import Dashboard

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker App")
        self.root.geometry("500x400")

        self.large_font = ('Helvetica', 16)

        self.database_file = "logindatabase.txt"
        if not os.path.exists(self.database_file):
            with open(self.database_file, "w") as file:
                file.write("")