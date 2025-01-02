import tkinter as tk

win=tk.Tk()
win.title('Calculator')
win.geometry('570x600')
win.resizable(False, False)
win.configure(bg='#17161b')

equation=''

def calulator():
    global equation
    result=''

    if equation!='':
        try:
            result=eval(equation)
            equation=str(result)
        except:
            result='error'
            equation=''

    label_result.configure(text=result)
    print('result')

def clear():
    global equation
    equation=''
    label_result.configure(text=equation)
    print('clear')

def show(value):
    global equation
    equation=equation+value
    label_result.configure(text=equation)
    print(value)

# 계산 결과 레이블
label_result=tk.Label(win, width=25, height=2, text='', font='arial 30')
label_result.place(x=0, y=0) #or #label_result.pack()

# 버튼 : C / % *
clear_button = tk.Button(win, width=5, height=1, text='C', font='arial 30 bold', fg='white', bg='#f7686a',command=clear)
clear_button.place(x=10, y=100)

div_button=tk.Button(win, width=5, height=1, text='/', font='arial 30', fg='white', bg='#591f20',command=lambda: show('/'))
div_button.place(x=150, y=100)

divmod_button=tk.Button(win, width=5, height=1, text='%', font='arial 30', fg='white', bg='#591f20',command=lambda: show('%'))
divmod_button.place(x=290, y=100)

muiti_button=tk.Button(win, width=5, height=1, text='*', font='arial 30', fg='white', bg='#591f20',command=lambda: show('*'))
muiti_button.place(x=430, y=100)

# 버튼 7 8 9 -
num7_button=tk.Button(win, width=5, height=1, text='7', font='arial 30', fg='white', bg='#591f20',command=lambda: show('7'))
num7_button.place(x=10,y=200)

num8_button=tk.Button(win, width=5, height=1, text='8', font='arial 30', fg='white', bg='#591f20',command=lambda: show('8'))
num8_button.place(x=150, y=200)

num9_button=tk.Button(win, width=5, height=1, text='9', font='arial 30', fg='white', bg='#591f20',command=lambda: show('9'))
num9_button.place(x=290, y=200)

minus_button=tk.Button(win, width=5, height=1, text='-', font='arial 30', fg='white', bg='#591f20',command=lambda: show('-'))
minus_button.place(x=430, y=200)

# 버튼 4 5 6 +
num4_button=tk.Button(win, width=5, height=1, text='4', font='arial 30', fg='white', bg='#591f20',command=lambda: show('4'))
num4_button.place(x=10,y=300)

num5_button=tk.Button(win, width=5, height=1, text='5', font='arial 30', fg='white', bg='#591f20',command=lambda: show('5'))
num5_button.place(x=150, y=300)

num6_button=tk.Button(win, width=5, height=1, text='6', font='arial 30', fg='white', bg='#591f20',command=lambda: show('6'))
num6_button.place(x=290, y=300)

plus_button=tk.Button(win, width=5, height=1, text='+', font='arial 30', fg='white', bg='#591f20',command=lambda: show('+'))
plus_button.place(x=430, y=300)

#버튼 1 2 3 =
num1_button=tk.Button(win, width=5, height=1, text='1', font='arial 30', fg='white', bg='#591f20',command=lambda: show('1'))
num1_button.place(x=10,y=400)

num2_button=tk.Button(win, width=5, height=1, text='2', font='arial 30', fg='white', bg='#591f20',command=lambda: show('2'))
num2_button.place(x=150, y=400)

num3_button=tk.Button(win, width=5, height=1, text='3', font='arial 30', fg='white', bg='#591f20',command=lambda: show('3'))
num3_button.place(x=290, y=400)

equals_button=tk.Button(win, width=5, height=3, text='=', font='arial 30', fg='white', bg='#f7686a',command=calulator)
equals_button.place(x=430, y=400)

#버튼 0 .
num0_button=tk.Button(win, width=11, height=1, text='0', font='arial 30', fg='white', bg='#591f20', command=lambda: show('0'))
num0_button.place(x=10,y=500)

dot_button=tk.Button(win, width=5, height=1, text='.', font='arial 30', fg='white', bg='#591f20',command=lambda: show('.'))
dot_button.place(x=290, y=500)

win.mainloop()