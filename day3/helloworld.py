import tkinter as tk

def click():
    label.config(text="Hello, World!")

window = tk.Tk()
window.title("Python World")
window.minsize=(400,300)


button=tk.Button(text="Click Here", command=click,font="10")
button.grid(padx=700,pady=50,sticky="N")

label=tk.Label(text="",font="georgia 15 bold",fg="crimson")
label.grid(padx=700,pady=50)


window.mainloop()
