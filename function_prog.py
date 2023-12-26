words = ['четыре', 'восемь', 'пятнадцать', 'восемнадцать']
max_word = ''
for word in words:
    if len(word) > len(max_word):
        max_word = word
print(max_word)

max_word = max(words, key=len)
print(max_word)

def double(num):
    return num * 2
number = double(8)
print(number)

number = lambda num: num * 2
print(number(8))

numbs = ['4', '23', '15', '8']
max_str = '0'
for num in numbs:
    if int(num) > int(max_str):
        max_str = num
print(max_str)

max_str = max([int(num) for num in numbs])
print(max_str)

max_str = max(numbs,key=len)
print(max_str)

max_str = max(numbs,key=lambda num: int(num))
print(max_str)

int_numbs = list(map(int, numbs))
print(int_numbs)

base = [1, 2, 5, 6]
exp = [2, 3, 4, 5]
data = list(map(lambda x, y: x**y, base, exp))
print(data)

words = ['красный', 'синий', 'оранжевый', 'белый']
long_words = list(filter(lambda line: len(line) > 5, words))
print(long_words)

words = ['шалаш', 'кот', 'топот', 'бег']
pal_words = list(filter(lambda word: word == word[::-1], words))
print(pal_words)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
mult = reduce(lambda x, y: x * y, numbers)
print(mult)