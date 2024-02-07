class Car:
    def __init__(self, color, model, speed=0):
        self.color = color
        self._speed = speed
        self.__model = model
    
    def show_info (self):
        print(f'Цвет: {self.color}')
        print(f'Текущая скорость: {self._speed}')
        print(f'Модель: {self.__model}')

    def get_model(self):
        return self.__model
    
    def set_speed(self, new_speed):
        if new_speed > 0:
            self._speed = new_speed
        else:
            print('Скорость не может быть отрицательной!')

    def get_speed(self):
        return self._speed
    

    
my_car = Car(color='Синий', speed=10, model='Skyline')
my_car.show_info()

print(my_car.color)
print(my_car._speed)
print(my_car._Car__model)
my_car._Car__model = 'Solaris'
print(my_car._Car__model)

print(my_car.get_model())

my_car.set_speed(-100)
print(my_car.get_speed())