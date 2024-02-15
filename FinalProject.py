from tkinter import *
import tkinter as tk

root = Tk()
root.title("Calculator")
root.geometry("295x544")
root.resizable(False, False)
root.configure(bg="black")

button_radius = 50

# Row 1
canvas_button_ac = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_ac.grid(row=0, column=0, padx=4, pady=10)
circle_button_ac = canvas_button_ac.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='lightgrey')
text_ac = canvas_button_ac.create_text(0.65*button_radius, 0.65*button_radius, text="AC", fill="black", font=("Arial", 20))

canvas_button_pm = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_pm.grid(row=0, column=1, padx=4, pady=10)
circle_button_pm = canvas_button_pm.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='lightgrey')
text_pm = canvas_button_pm.create_text(0.65*button_radius, 0.65*button_radius, text="+/-", fill="black", font=("Arial", 20))

canvas_button_percent = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_percent.grid(row=0, column=2, padx=4, pady=10)
circle_button_percent = canvas_button_percent.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='lightgrey')
text_percent = canvas_button_percent.create_text(0.65*button_radius, 0.65*button_radius, text="%", fill="black", font=("Arial", 20))

canvas_button_divide = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_divide.grid(row=0, column=3, padx=4, pady=10)
circle_button_divide = canvas_button_divide.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_divide = canvas_button_divide.create_text(0.65*button_radius, 0.65*button_radius, text="/", fill="white", font=("Arial", 20))

# Row 2
canvas_button_7 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_7.grid(row=1, column=0, padx=4, pady=10)
circle_button_7 = canvas_button_7.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_7 = canvas_button_7.create_text(0.65*button_radius, 0.65*button_radius, text="7", fill="white", font=("Arial", 20))

canvas_button_8 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_8.grid(row=1, column=1, padx=4, pady=10)
circle_button_8 = canvas_button_8.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_8 = canvas_button_8.create_text(0.65*button_radius, 0.65*button_radius, text="8", fill="white", font=("Arial", 20))

canvas_button_9 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_9.grid(row=1, column=2, padx=4, pady=10)
circle_button_9 = canvas_button_9.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_9 = canvas_button_9.create_text(0.65*button_radius, 0.65*button_radius, text="9", fill="white", font=("Arial", 20))

canvas_button_multiply = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_multiply.grid(row=1, column=3, padx=4, pady=10)
circle_button_multiply = canvas_button_multiply.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_multiply = canvas_button_multiply.create_text(0.65*button_radius, 0.65*button_radius, text="*", fill="white", font=("Arial", 20))

# Row 3
canvas_button_4 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_4.grid(row=2, column=0, padx=4, pady=10)
circle_button_4 = canvas_button_4.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_4 = canvas_button_4.create_text(0.65*button_radius, 0.65*button_radius, text="4", fill="white", font=("Arial", 20))

canvas_button_5 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_5.grid(row=2, column=1, padx=4, pady=10)
circle_button_5 = canvas_button_5.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_5 = canvas_button_5.create_text(0.65*button_radius, 0.65*button_radius, text="5", fill="white", font=("Arial", 20))

canvas_button_6 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_6.grid(row=2, column=2, padx=4, pady=10)
circle_button_6 = canvas_button_6.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_6 = canvas_button_6.create_text(0.65*button_radius, 0.65*button_radius, text="6", fill="white", font=("Arial", 20))

canvas_button_subtract = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_subtract.grid(row=2, column=3, padx=4, pady=10)
circle_button_subtract = canvas_button_subtract.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_subtract = canvas_button_subtract.create_text(0.65*button_radius, 0.65*button_radius, text="-", fill="white", font=("Arial", 20))

# Row 4
canvas_button_1 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_1.grid(row=3, column=0, padx=4, pady=10)
circle_button_1 = canvas_button_1.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_1 = canvas_button_1.create_text(0.65*button_radius, 0.65*button_radius, text="1", fill="white", font=("Arial", 20))

canvas_button_2 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_2.grid(row=3, column=1, padx=4, pady=10)
circle_button_2 = canvas_button_2.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_2 = canvas_button_2.create_text(0.65*button_radius, 0.65*button_radius, text="2", fill="white", font=("Arial", 20))

canvas_button_3 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_3.grid(row=3, column=2, padx=4, pady=10)
circle_button_3 = canvas_button_3.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='darkgrey')
text_3 = canvas_button_3.create_text(0.65*button_radius, 0.65*button_radius, text="3", fill="white", font=("Arial", 20))

canvas_button_add = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_add.grid(row=3, column=3, padx=4, pady=10)
circle_button_add = canvas_button_add.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_add = canvas_button_add.create_text(0.65*button_radius, 0.65*button_radius, text="+", fill="white", font=("Arial", 20))

root.mainloop()
