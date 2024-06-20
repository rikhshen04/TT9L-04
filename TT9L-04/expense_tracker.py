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

        self.style_widgets()  # Apply custom styles

        self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.create_login_frame()

        self.register_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.create_register_frame()

        self.login_frame.pack()

    def style_widgets(self):
        self.root.configure(bg="#343a40")  # Dark background for the root window
        self.root.option_add('*Font', 'Helvetica 12')  # Global font setting

    def create_login_frame(self):
        tk.Label(self.login_frame, text="Login", font=('Helvetica', 20), bg="#f0f0f0").pack(pady=10)
        tk.Label(self.login_frame, text="Username", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.login_username_entry = tk.Entry(self.login_frame, font=self.large_font, width=20)
        self.login_username_entry.pack(pady=5)
        tk.Label(self.login_frame, text="Password", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.login_password_entry = tk.Entry(self.login_frame, show='*', font=self.large_font, width=20)
        self.login_password_entry.pack(pady=5)
        tk.Button(self.login_frame, text="Login", font=self.large_font, command=self.login, width=15, height=2, bg="#28a745", fg="white").pack(pady=10)
        tk.Button(self.login_frame, text="Register", font=self.large_font, command=self.show_register_page, width=15, height=2, bg="#007bff", fg="white").pack(pady=5)