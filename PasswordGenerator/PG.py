from tkinter import *
from tkinter import ttk
import random


window = Tk()
window.resizable(False , False)
window.title('Password Generator')
window.geometry('300x200')
window.iconbitmap('PG.ico')

length = IntVar()
lbl = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()


Alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
Numbers = '1234567890'
Symbols = '-=;:/!@#$%&*()^_+~?'


# showpass label
showpass = ttk.Label(window , font = ('arial' ,15) , foreground = '#CE00FF' , textvariable = lbl ).pack()


# combobox
ttk.Label(window , text = 'Password Lentgh:').pack()
numchoosen = ttk.Combobox(window, width = 12 , textvariable = length)
numchoosen['values'] = (5,6,7,8,9,10)
numchoosen.pack()
numchoosen.current(2)
numchoosen.config(state = 'readonly')


# functions
def randalp():
        string = list(Alphabet)
        random.shuffle(string)
        return ''.join(string[:length.get()])


def randnum():
        string = list(Numbers)
        random.shuffle(string)
        return ''.join(string[:length.get()])


def randsym():
        string = list(Symbols)
        random.shuffle(string)
        return ''.join(string[:length.get()])
            
def randan():
        string = list(Alphabet) + list(Numbers)
        random.shuffle(string)
        return ''.join(string[:length.get()])


def randas():
        string = list(Alphabet) + list(Symbols)
        random.shuffle(string)
        return ''.join(string[:length.get()])


def randns():
        string = list(Numbers) + list(Symbols)
        random.shuffle(string)
        return ''.join(string[:length.get()])

def randans():
        string = list(Alphabet) + list(Numbers) + list(Symbols)
        random.shuffle(string)
        return ''.join(string[:length.get()])


# checkbuttons
rad1 = ttk.Checkbutton(window , text = 'Alphabet' , variable = var1).pack()
rad2 = ttk.Checkbutton(window , text = 'Numbers' , variable = var2).pack()
rad3 = ttk.Checkbutton(window , text = 'Symbols' , variable = var3).pack()


def genbtn():
        get1 = var1.get()
        get2 = var2.get()
        get3 = var3.get()
        if get1 == '1':
                lbl.set(randalp())
        if get2 == '1':
                lbl.set(randnum())
        if get3 == '1':
                lbl.set(randsym())
        if get1 == '1' and get2 == '1':
                lbl.set(randan())
        if get1 == '1' and get3 == '1' :
                lbl.set(randas())
        if get2 == '1' and get3 == '1':
                lbl.set(randns())
        if get1 == '1' and get2 == '1' and get3 == '1':
                lbl.set(randans())


def copybtn():
        window.clipboard_clear()
        window.clipboard_append(lbl.get())


# buttons
ttk.Button(window , text = 'Generate' , command = genbtn).pack()
ttk.Button(window , text = 'Copy' , command = copybtn).pack()


window.mainloop()