import tkinter as tk


def fun1():
    pass


def Window_display(name):
    win = tk.Tk()
    win.title(name)
    win.geometry("500x500")
    num1 = tk.Entry(win)
    num1.pack()
    but1 = tk.Button(win, text="click", command=fun1)
    but1.pack()

    win.mainloop()
