from tkinter import *
import tkinter.font as font

top = Tk()

myFont2 = font.Font(family='Calibri',size = 15)

functions = []
def getFunc(event):
    global functions
    global entries
    for i in entries:
        y = '{x}'.format(x = i.entryText.get())
        if y != '':
            functions.append(y)   
    top.destroy()


class newEntry():
    def __init__(self,row):
        self.row = row
        self.entryText = StringVar()
        self.enter = Entry(top, width=25,textvariable = self.entryText)
        self.enter['font'] = font.Font(family='Calibri',size = 38)
        self.enter.grid(row = row, column = 5, columnspan = 10)

entries = [newEntry(x) for x in range(0,5)]

numEnterBut = Button(top,text = 'Plot Graph',width = 65,height = 2,relief = 'flat',bg = 'brown1')
numEnterBut.bind('<Button-1>',getFunc)
numEnterBut['font'] = myFont2
numEnterBut.grid(row = 6, column = 6,columnspan = 7 )

top.resizable(False,False)
top.mainloop()
