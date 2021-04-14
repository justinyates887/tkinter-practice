from tkinter import *

root = Tk()

#We can create functions to run on b utton click
def myClick():
    myLabel = Label(root, text='I clicked a button O.o')
    myLabel.pack()

#Buttons have a lot of customization, such as padding, foreground color(fg), background color(bg), and state (disabled)
#functions called in command are called without parenthesis
myButton = Button(root, text="Click me!", padx=15, pady=5, command=myClick, bg='#0BB5FF', fg='white')
myButton.pack()

root.mainloop()