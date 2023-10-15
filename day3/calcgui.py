import tkinter as tk

window=tk.Tk()
window.title("CALCULATOR")
window.minsize(300,300)

expression = ""
text1 = tk.StringVar()

def click(item):
    global expression
    expression = expression + str(item)
    text1.set(expression)

def clear():
    global expression
    expression = "" 
    text1.set("")

 
def equal():
    global expression
    result = str(eval(expression))
    text1.set(result)

  
entry1 = tk.Entry(textv = text1,width = 50,font="Sans 30")
entry1.grid(row=0, column=0, padx=0, columnspan=4, pady=0, sticky="NSEW")
 
clear = tk.Button( text = "CLEAR", width = 35,bg="gray15", fg="white",height = 3,command = lambda:clear())
clear.grid(row = 1, column = 0, columnspan=3, padx=0, pady=0, sticky="NSEW")

divide = tk.Button(text = "/", font="2",width = 5, height = 3,bg="gray15",fg="white",command =lambda:click("/"))
divide.grid(row = 2, column = 3, padx=0, pady=0, sticky="NSEW")

seven = tk.Button(text = "7",font="2",bg="gray15",fg="white",width = 5, height = 3,command =lambda:click(7))
seven.grid(row = 2, column = 0, padx=0, pady=0, sticky="NSEW")

eight = tk.Button(text = "8",font="2",width = 5,fg="white", bg="gray15",height = 3,command =lambda:click(8))
eight.grid(row = 2, column = 1, padx=0, pady=0, sticky="NSEW")

nine = tk.Button(text = "9", font="2",width = 5,fg="white",bg="gray15", height = 3,command =lambda:click(9))
nine.grid(row = 2, column = 2, padx=0, pady=0, sticky="NSEW")
 
multiply = tk.Button(text = "*",font="2",width = 5, height = 3,bg="gray15",fg="white",command =lambda:click("*"))
multiply.grid(row = 3, column = 3, padx=0, pady=0, sticky="NSEW")

four =tk.Button(text = "4",font="2",width = 5,fg="white",bg="gray15", height = 3,command =lambda:click(4))
four.grid(row = 3, column = 0, padx=0, pady=0, sticky="NSEW")
 
five =tk.Button(text = "5",font="2",bg="gray15",fg="white",width = 5, height = 3,command =lambda:click(5))
five.grid(row = 3, column = 1, padx=0, pady=0, sticky="NSEW")
 
six =tk.Button(text = "6",font="2",bg="gray15",fg="white",width = 5, height = 3,command =lambda:click(6))
six.grid(row = 3, column = 2, padx=0, pady=0, sticky="NSEW")

minus =tk.Button(text = "-",font="2",width = 5, height = 3,bg="gray15",fg="white",command =lambda:click("-"))
minus.grid(row = 4, column = 3, padx=0, pady=0, sticky="NSEW")
 
one =tk.Button(text = "1",font="2",bg="gray15",fg="white",width = 5, height = 3,command =lambda:click(1))
one.grid(row = 4, column = 0, padx=0, pady=0, sticky="NSEW")
 
two =tk.Button(text = "2",font="2",bg="gray15",fg="white",width = 5, height = 3,command =lambda:click(2))
two.grid(row = 4, column = 1, padx=0, pady=0, sticky="NSEW")
 
three =tk.Button(text = "3",font="2",bg="gray15",fg="white",width = 5, height = 3,command =lambda:click(3))
three.grid(row = 4, column = 2, padx=0, pady=0, sticky="NSEW")
 
plus =tk.Button(text = "+",font="2",width = 5, height = 3,bg="gray15",fg="white",command =lambda:click("+"))
plus.grid(row = 5, column = 3, padx=0, pady=0, sticky="NSEW")

zero = tk.Button(text = "0",font="2",bg="gray15",fg="white",width = 5, height = 3,command = lambda: click(0))
zero.grid(row = 5, column = 0, columnspan=2, padx=0, pady=0, sticky="NSEW")
 
point = tk.Button(text = ".",font="2",bg="gray15",fg="white",width = 5, height = 3,command = lambda:click("."))
point.grid(row = 5, column = 2, padx=0, pady=0, sticky="NSEW")
 
equal = tk.Button(text = "=",font="2",width = 5,fg="white", bg="gray15",height = 3,command = lambda:equal())
equal.grid(row = 1, column = 3, padx=0, pady=0, sticky="NSEW")

window.mainloop()