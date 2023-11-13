def show_info(lst):
    print(f'Сумма: {sum(lst)}')
    print(f'Среднее арифметическое: {sum(lst) / len(lst)}')
    print(f'Максимально значение: {max(lst)}')
    print(f'Минимальное значение: {min(lst)}')



# numbers = []
# for i in range(10):
#     num = int(input())
#     numbers.append(num)
# # print(f'Сумма: {sum(numbers)}')
# # print(f'Среднее арифметическое: {sum(numbers) / len(numbers)}')
# # print(f'Максимально значение: {max(numbers)}')
# # print(f'Минимальное значение: {min(numbers)}')
# show_info(numbers)
# numbers_1 = [1, 2, 3, 45 ,234, 7]
# show_info(numbers_1)

def sum_digits(num):
    summa = 0
    while num > 0:
        summa = summa + num % 10
        num = num // 10
    return summa

sum_1 = sum_digits(123)
print(sum_1)

def send_hello():
    print('Добрый день пользователь!')
    print('Хорошего вам дня!')

send_hello()

def circle_area(rad=1):
    pi = 3.14
    return pi*rad**2

result = circle_area(14)
print(result)

def F(n):
    if n == 1:
        return 1
    else:
        return 10 - F(n-1)
    
print(F(5))