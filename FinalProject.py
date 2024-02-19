from tkinter import *
import tkinter as tk
import re

root = Tk()
root.title("Calculator")
root.geometry("295x544")
root.resizable(False, False)
root.configure(bg="black")

button_radius = 50
new_number = True
entry = None 
new_number = True
clear_entry_on_next_input = False


def add_digit(digit):
    global new_number, clear_entry_on_next_input
    if clear_entry_on_next_input:
        entry.delete(0, END)
        clear_entry_on_next_input = False
    current_text = entry.get()
    if current_text == "0" or new_number:
        entry.delete(0, END)
        entry.insert(END, str(digit))
        new_number = False
    else:
        entry.insert(END, str(digit))


def clear_entry():
    global entry, new_number
    if entry is not None:
        entry.delete(0, END)
        entry.insert(END, "0")
        new_number = True 

# Row 1
canvas_button_ac = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_ac.place(x=6, y=176)
circle_button_ac = canvas_button_ac.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='lightgrey')
text_ac = canvas_button_ac.create_text(0.65*button_radius, 0.65*button_radius, text="AC", fill="black", font=("Arial", 20))

canvas_button_ac.bind("<Button-1>", lambda event: clear_entry())


canvas_button_pm = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_pm.place(x=78, y=176)
circle_button_pm = canvas_button_pm.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='lightgrey')
text_pm = canvas_button_pm.create_text(0.65*button_radius, 0.65*button_radius, text="+/-", fill="black", font=("Arial", 20))

sign = ""

def change_sign():
    global sign
    if sign == "":
        sign = "-"
    else:
        sign = ""
    current_text = entry.get()
    if current_text.startswith("-"):
        current_text = current_text[1:]
    else:
        current_text = "-" + current_text
    entry.delete(0, END)
    entry.insert(0, current_text)

canvas_button_pm.bind("<Button-1>", lambda event: change_sign())


canvas_button_percent = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_percent.place(x=150, y=176)
circle_button_percent = canvas_button_percent.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='lightgrey')
text_percent = canvas_button_percent.create_text(0.65*button_radius, 0.65*button_radius, text="%", fill="black", font=("Arial", 20))

def calculate_percentage():
    try:
        number = float(entry.get())
        result = number / 100
        entry.delete(0, END)
        entry.insert(END, str(result))
    except ValueError:
        entry.delete(0, END)
        entry.insert(END, "Error")

canvas_button_percent.bind("<Button-1>", lambda event: calculate_percentage())


canvas_button_divide = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_divide.place(x=222, y=176)
circle_button_divide = canvas_button_divide.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_divide = canvas_button_divide.create_text(0.65*button_radius, 0.65*button_radius, text="/", fill="white", font=("Arial", 20))


# Row 2
canvas_button_7 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_7.place(x=6, y=250)
circle_button_7 = canvas_button_7.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_7 = canvas_button_7.create_text(0.65*button_radius, 0.65*button_radius, text="7", fill="white", font=("Arial", 20))

canvas_button_8 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_8.place(x=78, y=250)
circle_button_8 = canvas_button_8.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_8 = canvas_button_8.create_text(0.65*button_radius, 0.65*button_radius, text="8", fill="white", font=("Arial", 20))

canvas_button_9 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_9.place(x=150, y=250)
circle_button_9 = canvas_button_9.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_9 = canvas_button_9.create_text(0.65*button_radius, 0.65*button_radius, text="9", fill="white", font=("Arial", 20))

canvas_button_multiply = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_multiply.place(x=222, y=250)
circle_button_multiply = canvas_button_multiply.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_multiply = canvas_button_multiply.create_text(0.65*button_radius, 0.65*button_radius, text="*", fill="white", font=("Arial", 20))

canvas_button_7.bind("<Button-1>", lambda event: add_digit(7))
canvas_button_8.bind("<Button-1>", lambda event: add_digit(8))
canvas_button_9.bind("<Button-1>", lambda event: add_digit(9))

# Row 3
canvas_button_4 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_4.place(x=6, y=324)
circle_button_4 = canvas_button_4.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_4 = canvas_button_4.create_text(0.65*button_radius, 0.65*button_radius, text="4", fill="white", font=("Arial", 20))

canvas_button_5 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_5.place(x=78, y=324)
circle_button_5 = canvas_button_5.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_5 = canvas_button_5.create_text(0.65*button_radius, 0.65*button_radius, text="5", fill="white", font=("Arial", 20))

canvas_button_6 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_6.place(x=150, y=324)
circle_button_6 = canvas_button_6.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_6 = canvas_button_6.create_text(0.65*button_radius, 0.65*button_radius, text="6", fill="white", font=("Arial", 20))

canvas_button_subtract = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_subtract.place(x=222, y=324)
circle_button_subtract = canvas_button_subtract.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_subtract = canvas_button_subtract.create_text(0.65*button_radius, 0.65*button_radius, text="-", fill="white", font=("Arial", 20))

canvas_button_4.bind("<Button-1>", lambda event: add_digit(4))
canvas_button_5.bind("<Button-1>", lambda event: add_digit(5))
canvas_button_6.bind("<Button-1>", lambda event: add_digit(6))

