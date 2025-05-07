import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

# ===== FUNCTIONS FOR EACH TOOL =====

def scientific_calculator():
    window = tk.Toplevel()
    window.title("Scientific Calculator - Siddiqui Saba | Next Hikes IT Solutions")
    window.configure(bg="black")

    entry = tk.Entry(window, font=("Arial", 20), width=25, bg="black", fg="cyan")
    entry.grid(row=0, column=0, columnspan=6)

    def click(event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(entry.get())
                entry.delete(0, tk.END)
                entry.insert(tk.END, result)
            except:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
        elif text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, text)

    buttons = [
        ["7", "8", "9", "/", "sin", "cos"],
        ["4", "5", "6", "*", "tan", "log"],
        ["1", "2", "3", "-", "(", ")"],
        ["0", "=", "+", "sqrt", "**", "C"]
    ]

    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            b = tk.Button(window, text=buttons[i][j], font=("Arial", 14), fg="cyan", bg="black", width=6, height=2)
            b.grid(row=i + 1, column=j)
            b.bind("<Button-1>", click)

def unit_converter():
    window = tk.Toplevel()
    window.title("Unit Converter - Siddiqui Saba | Next Hikes IT Solutions")

    entry = tk.Entry(window)
    entry.pack(pady=10)

    variable = tk.StringVar(window)
    variable.set("Kg to Pound")

    menu = tk.OptionMenu(window, variable, "Kg to Pound", "Km to Miles")
    menu.pack(pady=10)

    result_label = tk.Label(window, text="Result: ")
    result_label.pack(pady=10)

    def convert():
        try:
            value = float(entry.get())
            conversion = variable.get()
            if conversion == "Kg to Pound":
                result = value * 2.20462
            elif conversion == "Km to Miles":
                result = value * 0.621371
            result_label.config(text=f"Result: {round(result, 2)}")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")

    btn = tk.Button(window, text="Convert", command=convert)
    btn.pack(pady=10)

def currency_converter():
    window = tk.Toplevel()
    window.title("Currency Converter - Siddiqui Saba | Next Hikes IT Solutions")

    entry = tk.Entry(window)
    entry.pack(pady=10)

    variable = tk.StringVar(window)
    variable.set("INR to USD")

    menu = tk.OptionMenu(window, variable, "INR to USD", "USD to INR")
    menu.pack(pady=10)

    result_label = tk.Label(window, text="Converted Amount: ")
    result_label.pack(pady=10)

    def convert():
        try:
            amount = float(entry.get())
            conversion = variable.get()
            if conversion == "INR to USD":
                result = amount * 0.012
            elif conversion == "USD to INR":
                result = amount * 83.0
            result_label.config(text=f"Converted Amount: {round(result, 2)}")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount")

    btn = tk.Button(window, text="Convert", command=convert)
    btn.pack(pady=10)

def age_calculator():
    window = tk.Toplevel()
    window.title("Age Calculator - Siddiqui Saba | Next Hikes IT Solutions")

    label = tk.Label(window, text="Enter DOB (dd-mm-yyyy):")
    label.pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=10)

    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

    def calculate_age():
        try:
            dob = datetime.strptime(entry.get(), "%d-%m-%Y")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            result_label.config(text=f"Your Age: {age} years")
        except:
            messagebox.showerror("Error", "Enter DOB in dd-mm-yyyy format")

    btn = tk.Button(window, text="Calculate Age", command=calculate_age)
    btn.pack(pady=10)

# ===== MAIN WINDOW =====

root = tk.Tk()
root.title("Super Calculator - Siddiqui Saba | Next Hikes IT Solutions")
root.geometry("400x400")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="SUPER CALCULATOR", font="Arial 22 bold", fg="white", bg="#1e1e1e")
title.pack(pady=20)

btn1 = tk.Button(root, text="Scientific Calculator", font="Arial 18", bg="#4caf50", fg="white", width=25, command=scientific_calculator)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Unit Converter", font="Arial 18", bg="#2196f3", fg="white", width=25, command=unit_converter)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Currency Converter", font="Arial 18", bg="#9c27b0", fg="white", width=25, command=currency_converter)
btn3.pack(pady=10)

btn4 = tk.Button(root, text="Age Calculator", font="Arial 18", bg="#ff5722", fg="white", width=25, command=age_calculator)
btn4.pack(pady=10)

btn5 = tk.Button(root, text="Exit", font="Arial 18", bg="#f44336", fg="white", width=25, command=root.destroy)
btn5.pack(pady=30)

root.mainloop()