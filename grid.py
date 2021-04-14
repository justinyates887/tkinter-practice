#tkinter is built into python
from tkinter import *

#To use a widget, or window, you have to declare it from tkinter
root = Tk()

#you can then add a label to the widget
myLabel = Label(root, text='Hello World')
myLabelTwo = Label(root, text="My name is Justin")

#As python is OO, you can make the grid call on the Label declaration as such:
myLabelThree = Label(root, text="I am 23").grid(row=2, column=0)

#Instead of using pack(), you can utilize a grid system to specify positioning
#You can specify rows and columns for absolute positioning of elements
myLabel.grid(row=0, column=0)
myLabelTwo.grid(row=1, column=0)

#Important note: Columns and rows are relative. This means that if you have col 0 and col 5, but no 1-4, there will not be gaps in the columns.

#Event loops are needed for gui's in order to determine the actions taken by the user on screen
root.mainloop()
