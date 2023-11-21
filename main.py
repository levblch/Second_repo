# file = open('file.txt')
# print(file)
# data = file.readlines()
# print(data)
# file.close()

# file = open('file.txt', encoding='UTF-8')
# data = file.readline()
# print(data)
# for line in file:
#     print(line)

# summa = 0
# for num in file:
#     summa += int(num) # summa = summa + num
# print(summa)

# numbers = []
# for num in file:
#     numbers.append(int(num))
# print(sum(numbers))

# file = open('file.txt', mode='w')
# file.write('Hello, world!')

# file = open('file.txt', mode='a')
# file.write('Привет, мир!')
# file.write('\nДобрый день!')

# file = open('nums.txt', mode='w')
# for num in range(1,21):
#     file.write(f'{num}\n')
# file.close()

from random import randint
file = open('rand_nums.txt', mode='w+')
N = randint(10, 100)
for num in range(N):
    file.write(f'{randint(1, 100)}\n')

# file = open('rand_nums.txt')
file.seek(0)
numbers = []
for num in file:
    numbers.append(int(num))
print(max(numbers) + min(numbers))


