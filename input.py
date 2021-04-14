from tkinter import *

root = Tk()

#Input widgets are called entry widgets, for entering data
#They can also be customized with a variety of options
entry = Entry(root, width=50, bg='#E5E1E6', fg='black', borderwidth=3)
entry.pack()

#If we want a default value, we can use the insert() function
entry.insert(0, 'Hello World!')

def myClick():
    #To use the entered data, use the get() function
    data = entry.get()

    #We can then use this data
    myLabel = Label(root, text='Data: ' + data)
    myLabel.pack()

#Buttons have a lot of customization, such as padding, foreground color(fg), background color(bg), and state (disabled)
#functions called in command are called without parenthesis
myButton = Button(root, text="Print Data", padx=15, pady=5, command=myClick, bg='#0BB5FF', fg='white')
myButton.pack()

root.mainloop()