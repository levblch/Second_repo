class BaseHuman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Привет, меня зовут {self.name}')
        print(f'Мой возраст: {self.age}')

    def walk(self):
        print(f'{self.name} идет на прогулку')

class Programmer(BaseHuman):
    def coding(self):
        print(f'Программист {self.name} сейчас пишет код!')
    
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.lenguage = language

class BackendProgrammer(Programmer):
    pass

human = BaseHuman(name='Миша', age=25)
proger = Programmer(name='Дима', age=26, language='Python')
human.introduce()
proger.introduce()
print(human.__dict__)
print(proger.__dict__)
proger.coding()
# human.coding()
backproger = BackendProgrammer(name='Иван', age=27, language='C++')
print(backproger.__dict__)
backproger.walk()

print(issubclass(BackendProgrammer, Programmer))
print(issubclass(BackendProgrammer, BaseHuman))
print(Programmer.__base__)
print(BaseHuman.__base__)

print(issubclass(Programmer, object))
print(issubclass(BackendProgrammer, object))

print(isinstance(proger, Programmer))
print(isinstance(proger, BaseHuman))