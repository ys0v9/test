import tkinter as tk

win=tk.Tk()
win.title('계산기')
win.geometry('570x600')
win.resizable(False, False)
win.configure(bg='#17161b')

# 계산 결과 레이블
label_result=tk.Label(win, width=25, height=2, text='', font='arial 30')
label_result.place(x=0, y=0) #or #label_result.pack()

# 버튼 : C / % *
clear_button = tk.Button(win, width=5, height=1, text='C', font='arial 30 bold', fg='white', bg='#f7686a')
clear_button.place(x=10, y=100)

div_button=tk.Button(win, width=5, height=1, text='/', font='arial 30', fg='white', bg='#943738')
div_button.place(x=150, y=100)

divmod_button=tk.Button(win, width=5, height=1, text='%', font='arial 30', fg='white', bg='#943738')
divmod_button.place(x=290, y=100)

muiti_button=tk.Button(win, width=5, height=1, text='*', font='arial 30', fg='white', bg='#943738')
muiti_button.place(x=430, y=100)

# 버튼 7 8 9 -
num7_button=tk.Button(win, width=5, height=1, text='7', font='arial 30', fg='white', bg='#591f20')
num7_button.place(x=10,y=190)

num8_button=tk.Button(win, width=5, height=1, text='8', font='arial 30', fg='white', bg='#591f20')
num8_button.place(x=150, y=190)

num9_button=tk.Button(win, width=5, height=1, text='9', font='arial 30', fg='white', bg='#591f20')
num9_button.place(x=290, y=190)

minus_button=tk.Button(win, width=5, height=1, text='-', font='arial 30', fg='white', bg='#591f20')
minus_button.place(x=430, y=190)


win.mainloop()
