import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class BillManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Upcoming Bills and Payments")
        self.root.geometry("600x400")
        self.root.configure(bg="#e9ecef")