import tkinter as tk

def add():
    task = entry.get()
    if task:
        lb.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove():
    try:
        selected_task = lb.curselection()[0]
        lb.delete(selected_task)
    except IndexError:
        pass

win= tk.Tk()
win.title("To-Do List")
win.minsize=(500,300)
win.configure(bg="black")

label=tk.Label(text="TO-DO LIST",font="times 20 underline",fg="gold3")
label.grid(pady=10)

entry = tk.Entry(win)
entry.grid(padx=500,pady=10)

lb = tk.Listbox(selectmode=tk.SINGLE,width=35,height=15)
lb.grid(padx=700,pady=30)

button1 = tk.Button(text="Add Task", command=add)
button1.grid(padx=600,pady=10)

button2 = tk.Button(text="Remove Task",command=remove)
button2.grid(padx=600,pady=10)


win.mainloop()
