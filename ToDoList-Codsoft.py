from asyncio import TaskGroup
from modulefinder import packagePathMap
from struct import pack
import tkinter
print ('Imported')

#1. import module
from tkinter import *
from tkinter import messagebox

# create functions 
def newTask():
    Task=my_entry.get()
    if Task != "":
        lb.insert(END, TaskGroup)
        my_entry.delete(0, "end")
    else: 
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
        
#2. configure & create mainwindow
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-do-list')
ws.config(bg='black')
ws.resizable(width=False, height=False)

#4. create widgets (frames, Lsitbox, scrollbar, entry, button)
frame = Frame(ws)

frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='white',
    
)

lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Wake up early',
    'Drink water',
    'Attend classes',
    'Take Notes',
    'Have proper lunch',
    'Return Hostel',
    'Take a nap',
    'Friends and family time',
    'Study',
    'Sleep'
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('Times', 24)
)
my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addtask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Times 14'),
    bg='green',
    padx=20,
    pady=10,
    command=newTask
)
addtask_btn.pack(fill=BOTH, expand=True, side=LEFT)

deltask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Times 14'),
    bg= 'yellow',
    padx=20,
    pady=10,
    command= deleteTask
)
deltask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#3. create mainloop
ws.mainloop()

