def show_info(x):
    print(f'Сумма: {sum(x)}')
    print(f'Среднее арифметическое: {sum(x) / len(x)}')
    print(f'Максимальное значение: {max(x)}')
    print(f'Минимальное значение: {min(x)}')

# numbers = []
# for i in range(10):
#     num = int(input())
#     numbers.append(num)
# show_info(numbers)

numbers_1 = [2, 4, 3]
show_info(numbers_1)

def sum_digits(num):
    summa = 0
    while num > 0:
        summa += num % 10 # summa = summa + num % 10
        num = num // 10
    return summa
    

sum_1 = sum_digits(123)
print(sum_1)

def send_hello():
    print('Добрый день, пользователь!')
    print('Хорошего вам дня!')

send_hello()


def circle_area(rad=1):
    pi = 3.14
    return pi * rad**2

result = circle_area(3)
print(result)

def F(n):
    if n == 1:
        return 1
    else:
        return 10 - F(n-1)
print(F(5))
print(F(6))
print(F(3))