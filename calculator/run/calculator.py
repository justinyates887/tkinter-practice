from tkinter import * 
from populate import populate
from clear import clear
from maths import *

#Root window
root = Tk()
root.title('Simple Calculator')

#Inpput field
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: populate(entry, 1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: populate(entry, 2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: populate(entry, 3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: populate(entry, 4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: populate(entry, 5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: populate(entry, 6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: populate(entry, 7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: populate(entry, 8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: populate(entry, 9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: populate(entry, 0))

button_add = Button(root, text='+', padx=40, pady=20, bg='#616161', fg='white', command=lambda: add(entry))
button_subtract = Button(root, text='-', padx=40, pady=20, bg='#616161', fg='white', command=lambda: sub(entry))
button_divide = Button(root, text='/', padx=40, pady=20, bg='#616161', fg='white', command=lambda: div(entry))
button_multiply = Button(root, text='*', padx=40, pady=20, bg='#616161', fg='white', command=lambda: mult(entry))
button_equals = Button(root, text='=', padx=86, pady=20, bg='#3377FF', fg='white',  command=lambda: equal(entry))
button_clear = Button(root, text='C', padx=40, pady=120, bg='#E67300', fg='white', command=lambda: clear(entry))

#Put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)

button_divide.grid(row=5, column=2)
button_multiply.grid(row=5, column=3)

button_equals.grid(row=4, column=1, columnspan=2)

button_clear.grid(row=1,column=3, rowspan=4)

#Loop until end
root.mainloop()