from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("320x544")
root.resizable(False, False)
root.configure(bg="black")

button_radius = 50
symbols = ['AC', '+/-', '%', '/',
           '7', '8', '9', '*',
           '4', '5', '6', '-',
           '1', '2', '3', '+']

for i in range(4):
    row_frame = Frame(root, bg='black')
    row_frame.pack(side=TOP, fill=BOTH, expand=True)

    for j in range(4):
        index = i * 4 + j
        symbol = symbols[index]

        if symbol in ['AC', '+/-', '%']:
            button = Button(row_frame, text=symbol, bg='lightgrey', fg='black', width=3, height=1, font=("Arial", 25))
        elif symbol in ['/', '*', '-', '+']:
            button = Button(row_frame, text=symbol, bg='orange', fg='white', width=3, height=1, font=("Arial", 25))
        else:
            button = Button(row_frame, text=symbol, bg='darkgrey', fg='white', width=3, height=1, font=("Arial", 25))
        button.pack(side=LEFT, padx=5, pady=0)

root.mainloop()