# Row 4
canvas_button_1 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_1.place(x=6, y=398)
circle_button_1 = canvas_button_1.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_1 = canvas_button_1.create_text(0.65*button_radius, 0.65*button_radius, text="1", fill="white", font=("Arial", 20))

canvas_button_2 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_2.place(x=78, y=398)
circle_button_2 = canvas_button_2.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_2 = canvas_button_2.create_text(0.65*button_radius, 0.65*button_radius, text="2", fill="white", font=("Arial", 20))

canvas_button_3 = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_3.place(x=150, y=398)
circle_button_3 = canvas_button_3.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_3 = canvas_button_3.create_text(0.65*button_radius, 0.65*button_radius, text="3", fill="white", font=("Arial", 20))

canvas_button_add = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_add.place(x=222, y=398)
circle_button_add = canvas_button_add.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_add = canvas_button_add.create_text(0.65*button_radius, 0.65*button_radius, text="+", fill="white", font=("Arial", 20))

canvas_button_1.bind("<Button-1>", lambda event: add_digit(1))
canvas_button_2.bind("<Button-1>", lambda event: add_digit(2))
canvas_button_3.bind("<Button-1>", lambda event: add_digit(3))

# Row 5
canvas_button_0 = tk.Canvas(root, width=2.6*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_0.place(x=6, y=472)
circle_button_0 = canvas_button_0.create_oval(0, 0, 2.6*button_radius, 1.3*button_radius, fill='#333333')
center_x = 1.3*button_radius / 2
center_y = 1.3*button_radius / 2

text_0 = canvas_button_0.create_text(center_x, center_y, text="0", fill="white", font=("Arial", 20))




canvas_button_comma = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_comma.place(x=150, y=472)
circle_button_comma = canvas_button_comma.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='#333333')
text_comma = canvas_button_comma.create_text(0.65*button_radius, 0.65*button_radius, text=".", fill="white", font=("Arial", 20))

def add_comma():
    current_text = entry.get()
    if '.' not in current_text:
        entry.insert(END, '.')
    else:
        pass

canvas_button_comma.bind("<Button-1>", lambda event: add_comma())


canvas_button_equal = tk.Canvas(root, width=1.3*button_radius, height=1.3*button_radius, bg='black', highlightthickness=0)
canvas_button_equal.place(x=222, y=472)
circle_button_equal = canvas_button_equal.create_oval(0, 0, 1.3*button_radius, 1.3*button_radius, fill='orange')
text_equal = canvas_button_equal.create_text(0.65*button_radius, 0.65*button_radius, text="=", fill="white", font=("Arial", 20))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

canvas_button_equal.bind("<Button-1>", lambda event: calculate())


canvas_button_0.bind("<Button-1>", lambda event: add_digit(0))

#Entry

def limit_entry(event):
    if entry.winfo_width() <= entry.index('end') + 1:
        return 'break'
    else:
        return None

def validate_input(event):
    char = event.char
    if char.isdigit() or char in ['+', '-', '*', '/', '.']:
        current_text = entry.get()
        entry.delete(0, END)
        entry.insert(END, current_text + char)
    elif char == '\r':  # Обробка натискання клавіші Enter як натискання "="
        calculate()
    return 'break'  # Забороняємо введення символів через обробник подій




entry = Entry(root, width=13, font=("Arial", 30), bg="black", fg="white", justify="right", border=False)
entry.insert(END, "0")
entry.place(x=2.5, y=120)

def add_text():
    text = "New Text"
    entry.insert('end', text[::-1])
entry.bind("<Key>", validate_input)

entry.focus_set()

#6

def perform_operation(operation):
    current_text = entry.get()
    if current_text and current_text[-1] not in ['+', '-', '*', '/']:
        entry.insert(END, operation)
    elif current_text and current_text[-1] in ['+', '-', '*', '/']:
        entry.delete(len(current_text) - 1, END)
        entry.insert(END, operation)

def add():
    perform_operation('+')

def subtract():
    perform_operation('-')

def multiply():
    perform_operation('*')

def divide():
    perform_operation('/')

canvas_button_add.bind("<Button-1>", lambda event: add())
canvas_button_subtract.bind("<Button-1>", lambda event: subtract())
canvas_button_multiply.bind("<Button-1>", lambda event: multiply())
canvas_button_divide.bind("<Button-1>", lambda event: divide())



def calculate():
    global clear_entry_on_next_input
    current_text = entry.get()
    if current_text and current_text[-1] in ['+', '-', '*', '/']:
        entry.delete(len(current_text) - 1, END)
    expression = entry.get().replace(' ', '')  # Видаляємо пробіли
    parts = re.split(r'(\+|\-|\*|\/)', expression)  # Розбиваємо вираз на числа та оператори
    for i, part in enumerate(parts):
        if part.startswith('0') and len(part) > 1 and not part.startswith('0.'):
            parts[i] = part[1:]  # Видаляємо нуль на початку числа, якщо число не є просто '0' або починається з '0.'
    expression = ''.join(parts)  # Збираємо вираз знову
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")
    clear_entry_on_next_input = True



root.mainloop()
