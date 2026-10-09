from tkinter import *

def pipes_calc():
    #frame1.update_idletasks()
    global pip_btn
    global belt_btn
    pip_btn = True
    belt_btn = False
    title_trd.pack_forget()
    time_round_duration_input.pack_forget()
    title1_belt.pack_forget()
    stack_belt_input.pack_forget()
    title_pipes.pack()
    capacity_pipes_input.pack()
    title2_belt.pack_forget()
    capacity_belt_input.pack_forget()
    title_trd.pack()
    time_round_duration_input.pack()

def belt_calc():
    #frame1.update_idletasks()
    global pip_btn
    global belt_btn
    pip_btn = False
    belt_btn = True
    title_trd.pack_forget()
    time_round_duration_input.pack_forget()
    title_pipes.pack_forget()
    capacity_pipes_input.pack_forget()
    title2_belt.pack()
    capacity_belt_input.pack()
    title1_belt.pack()
    stack_belt_input.pack()
    title_trd.pack()
    time_round_duration_input.pack()

def result_window():
    title_result_trd.pack_forget()
    title_result_trd.pack()
    result_calc()

def result_calc():
    global pip_btn
    global belt_btn
    global result
    if belt_btn == True:
        stack_belt = int(stack_belt_input.get())
        capacity_belt = int(capacity_belt_input.get())
        time_round_duration = int(time_round_duration_input.get()) # в секундах
        storage = 32 * stack_belt
        trd = round(time_round_duration / 60,2)
        ttf = round(storage / capacity_belt,2)
        result = min(trd/ttf,1)*(storage/trd)
        #print(stack_belt, capacity_belt, time_round_duration)
        #print(storage,ttf,trd,result)
        title_result_trd['text'] = f'{result}'
    if pip_btn == True:
        capacity_pipes = int(capacity_pipes_input.get())
        storage = 2400
        time_round_duration = int(time_round_duration_input.get())  # в секундах
        ttf = round(storage / capacity_pipes,2)
        trd = round(time_round_duration / 60,2)
        result = min(trd / ttf, 1) * (storage / trd)
        print(capacity_pipes, time_round_duration)
        print(storage,ttf,trd,result)
        title_result_trd['text'] = f'{result}'

root = Tk()

root.title("Калькулятор пропускной способности")
root.geometry("400x300")
root.resizable(width=False, height=False)

canvas = Canvas(root, width=500, height=400)
canvas.pack()

pip_btn = False
belt_btn = False

frame1 = Frame(root, bg="gray")
frame2 = Frame(root, bg="gray")
frame3 = Frame(root, bg="gray")
frame4 = Frame(root, bg="gray")
frame5 = Frame(root, bg="gray")
frame1.place(relx=0.05, rely=0.05,relwidth=0.45, relheight=0.41)
frame2.place(relx=0.6, rely=0.05,relwidth=0.3, relheight=0.41)
frame3.place(relx=0.4, rely=0.52, relwidth=0.5, relheight=0.2)
frame4.place(relx=0.05, rely=0.52, relwidth=0.32, relheight=0.2)
frame5.place(relx=0.05, rely=0.75, relwidth=0.85, relheight=0.2)

img = PhotoImage(file="satisfctory_pic.png")
image = Label(frame5, image=img)
image.pack()

# окно ввода предмета
title1_belt = Label(frame1, text="Размер стака", bg="gray")
stack_belt_input = Entry(frame1, width=20, bg="gray")
title2_belt = Label(frame1, text="Пропускная способность(п/м)", bg="gray")
capacity_belt_input = Entry(frame1, width=20, bg="gray")

# окно ввода жидкости
title_pipes = Label(frame1,text="Пропускная способность(м3)", bg="gray")
capacity_pipes_input = Entry(frame1, width=20, bg="gray")

# общее для предметов и жидкостей
title_trd = Label(frame1, text='Время круг. маршрута (в сек.)', bg="gray")
time_round_duration_input = Entry(frame1, width=20, bg="gray")

# окно кнопок
belt_button = Button(frame2, text='Конвейеры', command=belt_calc)
belt_button.place(relx=0.21,rely=0.2)
pipes_button = Button(frame2, text='Трубы', command=pipes_calc)
pipes_button.place(relx=0.3,rely=0.5)

# окно вывода
result_button = Button(frame4, text='Показать результат', command=result_window)
result_button.place(relx=0.05,rely=0.25)
title_info = Label(frame3,text='Пропускная способность вагона:', bg="gray")
title_info.pack()
title_result_trd = Label(frame3,text='', bg="white")

root.mainloop()