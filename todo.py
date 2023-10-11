import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set the background color to an Instagram-like gradient
root.configure(bg='#f2e6dd')

# Create and configure the listbox with a larger font
listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=('Helvetica', 14))
listbox.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

# Create an entry field for adding tasks
entry = tk.Entry(root, font=('Helvetica', 14))
entry.pack(pady=10, padx=10, fill=tk.BOTH)

# Create buttons for adding and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task, font=('Helvetica', 12))
delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=('Helvetica', 12))
add_button.pack(pady=5, padx=10, fill=tk.BOTH)
delete_button.pack(pady=5, padx=10, fill=tk.BOTH)

# Start the main loop
root.geometry("400x400")
root.mainloop()
