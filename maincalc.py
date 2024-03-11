from tkinter import *

root = Tk()
tab = Entry(root, width=30)
tab.grid(row=0, column=0, columnspan=4)

operator = None

def button_add(num):
    cur = tab.get()
    tab.delete(0, END)
    tab.insert(0, str(cur) + str(num))

def button_clear():
    tab.delete(0, END)

f_num = 0

def addition():
    global operator
    operator = '+'
    first_num = tab.get()
    global f_num
    f_num = int(first_num)
    tab.delete(0, END)

def subtraction():
    global operator
    operator = '-'
    first_num = tab.get()
    global f_num
    f_num = int(first_num)
    tab.delete(0, END)

def multiplication():
    global operator
    operator = '*'
    first_num = tab.get()
    global f_num
    f_num = int(first_num)
    tab.delete(0, END)

def division():
    global operator
    operator = '/'
    first_num = tab.get()
    global f_num
    f_num = int(first_num)
    tab.delete(0, END)

def equal():
    second_num = tab.get()
    tab.delete(0, END)
    if f_num is not None and second_num:
        if operator == '+':
            result = f_num + int(second_num)
        elif operator == '-':
            result = f_num - int(second_num)
        elif operator == '*':
            result = f_num * int(second_num)
        elif operator == '/':
            if int(second_num) != 0:
                result = f_num / int(second_num)
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operator"
        tab.insert(0, str(result))

button0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_add(0))
button1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_add(1))
button2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_add(2))
button3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_add(3))
button4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_add(4))
button5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_add(5))
button6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_add(6))
button7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_add(7))
button8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_add(8))
button9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_add(9))
button_equal = Button(root, text="=", padx=29, pady=20, command=equal)
button_addition = Button(root, text="+", padx=29, pady=20, command=addition)
button_subtraction = Button(root, text="-", padx=29, pady=20, command=subtraction)
button_multiplication = Button(root, text="*", padx=29, pady=20, command=multiplication)
button_division = Button(root, text="/", padx=29, pady=20, command=division)
button_clear = Button(root, text="Clear", padx=15, pady=20, command=button_clear)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_addition.grid(row=1, column=3)
button_subtraction.grid(row=2, column=3)
button_multiplication.grid(row=3, column=3)
button_division.grid(row=4, column=3)
button_clear.grid(row=4, column=0)

root.mainloop()
