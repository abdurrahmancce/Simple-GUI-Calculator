import tkinter as tk

# ----------------------------
# Main Window
# ----------------------------
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("350x500")
root.resizable(False, False)

# ----------------------------
# Dark Mode Control
# ----------------------------
dark_mode = False

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    bg = "#1e1e1e" if dark_mode else "white"
    fg = "white" if dark_mode else "black"
    btn_bg = "#333" if dark_mode else "#f0f0f0"

    root.config(bg=bg)
    entry.config(bg=bg, fg=fg, insertbackground=fg)

    for btn in buttons_list:
        btn.config(bg=btn_bg, fg=fg)

# ----------------------------
# History
# ----------------------------
history = []

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("History")
    history_window.geometry("300x400")

    tk.Label(history_window, text="Calculation History", font=("Arial", 14, "bold")).pack()

    for item in history:
        tk.Label(history_window, text=item, anchor="w").pack(fill="both")

# ----------------------------
# Functions
# ----------------------------
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)

        history.append(f"{expression} = {result}")

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ----------------------------
# Keyboard Support
# ----------------------------
def key_input(event):
    if event.char in "0123456789+-*/%.()":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get())-1, tk.END)

root.bind("<Key>", key_input)

# ----------------------------
# Display Entry
# ----------------------------
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", ipadx=10, ipady=20, padx=10, pady=10)

# ----------------------------
# Buttons Layout
# ----------------------------
frame = tk.Frame(root)
frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '%', 'C', '+'],
]

buttons_list = []

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "C":
            action = clear
        else:
            action = lambda x=btn: click(x)

        b = tk.Button(row_frame, text=btn, font=("Arial", 14), command=action)
        b.pack(side="left", expand=True, fill="both")
        buttons_list.append(b)

# ----------------------------
# Extra Buttons
# ----------------------------
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="both")

tk.Button(bottom_frame, text="=", font=("Arial", 16), bg="lightblue",
          command=calculate).pack(fill="both")

tk.Button(bottom_frame, text="History", command=show_history).pack(fill="both")

tk.Button(bottom_frame, text="Dark Mode", command=toggle_theme).pack(fill="both")

root.mainloop()
