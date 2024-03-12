# from tkinter import *

# window = Tk()
# window.geometry("350x300")

# for c in range(2): window.columnconfigure(index=c, weight=1)
# for r in range(2):
#     window.rowconfigure(index=r, weight=1)

# btn1 = Button(window,text="Кнопка 1", font=('Arial', 15))
# btn1.grid(row=0, column=0)
# btn2 = Button(window,text="Кнопка 2", font=('Arial', 15))
# btn2.grid(row=0, column=1, rowspan=2)
# btn3 = Button(window,text="Кнопка 3", font=('Arial', 15))
# btn3.grid(row=1, column=0)
# # btn3.grid(row=1, column=0, columnspan=2)

# window.mainloop()

from tkinter import *
from random import choice

class Game:
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.moves = ['Камень', 'Ножницы', 'Бумага']
    
    def move_result(self, user_choice):
        comp_choice = choice(self.moves)
        if user_choice == comp_choice:
            self.draw += 1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nНичья'
        elif user_choice == 'Камень' and comp_choice == 'Ножницы' or \
                user_choice == 'Ножницы' and comp_choice == 'Бумага' or \
                user_choice == 'Бумага' and comp_choice == 'Камень':
            self.win += 1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nПобеда'
        else:
            self.lose +=1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nПроигрыш'
        
    def show_info(self):
        return f'Победы: {self.win}\nПроигрыши: {self.lose}\nНичьи: {self.draw}'


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x300')
        self.window.title('Камень, ножницы, бумага')
        self.game = Game()
        self.startUI(self.window)
        self.window.mainloop()

    def startUI(self, window):
        for c in range(3): window.columnconfigure(index=c, weight=1)
        for r in range(3): window.rowconfigure(index=r, weight=1)
        self.btn1 = Button(window,text="Камень", font=('Arial', 15), command=lambda: self.btn_click('Камень'))
        self.btn2 = Button(window,text="Ножницы", font=('Arial', 15), command=lambda: self.btn_click('Ножницы'))
        self.btn3 = Button(window,text="Бумага", font=('Arial', 15), command=lambda: self.btn_click('Бумага'))
        self.btn1.grid(row=2, column=0)
        self.btn2.grid(row=2, column=1)
        self.btn3.grid(row=2, column=2)

        self.lbl = Label(window, text='Начало игры!', font=('Arial', 20))
        self.lbl.grid(row=1, column=0, columnspan=3)

        self.lbl2 = Label(window, justify='left', font=('Arial', 13), text=self.game.show_info())
        self.lbl2.grid(row=0, column=0)

    def btn_click(self, user_choice):
        self.lbl['text'] = self.game.move_result(user_choice)
        self.lbl2['text'] = self.game.show_info() 

app = GUI()           