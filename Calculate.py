import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Core functionality
def calculate_age():
    try:
        birthdate = datetime.strptime(entry_birthdate.get(), "%d.%m.%Y")
        today = datetime.now()
        
        # Calculate years, months, and days
        age_years = relativedelta(today, birthdate).years
        age_months = relativedelta(today, birthdate).months
        age_days = relativedelta(today, birthdate).days

        # Calculate total days, hours, minutes, and seconds
        diff = today - birthdate
        total_days = diff.days
        total_hours = total_days * 24 + diff.seconds // 3600
        total_minutes = total_hours * 60 + (diff.seconds // 60) % 60
        total_seconds = total_minutes * 60 + diff.seconds % 60

        # Display results
        result.set(
            f"Years: {age_years} years\n"
            f"Months: {age_months} months\n"
            f"Days: {age_days} days\n\n"
            f"Total Days: {total_days:,}\n"
            f"Total Hours: {total_hours:,}\n"
            f"Total Minutes: {total_minutes:,}\n"
            f"Total Seconds: {total_seconds:,}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter the date in DD.MM.YYYY format.")

# Create GUI
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x400")
root.resizable(False, False)

# Input label and entry
label_birthdate = ttk.Label(root, text="Enter your birthdate (DD.MM.YYYY):")
label_birthdate.pack(pady=10)

entry_birthdate = ttk.Entry(root, font=("Arial", 14))
entry_birthdate.pack(pady=10)

# Button to calculate
btn_calculate = ttk.Button(root, text="Calculate Age", command=calculate_age)
btn_calculate.pack(pady=10)

# Result display
result = tk.StringVar()
label_result = ttk.Label(root, textvariable=result, font=("Arial", 12), anchor="center", justify="left")
label_result.pack(pady=20)

# Run the application
root.mainloop()
