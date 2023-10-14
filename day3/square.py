import tkinter as tk
window = tk.Tk()
window.title("GUI")
window.minsize(500,300)
 
entry=tk.Entry()
entry.grid(padx=700,pady=10,column=1,row=1,)

    

def click():
    n=float(entry.get())
    num=n*n
    label.config(text=num)
      
button=tk.Button(text="submit",command=click)
button.grid(padx=700,pady=20,column=1,row=2)

label=tk.Label(text="SQUARE",font="Sans 12")
label.grid(padx=700,pady=500,column=1,row=3)


window.mainloop()