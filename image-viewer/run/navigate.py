def forward(my_label, button_forward, button_back, image_list):

    global new_label
    new_label = my_label
    global new_button_forward
    new_button_forward = button_forward
    global new_button_back
    new_button_back = button_back

    my_label.grid_forget()
    new_label = Label(image=)

def back():
    return