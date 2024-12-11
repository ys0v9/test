import tkinter as tk
from tkinter import filedialog

win=tk.Tk()
win.title('To Do List')
win.geometry('400x650')
win.resizable(False, False)

task_list=[]

def add_task():
    print('할 일 추가하는 함수')
def delete_task():
    print('할 일 삭제하는 함수')
def opentaskfile():
    try:
        global task_list

        taskfile=open('taskfile.txt','r',encoding='utf-8')
        tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(tk.END,task)
        taskfile.close()
    except:
        file=open('taskfile.txt','w',encoding='utf-8')
        file.close()

image_icon=tk.PhotoImage(file='image/task.png')
win.iconphoto(False,image_icon)

top_image=tk.PhotoImage(file='image/topbar.png')
top_label=tk.Label(win ,image=top_image)
top_label.pack()

dock_image=tk.PhotoImage(file='image/dock.png')
dock_label=tk.Label(win ,image=dock_image,bg='#32405b')
dock_label.place(x=30,y=25)

note_image=tk.PhotoImage(file='image/task.png')
note_label=tk.Label(win ,image=note_image,bg='#32405b')
note_label.place(x=340,y=17)

heading_label=tk.Label(win,text='ALL TASK',font='arial 20 bold',bg='#32405b',fg='#ffffff')
heading_label.place(x=130,y=20)

#main
frame=tk.Frame(win,width=400,height=50,bg='#ffffff')
frame.place(x=0,y=180)

task=tk.StringVar()
task_entry=tk.Entry(frame,width=18,font='arial 20',bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=tk.Button(frame,text='ADD',width=6,font='arial 20 bold',bg='#32405b',fg='#ffffff',
                 command=add_task)
button.place(x=290,y=0)

#listbox
listbox_frame=tk.Frame(win, width=700, height=280,bg='#32405b')
listbox_frame.pack(pady=(160,0))

listbox=tk.Listbox(listbox_frame,font='arial 12',width=40,height=16,bg='#32405b',fg='#ffffff',
                   cursor='hand2',selectbackground='#32405b')
listbox.pack(side=tk.LEFT,fill=tk.BOTH,padx=(2,0))

scrollbar=tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# for i in range(0,50,1):
#     listbox.insert(0,'놀기'+str(i+1))

opentaskfile()
#delete
delete_image=tk.PhotoImage(file='image/delete.png')
delete_button=tk.Button(win, image=delete_image,bd=0,command=delete_task)
delete_button.pack(side=tk.BOTTOM,pady=13)

win.mainloop()