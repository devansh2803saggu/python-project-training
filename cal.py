import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# GUI Setup
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button Layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in button_texts:
    frame = tk.Frame(root)
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", padx=20, pady=20)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", click)
    frame.pack(expand=True, fill=tk.BOTH)

root.mainloop()
