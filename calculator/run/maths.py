def add(entry):
    first_number = entry.get()
    global f_num
    global math
    math  = 'addition'
    f_num = int(first_number)
    entry.delete(0)

def sub(entry):
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry.delete(0)

def mult(entry):
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry.delete(0)

def div(entry):
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry.delete(0)

def equal(entry):
    second_number = entry.get()
    entry.delete(0)

    if math == 'addition':
        entry.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        entry.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
        entry.insert(0, f_num * int(second_number))
    elif math == 'division':
        entry.insert(0, f_num / int(second_number))

