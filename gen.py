# numbers =[]
# for num in range(1, 101):
#     numbers.append(num)
# print(numbers)

# numbers = [num for num in range(1, 101)]
# print(numbers)

# 1
# N = int(input())
# squares = [num**2 for num in range(1, int(input()) +1)]
# print([num**2 for num in range(1, int(input()) +1)])

# 2
# line = input()
# symbols = [sym for sym in input()]
# print(symbols)

# 3
# numbers = [num for num in range(100, 1001) if num % 7 == 0]
# print(numbers)

# 4
cities = ['Самара', 'Москва', 'Анапа', 'Новосибирск', 'Архангельск', 'Екатеринбург', 'Александровск']
new_cities = [city for city in cities if city[0] == 'А' and len(city) >= 7]
print(new_cities)

# 5
uniq_cities = [city for city in cities if len(city) == len(set(city.lower()))]
print(uniq_cities)

# 6
# from math import scrt
from pprint import pprint
square_roots = {}
for num in range(1, 21):
    square_roots[num] = num**0.5 # sqrt(num)
pprint(square_roots)

square_roots = {num:num**0.5 for num in range(1, 21) if num % 2 == 0}
pprint(square_roots)

# 7
fruits = {
    'Персики': 150,
    'Яблоки': 100,
    'Бананы': 140,
    'Лимоны': 200,
    'Авокадо': 450
}
fruits_new = {fruit:price * 1.2 for fruit, price in fruits.items()}
pprint(fruits_new)

# 8

# N = int(input())
# table = []
# for i in range(1, N + 1):
#     line = []
#     for j in range(1, N+1):
#         line.append(i * j)
#     table.append(line)
# for line in table:
#     print(line)

# N = int(input())
# table = [[i * j for j in range(1, N+1)] for i in range(1, N + 1)]
# print(table)

# 9
from time import time
def get_divisors(n):
    divisors = []
    for div in range(2, n // 2 +1):
        if n % div == 0:
            divisors.append(div)
    return divisors

N, M = int(input()), int(input())
start = time()
nums_and_divs = {num:get_divisors(num) for num in range(N, M + 1) if len(get_divisors(num)) > 0}
stop = time()
print(f'Программа работала {stop - start} секунд')
# print(nums_and_divs)
