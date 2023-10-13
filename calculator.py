import tkinter as tk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry field for the display
entry = tk.Entry(root, width=20, font=('Helvetica', 16))
entry.grid(row=0, column=0, columnspan=4)

# Create the number buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val, col_val = 1, 0
for button_text in buttons:
    tk.Button(root, text=button_text, font=('Helvetica', 14), padx=20, pady=20, command=lambda text=button_text: button_click(text)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create the clear button
clear_button = tk.Button(root, text='C', font=('Helvetica', 14), padx=20, pady=20, command=clear_display)
clear_button.grid(row=row_val, column=col_val)

# Create the equals button
equals_button = tk.Button(root, text='=', font=('Helvetica', 14), padx=20, pady=20, command=calculate)
equals_button.grid(row=row_val, column=col_val + 1)

# Start the main loop
root.mainloop()
