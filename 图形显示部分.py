from tkinter import *
from 爬虫部分 import introduction
window = Tk()
window.title('Python结课大作业')
window.geometry('580x480')
e=Entry(window, show=None,borderwidth=4,justify='center')
e.pack()
def search():
    item=e.get()
    t.insert('1.0',introduction(item))
def clear():
    t.delete('1.0','end')
b1=Button(window, text='查询', width=10,height=1, command=search)
b1.pack()
b2=Button(window, text='清空', width=10,height=1, command=clear)
b2.pack()
t=Text(window, height=20)
t.focus_set()
t.pack(side=LEFT,fill=Y)
scroll=Scrollbar()
scroll.pack(side=LEFT,fill=Y)
scroll.config(command=t.yview)
t.config(yscrollcommand=scroll.set)
window.mainloop()