class Car:
   

    def __init__(self, mark='', model='', color='', speed=0):
        self.mark = mark
        self.model = model
        self.color = color
        self.speed = speed

    def __del__(self):
        print('сработал метод __del__')

    def set_power_engine(self, power_engine):
        self.power_engine = power_engine

    def show_info(self):
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        print(f'Текущая скорость: {self.speed}')

    def get_params(self):
        return (self.mark, self.model, self.color, self.speed)

# my_car_1 = Car()
# my_car_2 = Car()

# # Car.set_power_engine(my_car_1)
# my_car_1.set_power_engine(200)
# print(f'Мощность двигателя: {my_car_1.power_engine}')

# print(my_car_2.__dict__)
# print(my_car_1.__dict__)
# print(Car.__dict__)

# my_car_2.show_info()
# params_car1 = my_car_1.get_params()
# print(params_car1)
    
# my_car_1 = Car()
# print(my_car_1.__dict__)
my_car_1 = Car('Nissan', 'Juke', 'red', 0)
# print(my_car_1.__dict__)
my_car_2 = Car()
# print(my_car_2.__dict__)


class Hero:
    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

    def get_status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Урон: {self.damage}')
        print(f'Защита: {self.defense}')
        print('-------------------------------------')

    def increase_defense(self):
        if self.defense * 1.5 < 100:
            self.defense *= 1.5
        else:
            print('Достигнут максимальный уровень защиты!')
        print(f'Текущий уровень защиты: {self.defense}')
        print('-------------------------------------')

    def make_damage(self, enemy):
        print(f'Атака по персонажу {enemy.name}!')
        print('-------------------------------------')
        enemy.get_damage(self.damage)

    def get_damage(self, damage):
        absorbed_damage = damage * self.defense / 100
        final_damage = damage - absorbed_damage
        print(f'По герою {self.name} нанесли урон {final_damage}!')
        self.health -= final_damage
        print('-------------------------------------')

hero_1 = Hero('Артур', 100, 20, 5)
hero_2 = Hero('Робин', 80, 30, 4)

hero_1.get_status()
hero_1.increase_defense()

hero_2.get_status()
hero_2.make_damage(hero_1)
hero_1.get_status

hero_2.get_status()
hero_2.make_damage(hero_1)
hero_1.get_status

