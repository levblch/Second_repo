class Car:
    mark = 'Toyota'
    model = 'Corolla'
    color = 'blue'
    speed = 0

my_car_1 = Car()
print(my_car_1)
print(type(my_car_1))
my_car_1.color = 'red'
print(f'Марка автомобиля: {my_car_1.mark}')
print(f'Модель автомобиля: {my_car_1.model}')
print(f'Цвет автомобиля: {my_car_1.color}')
print(f'Скорость автомобиля: {my_car_1.speed}')

my_car_2 = Car()
my_car_2.model = 'Tundra'
print(f'Марка автомобиля: {my_car_2.mark}')
print(f'Модель автомобиля: {my_car_2.model}')
print(f'Цвет автомобиля: {my_car_2.color}')
print(f'Скорость автомобиля: {my_car_2.speed}')

class SportCar:
    mark = ''
    model = ''
    engine_power = 0
    max_speed = 0

cars = []
for _ in range(3):
    car = SportCar()
    car.mark = input('Введите марку:')
    car.model = input('Введите модель:')
    car.engine_power = int(input('Введите мощность двигателя:'))
    car.max_speed = int(input('Введите макс. скорость:'))
    cars.append(car)
    print('---------------------')

print('Машины в автопарке:')
for car in cars:
    print(f'Марка: {car.mark}')
    print(f'Модель: {car.model}')
    print(f'Мощность двигателя: {car.engine_power}')
    print(f'Максимальная скорость: {car.max_speed}')
    print('---------------------')


