from tkinter import *

#To use images, you need a new library
from PIL import ImageTk,Image

root = Tk()
root.title('Icon')

#This is how you set the window for the icon
root.iconbitmap('D:/Digital Image Finished (Operations File)/Icons/Double-Waves-Logo.ico')

#utilizing Pillow to add an image
my_img = ImageTk.PhotoImage(Image.open('D:/Digital Image Finished (Operations File)/Letterhead 2.0.png'))
label = Label(image=my_img)
label.pack()

#This is how you set the close button. root.quit is a built in function with tkinter
button_cancel = Button(root, text='Close', bg='red', fg='white', command=root.quit)
button_cancel.pack()

root.mainloop()