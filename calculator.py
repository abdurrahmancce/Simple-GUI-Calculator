import tkinter as tk

# ------------------------
# Functions
# ------------------------
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# ------------------------
# Main Window
# ------------------------
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x400")

# Entry Box
entry = tk.Entry(root, font=("Arial", 18), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '%', 'C', '+'],
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == 'C':
            action = clear
        else:
            action = lambda x=btn: click(x)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 14),
            command=action
        ).pack(side="left", expand=True, fill="both")

# Equal Button
tk.Button(
    root,
    text="=",
    font=("Arial", 16),
    bg="lightblue",
    command=calculate
).pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()