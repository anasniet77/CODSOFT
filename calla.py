import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=20, font=('Arial', 14), borderwidth=5, relief="ridge",bg="#6F9D9D", fg="black")
entry.grid(row=0, column=0, columnspan=4)

# Row 1
b7 = tk.Button(root, text='7', width=5, height=2, font=('Arial', 12), command=lambda: press('7'))
b7.grid(row=1, column=0)

b8 = tk.Button(root, text='8', width=5, height=2, font=('Arial', 12), command=lambda: press('8'))
b8.grid(row=1, column=1)

b9 = tk.Button(root, text='9', width=5, height=2, font=('Arial', 12), command=lambda: press('9'))
b9.grid(row=1, column=2)

b_div = tk.Button(root, text='/', width=5, height=2, font=('Arial', 12), command=lambda: press('/'),bg="#275554", fg="white")
b_div.grid(row=1, column=3)

# Row 2
b4 = tk.Button(root, text='4', width=5, height=2, font=('Arial', 12), command=lambda: press('4'))
b4.grid(row=2, column=0)

b5 = tk.Button(root, text='5', width=5, height=2, font=('Arial', 12), command=lambda: press('5'))
b5.grid(row=2, column=1)

b6 = tk.Button(root, text='6', width=5, height=2, font=('Arial', 12), command=lambda: press('6'))
b6.grid(row=2, column=2)

b_mul = tk.Button(root, text='*', width=5, height=2, font=('Arial', 12), command=lambda: press('*'),bg="#346160", fg="white")
b_mul.grid(row=2, column=3)

# Row 3
b1 = tk.Button(root, text='1', width=5, height=2, font=('Arial', 12), command=lambda: press('1'))
b1.grid(row=3, column=0)

b2 = tk.Button(root, text='2', width=5, height=2, font=('Arial', 12), command=lambda: press('2'))
b2.grid(row=3, column=1)

b3 = tk.Button(root, text='3', width=5, height=2, font=('Arial', 12), command=lambda: press('3'))
b3.grid(row=3, column=2)

b_sub = tk.Button(root, text='-', width=5, height=2, font=('Arial', 12), command=lambda: press('-'),bg="#356A69", fg="white")
b_sub.grid(row=3, column=3)

# Row 4
b0 = tk.Button(root, text='0', width=5, height=2, font=('Arial', 12), command=lambda: press('0'))
b0.grid(row=4, column=0)

b_dot = tk.Button(root, text='.', width=5, height=2, font=('Arial', 12), command=lambda: press('.'))
b_dot.grid(row=4, column=1)

b_add = tk.Button(root, text='+', width=5, height=2, font=('Arial', 12), command=lambda: press('+'),bg="#357877", fg="white")
b_add.grid(row=4, column=3)

b_eq = tk.Button(root, text='=', width=5, height=2, font=('Arial', 12), command=calculate,bg="#AD3440", fg="white")
b_eq.grid(row=4, column=2)
clear_button = tk.Button(root, text="CLEAR", width=10, height=2, font=('Arial', 12), command=clear,bg="#0D6712", fg="white")
clear_button.grid(row=5, column=0, columnspan=4)

root.configure(bg='light blue')
root.mainloop()