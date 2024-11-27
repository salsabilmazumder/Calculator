import tkinter as tk
from tkinter import ttk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Style configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 18), padding=10)
style.configure("TEntry", font=("Arial", 20))

# Entry widget for the display
screen = ttk.Entry(root, justify="right")
screen.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and place buttons
for i, btn_text in enumerate(buttons):
    btn = ttk.Button(root, text=btn_text)
    btn.grid(row=(i // 4) + 1, column=i % 4, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click)

# Configure row and column weights for better resizing
for i in range(5):
    root.rowconfigure(i, weight=1)
    if i < 4:
        root.columnconfigure(i, weight=1)

# Run the application
root.mainloop()

