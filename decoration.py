def decorator(func):
    def wrapper():
        print('Начало работы функции')
        func()
        print('Конец работы функции')
    return wrapper

@decorator
def hello():
    print('Приветствую в своей прграмме')
    

# hello_message = decorator(hello)
# hello_message()

# hello()
#------------------------------------------------

from time import time, sleep

def timer(func):
    def wrapper():
        start_time = time()
        func()
        end_time = time()
        print(f'Время исполнения: {end_time - start_time} секунд.')
    return wrapper

# @timer
# def unfreeze():
#     sleep(10)

# unfreeze()

# @timer
# def get_num():
#     return [i for i in range(1, 10000000)]

# get_num()

def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(10):
            func(*args, **kwargs)
    return wrapper

@repeat
def message(name):
    print(f'Привет!, {name}!')

# message('Ваня')
#---------------------------------------------

def access(func):
    def wraper (*args, **kwargs):
        if kwargs.get('password') == '12345qwerty':
            return f'Доступ разрешен. {func(*args, **kwargs)}'
        else:
            return 'Доступ запрещен. Введен неверный пароль'
    return wraper

@access
def send_message(message, **kwargs):
    return f'Сообщение: {message}'

# user_password = input('Введите пароль: ')
# result = send_message('Очень важное сообщение!', password=user_password)
# print(result)

#-----------------------------------

def up(func):
    def wraper (*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wraper

def warning(func):
    def wraper (*args, **kwargs):
        return f'Вы получили сообщение: {func(*args, **kwargs)}'
    return wraper


@warning
@up
def send_message(gift):
    return f'Мне на день рождения подарили {gift}'

print(send_message('телефон'))