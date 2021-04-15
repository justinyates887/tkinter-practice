from tkinter import *
from navigate import *

#To use images, you need a new library
from PIL import ImageTk,Image

root = Tk()
root.title('Icon')

#This is how you set the window for the icon
root.iconbitmap('D:/Digital Image Finished (Operations File)/Icons/Double-Waves-Logo.ico')

#utilizing Pillow to add an image
my_img1 = ImageTk.PhotoImage(Image.open('images/Presentation Folder Concept 2.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/Logo Art Concept 1.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/PostcardConcept1.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/Icon.png'))
my_img5 = ImageTk.PhotoImage(Image.open('images/Letterhead 2.0.png'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

label = Label(image=my_img1)
label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<" command=lambda: back())
button_cancel = Button(root, text='Close', bg='red', fg='white', command=root.quit)
button_forward = Button(root, text='>>' command=lambda: forward(my_label, button_forward, button_back, image_list))

button_back.grid(row=1, column=0)
button_cancel.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()