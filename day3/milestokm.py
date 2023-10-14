import tkinter as tk
window=tk.Tk()
window.title("MILES ->> KILOMETERS")
window.minsize(500,300)
text1 = tk.StringVar()

label1=tk.Label(text="Miles",font="Times 20")
label1.grid(padx=200,pady=10)

entry1=tk.Entry()
entry1.grid(padx=200,pady=10)

label2=tk.Label(text="Kilometers",font="Times 20")
label2.grid(padx=200,pady=10)

entry2=tk.Entry(textv=text1)
entry2.grid(padx=200,pady=10)

def click():
    n=float(entry1.get())
    num=1.60934*n
    text1.set(num)

button=tk.Button(text="Convert",font="20",command=click)
button.grid(row=4,column=4)

window.mainloop()