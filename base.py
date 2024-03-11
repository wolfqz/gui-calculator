from tkinter import *

root=Tk()
root.title("Calculator")
num1=Entry(root, width=30)
op=Entry(root, width=5)
num2=Entry(root, width=30)

num1.grid(row=0, column=0)
op.grid(row=0, column=1)
num2.grid(row=0, column=2)

def operation():
    n1=int(num1.get())
    operator=op.get()
    n2=int(num2.get())
    result=0

    if operator == "+":
        result=n1+n2
    elif operator == "-":
        result=n1-n2
    elif operator == "*":
        result=n1*n2
    elif operator == "/":
        try:
            result=n1/n2
        except ZeroDivisionError:
            label1=Label(root,text="Zero Divison Error")
            label1.grid(row=2,column=1)
            print("Error: Zero Division Error")
            quit()
    else:
        label2=Label(root,text="Invalid Operator")
        label2.grid(row=2,column=1)
    label=Label(root, text="The result is "+str(result))
    label.grid(row=2, column=1)
b=Button(root, text="Calculate", command=operation)
b.grid(row=1, column=1)
root.mainloop()
