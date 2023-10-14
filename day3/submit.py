import tkinter as tk
window = tk.Tk()
window.title("GUI")
window.minsize(500,300)

entry=tk.Entry()
entry.pack()
    

def click():
    txt=entry.get()
    label.config(text=txt)
      
button=tk.Button(text="submit",command=click)
button.pack()

label=tk.Label(text="Name",font="Sans 12")
label.pack(side="bottom")




window.mainloop()