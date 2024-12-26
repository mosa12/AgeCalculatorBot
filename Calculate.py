import customtkinter as ctk
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tkinter import messagebox

# Function to calculate age
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
        result_text = (
            f"Years: {age_years} years\n"
            f"Months: {age_months} months\n"
            f"Days: {age_days} days\n\n"
            f"Total Days: {total_days:,}\n"
            f"Total Hours: {total_hours:,}\n"
            f"Total Minutes: {total_minutes:,}\n"
            f"Total Seconds: {total_seconds:,}"
        )
        result_label.configure(text=result_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter the date in DD.MM.YYYY format.")

# Initialize customTkinter
ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create main application window
app = ctk.CTk()
app.title("Age Calculator")
app.geometry("550x600")
app.resizable(False, False)

# Colors
bg_color = "#1a1a2e"
frame_color = "#16213e"
button_color = "#0f3460"
text_color = "#e94560"
result_color = "#00adb5"

# Set window background
app.configure(bg=bg_color)

# Title label
title_label = ctk.CTkLabel(
    app, text="🌟 Age Calculator 🌟", font=ctk.CTkFont(size=28, weight="bold"), text_color=text_color
)
title_label.pack(pady=20)

# Input frame
input_frame = ctk.CTkFrame(app, corner_radius=15, fg_color=frame_color)
input_frame.pack(pady=20, padx=20, fill="x")

# Birthdate input
birthdate_label = ctk.CTkLabel(
    input_frame, text="Enter your birthdate (DD.MM.YYYY):", font=ctk.CTkFont(size=14), text_color="white"
)
birthdate_label.pack(pady=10)

entry_birthdate = ctk.CTkEntry(
    input_frame, placeholder_text="DD.MM.YYYY", font=ctk.CTkFont(size=14), text_color="white"
)
entry_birthdate.pack(pady=10, padx=20)

# Calculate button
calculate_button = ctk.CTkButton(
    app, text="💡 Calculate Age 💡", command=calculate_age, fg_color=button_color, hover_color=text_color
)
calculate_button.pack(pady=20)

# Results frame
result_frame = ctk.CTkFrame(app, corner_radius=15, fg_color=frame_color)
result_frame.pack(pady=10, padx=20, fill="x")

result_label = ctk.CTkLabel(
    result_frame,
    text="Your results will appear here!",
    font=ctk.CTkFont(size=16),
    text_color=result_color,
    wraplength=400,
    justify="left",
)
result_label.pack(pady=20)

# Footer label
footer_label = ctk.CTkLabel(
    app, text="🔗 Built with Love 💖 ", font=ctk.CTkFont(size=12), text_color="white"
)
footer_label.pack(pady=10)

# Run the application
app.mainloop()
