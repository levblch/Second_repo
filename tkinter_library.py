from tkinter import *
window = Tk()
window.title('Анкета')
window.geometry('700x500')

def check():
    print(name.get(), selected.get(), age.get(), check_state.get())
    label.configure(text=f'Спасибо, {name.get()}')
    label['text'] = f'Спасибо, {name.get()}'

label = Label(text='Расскажите о себе', font=('Arial', 20))
label.place(x=230,y=10)

about = Message(text='Мы рады приветствовать вас в нашей анкете дружбы! Пожалуйста, отвечайте на вопросы честно, вся информация останется между нами.', font=('Arial', 14), width=680)
about.configure(justify=CENTER)
about.place(x=5, y=70)

name = Entry(width=30)
name.place(x=70, y=155)

label_name = Label(text='ФИО: ', font=('Arial', 15))
label_name.place(x=5, y=150)

selected = IntVar()
rad1 = Radiobutton(text='Мужской', value=1, variable=selected)
rad2 = Radiobutton(text='Женский', value=2, variable=selected)
rad1.place(x=10, y=200)
rad2.place(x=100, y=200)

label_age = Label(text='Сколько вам лет?', font=('Arial', 15))
label_age.place(x=5,y=250)

age = Spinbox(from_=0, to=100, width=20)
age.place(x=10, y=300)

check_state = IntVar()
check_btn = Checkbutton(text='Запомнить меня', variable=check_state)
check_btn.place(x=10, y=350)

btn = Button(text='Отправить', font=('Arial', 10), bg='green', command=check)
btn.place(x=10, y=400)

window.mainloop()

