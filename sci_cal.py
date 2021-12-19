from tkinter import *
import tkinter.font as font

top = Tk()





myFont2 = font.Font(family='Calibri',size = 15)

functions = []

def set_text(text,currentEntry):
    currentEntry.enter.insert(END,text)
    


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
currentEntry = newEntry(1)


xBut = Button(top,text = 'x',width = 5,height = 2,relief = 'flat',bg = 'brown1',command = lambda:set_text('x',currentEntry))
xBut['font'] = myFont2
xBut.grid(row = 0, column = 0)  

openBracketBut = Button(top,text = '(',width = 5,height = 2,relief = 'flat',bg = 'brown1',command = lambda:set_text('(',currentEntry))
openBracketBut['font'] = myFont2
openBracketBut.grid(row = 0, column = 1)

closedBracketBut = Button(top,text = ')',width = 5,height = 2,relief = 'flat',bg = 'brown1',command = lambda:set_text(')',currentEntry))
closedBracketBut['font'] = myFont2
closedBracketBut.grid(row = 0, column = 2)

funcBut = Button(top,text = 'f(x)',width = 5,height = 2,relief = 'flat',bg = 'brown1')
funcBut['font'] = myFont2
funcBut.grid(row = 0, column = 3)


plusBut = Button(top,text = '+',width = 5,height = 2,relief = 'flat',bg = 'ivory3',command = lambda:set_text('+',currentEntry))
plusBut['font'] = myFont2
plusBut.grid(row = 1, column = 0)

subBut = Button(top,text = '-',width = 5,height = 2,relief = 'flat',bg = 'ivory3',activebackground = 'ivory3',command = lambda:set_text('-',currentEntry))
subBut['font'] = myFont2
subBut.grid(row = 2, column = 0)

mulBut = Button(top,text = 'x',width = 5,height = 2,relief = 'flat',bg = 'ivory3',activebackground = 'ivory3',command = lambda:set_text('*',currentEntry))
mulBut['font'] = myFont2
mulBut.grid(row = 3, column = 0)

divBut = Button(top,text = '÷',width = 5,height = 2,relief = 'flat',bg = 'ivory3',command = lambda:set_text('/',currentEntry))
divBut['font'] = myFont2
divBut.grid(row = 4, column = 0)

num1But = Button(top,text = '1',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('1',currentEntry))
num1But['font'] = myFont2
num1But.grid(row = 1, column = 1)

num2But = Button(top,text = '2',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text(2,currentEntry))
num2But['font'] = myFont2
num2But.grid(row = 1, column = 2)

num3But = Button(top,text = '3',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('3',currentEntry))
num3But['font'] = myFont2
num3But.grid(row = 1, column = 3)

num4But = Button(top,text = '4',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('4',currentEntry))
num4But['font'] = myFont2
num4But.grid(row = 2, column = 1)

num5But = Button(top,text = '5',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('5',currentEntry))
num5But['font'] = myFont2
num5But.grid(row = 2, column = 2)

num6But = Button(top,text = '6',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('6',currentEntry))
num6But['font'] = myFont2
num6But.grid(row = 2, column = 3)

num7But = Button(top,text = '7',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('7',currentEntry))
num7But['font'] = myFont2
num7But.grid(row = 3, column = 1)

num8But = Button(top,text = '8',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('8',currentEntry))
num8But['font'] = myFont2
num8But.grid(row = 3, column = 2)

num9But = Button(top,text = '9',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('9',currentEntry))
num9But['font'] = myFont2
num9But.grid(row = 3, column = 3)

numEnterBut = Button(top,text = '<--',width = 5,height = 2,relief = 'flat',bg = 'brown1')
numEnterBut.bind('<Button-1>',getFunc)
numEnterBut['font'] = myFont2
numEnterBut.grid(row = 4, column = 3)

num0But = Button(top,text = '0',width = 5,height = 2,relief = 'flat',bg = 'white',command = lambda:set_text('0',currentEntry))
num0But['font'] = myFont2
num0But.grid(row = 4, column = 2)

clearBut = Button(top,text = 'C',width = 5,height = 2,relief = 'flat',bg = 'white')
clearBut['font'] = myFont2
clearBut.grid(row = 4, column = 1)




top.resizable(False,False)
top.mainloop()
