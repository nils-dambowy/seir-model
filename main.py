import tkinter as tk

window = tk.Tk()
window.geometry("800x400")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1], minsize=200)
window.columnconfigure([0,1], minsize=200)

user_input = tk.StringVar()

def get_input():
    user_input = e1.get()
    print(user_input)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, padx=100)

label2 = tk.Label(text="B")
label2.grid(row=0, column=1, padx=100)

label1 = tk.Label(text="C")
label1.grid(row=1, column=0, padx=100)

label2 = tk.Label(text="D")
label2.grid(row=1, column=1, padx=100)

e1 = tk.Entry(window, textvariable=user_input)
e1.grid(row=0, column=2)

b1 = tk.Button(window, command=get_input)
b1.grid(row=1, column=2)

window.mainloop()