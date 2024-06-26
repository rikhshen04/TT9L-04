import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class BillManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Upcoming Bills and Payments")
        self.root.geometry("600x400")
        self.root.configure(bg="#e9ecef")

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="Upcoming Bills and Payments", font=('Arial', 24), bg="#e9ecef", fg="#343a40")
        self.title_label.pack(pady=20)

        # Bill Name
        self.bill_name_label = tk.Label(self.root, text="Bill Name:", font=('Arial', 12), bg="#e9ecef", fg="#495057")
        self.bill_name_label.pack()
        self.bill_name_entry = tk.Entry(self.root, font=('Arial', 12))
        self.bill_name_entry.pack(pady=5)

        # Due Date
        self.due_date_label = tk.Label(self.root, text="Due Date (YYYY-MM-DD):", font=('Arial', 12), bg="#e9ecef", fg="#495057")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(self.root, font=('Arial', 12))
        self.due_date_entry.pack(pady=5)

        # Add Bill Button
        self.add_bill_button = tk.Button(self.root, text="Add Bill", font=('Arial', 12), bg="#28a745", fg="white", command=self.add_bill)
        self.add_bill_button.pack(pady=10)

        # Bill List
        self.bill_list_frame = tk.Frame(self.root, bg="#e9ecef")
        self.bill_list_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        self.bill_list = tk.Listbox(self.bill_list_frame, font=('Arial', 12))
        self.bill_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.bill_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bill_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.bill_list.yview)

        self.bill_list.bind("<Double-Button-1>", self.mark_as_paid)

    def add_bill(self):
        bill_name = self.bill_name_entry.get()
        due_date = self.due_date_entry.get()

        # Validate inputs
        if not bill_name.strip() or not due_date.strip():
            messagebox.showerror("Error", "Please enter both bill name and due date.")
            return

        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please enter date as YYYY-MM-DD.")
            return

        current_date = datetime.now().date()
        if due_date_obj.date() < current_date:
            messagebox.showerror("Error", "Due date cannot be in the past.")
            return

        days_left = (due_date_obj.date() - current_date).days
        days_left_text = f"{days_left} day(s) left" if days_left > 0 else "Due today"

        # Add bill to list
        bill_info = f"{bill_name}: Due on {due_date} ({days_left_text})"
        self.bill_list.insert(tk.END, bill_info)

        # Clear input fields after adding the bill
        self.bill_name_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

    def mark_as_paid(self, event):
        selected_bill_index = self.bill_list.curselection()
        if selected_bill_index:
            current_text = self.bill_list.get(selected_bill_index)
            if "(Paid)" in current_text:
                new_text = current_text.replace(" (Paid)", "")
            else:
                new_text = current_text + " (Paid)"
            self.bill_list.delete(selected_bill_index)
            self.bill_list.insert(selected_bill_index, new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillManagerApp(root)
    root.mainloop()
