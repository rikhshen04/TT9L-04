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

    def create_register_frame(self):
        tk.Label(self.register_frame, text="Register", font=('Helvetica', 20), bg="#f0f0f0").pack(pady=10)
        tk.Label(self.register_frame, text="Username", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.register_username_entry = tk.Entry(self.register_frame, font=self.large_font, width=20)
        self.register_username_entry.pack(pady=5)
        tk.Label(self.register_frame, text="Password", font=self.large_font, bg="#f0f0f0").pack(pady=5)
        self.register_password_entry = tk.Entry(self.register_frame, show='*', font=self.large_font, width=20)
        self.register_password_entry.pack(pady=5)
        tk.Button(self.register_frame, text="Register", font=self.large_font, command=self.register, width=15, height=2, bg="#007bff", fg="white").pack(pady=10)
        tk.Button(self.register_frame, text="Back to Login", font=self.large_font, command=self.show_login_page, width=15, height=2, bg="#6c757d", fg="white").pack(pady=5)

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if not username or not password:  
            messagebox.showerror("Login Failed", "Check Username and Password")
            return

        with open(self.database_file, "r") as file:
            for line in file:
                a, b = line.strip().split(",")
                if a == username and b == password:
                    messagebox.showinfo("Login", "Login successful!")
                    self.login_frame.pack_forget()
                    self.open_dashboard()
                    return

        messagebox.showerror("Login Failed", "Incorrect Username or Password")

    def register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()

        if not username or not password:  
            messagebox.showerror("Register Failed", "Username and Password cannot be empty")
            return

        with open(self.database_file, "r") as file:
            for line in file:
                a, b = line.strip().split(",")
                if a == username:
                    messagebox.showerror("Register Failed", "Username already exists")
                    return

        with open(self.database_file, "a") as file:
            file.write(f"{username},{password}\n")
        messagebox.showinfo("Register", "You have been registered!")
        self.show_login_page()

    def show_login_page(self):
        self.register_frame.pack_forget()
        self.login_frame.pack()
        self.login_username_entry.delete(0, tk.END)
        self.login_password_entry.delete(0, tk.END)

    def show_register_page(self):
        self.login_frame.pack_forget()
        self.register_frame.pack()
        self.register_username_entry.delete(0, tk.END)
        self.register_password_entry.delete(0, tk.END)

    def open_dashboard(self):
        self.dashboard = Dashboard(self.root)
        self.dashboard.pack(fill="both", expand=True)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()