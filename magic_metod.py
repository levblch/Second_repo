# class Car:
#     def __new__(cls, *args, **kwargs):
#         print(f'Работает метод __new__() для класса {cls}')
#         print(args)
#         print(kwargs)
#         return super().__new__(cls)

#     def __init__(self, color, model, speed):
#         self.color = color
#         self.model = model
#         self.speed = speed

# my_car = Car(color = 'Белый', model = 'Camry', speed = 100)
# print(my_car)
# # print(my_car.__dict__)


class Captain:
    __cap = None
    def __new__(cls, *args, **kwargs):
        if cls.__cap is None:
            cls.__cap = super().__new__(cls)
        return cls.__cap

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

cap = Captain(name='Дима', age=26, height=179, weight=75)
new_cap = Captain(name='Миша', age=25, height=189, weight=82)  
print(cap.__dict__)
print(new_cap.__dict__)     
    
class Car:
    def __init__(self, model):
        self.model = model

    # def __str__(self):
    #     return f'Модель машины - {self.model}'
    
    def __repr__(self):
        return f'Car({self.model})'

my_car = Car('Camry')
print(my_car)
print(repr(my_car))

class MoneyBox:
    def __init__(self, money=0):
        self.__money = money

    def __repr__(self):
        return f'{self.__money}'
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money + other)
        else:
            print('Некорректное сложение')
            
    def __radd__(self, other):
        return self.__add__(other)

box = MoneyBox(123)
box = 10 + box
print(box)