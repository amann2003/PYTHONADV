import tkinter as tk
import random
def pw():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password=[]
    for i in range(0,5):
        password.append(random.choice(letters))
    for i in range(0,3):
        password.append(random.choice(numbers))
    for i in range(0,2):
        password.append(random.choice(symbols))
        
    random.shuffle(password)

    ab=""
    for i in password:
        ab+=i

    label2.config(text=f"Your newly generated password is  {ab}")


window=tk.Tk()
window.title("Password Generator")
window.minsize(500,300)
window.configure(bg='gray89')

label1=tk.Label(text="Welcome to Password Generator 2.0!",font="Times 30",fg="crimson")
label1.grid(padx=500,pady=10,sticky="N")


button=tk.Button(text="Generate a strong Password",font="10",command=pw)
button.grid(padx=500,pady=35)


label2=tk.Label(text="Password >>> ",font="Times")
label2.grid(padx=500,pady=50)


window.mainloop()