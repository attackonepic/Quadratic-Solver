from tkinter import *
import math

def solver():
    try:
        a = int(entrada_a.get())
        b = int(entrada_b.get())
        c = int(entrada_c.get())
        b = -b
        d = 4 * a * c
        e = b * b
        f = e - d
        
        if f >= 0:
            raiz = math.sqrt(f)
            x1 = (b + raiz) / (2 * a)
            x2 = (b - raiz) / (2 * a)
            
            if x1 != x2:
                entrada_x1.insert(0, x1)
                entrada_x2.insert(0, x2)
            else:
                entrada_x1.insert(x1)
        else:
                entrada_x1.insert(0, "Negative")
                entrada_x2.insert(0, "root")
    except ValueError:
        pass
    
def clear():
    entrada_a.delete(0, END)
    entrada_b.delete(0, END)
    entrada_c.delete(0, END)
    entrada_x1.delete(0, END)
    entrada_x2.delete(0, END)

window = Tk()

window.rowconfigure(3, minsize=50, weight=1)
window.columnconfigure(3, minsize=50, weight=1)

entrada_a = Entry(window, width=10, borderwidth=5)
entrada_b = Entry(window, width=10, borderwidth=5)
entrada_c = Entry(window, width=10, borderwidth=5)
entrada_x1 = Entry(window, width=20, borderwidth=5)
entrada_x2 = Entry(window, width=20, borderwidth=5)

lbl_a = Label(window, text="a", font="Arial 13")
lbl_b = Label(window, text="b", font="Arial 13")
lbl_c = Label(window, text="c", font="Arial 13")
lbl_x1 = Label(window, text="x1", font="Arial 13")
lbl_x2 = Label(window, text="x2", font="Arial 13")

btn_solve = Button(window, text="Solve!", padx=40, pady=10, command=solver, font="Arial 11", fg="white", bg="green")
btn_clear = Button(window, text="Clear", padx=40, pady=10, command=clear, font="Arial 11", fg="white", bg="green")

entrada_a.grid(row=0, column=1)
entrada_b.grid(row=1, column=1)
entrada_c.grid(row=2, column=1)
entrada_x1.grid(row=0, column=3)
entrada_x2.grid(row=2, column=3)

lbl_a.grid(row=0, column=0)
lbl_b.grid(row=1, column=0)
lbl_c.grid(row=2, column=0)
lbl_x1.grid(row=0, column=2)
lbl_x2.grid(row=2, column=2)

btn_solve.grid(row=3, column=0, columnspan=2)
btn_clear.grid(row=3, column=2, columnspan=2)

window.title("QES")
window.mainloop()