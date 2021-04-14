#tkinter is built into python
from tkinter import *

#To use a widget, or window, you have to declare it from tkinter
root = Tk()

#you can then add a label to the widget
myLabel = Label(root, text='Hello World')

#The pack function is a primitive way to get the widget to appear on screen
myLabel.pack() #Now the window will appear once ran

#Event loops are needed for gui's in order to determine the actions taken by the user on screen
root.mainloop()
