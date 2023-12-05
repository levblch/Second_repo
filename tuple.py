# objects_tuple = tuple()
# print(type(objects_tuple))

# objects_tuple = (1, 2, 3)
# print(type(objects_tuple))

objects_tuple = tuple([1, 2, 3, 1])
print(objects_tuple)

first_elem = objects_tuple[0]
print(first_elem)

# objects_tuple[0] = 5

# first, second, third = objects_tuple
# print(first, second, third)
# print(second)

# first, second, third, fourth = objects_tuple
# print(first, second, third, fourth)

for elem in objects_tuple:
    print(elem)

print(objects_tuple.count(1))
print(objects_tuple.index(1))
print(len(objects_tuple))

print('-'*15)

first_tuple = (1, 2)
second_tuple = (3, 4)
third_tuple = first_tuple + second_tuple
print(third_tuple)

sliced_tuple = first_tuple[1:] + second_tuple[1:]
print(sliced_tuple)

print('-'*15)

def func(a, b, c):
    summa = a + b + c
    difference = a - b - c

    return(summa, difference)
objects_tuple = (1, 2, 3)
result = func(*objects_tuple)
print(type(result))
print(result)
summa, difference = func(*objects_tuple)
print(summa, difference)

print('-'*15)

empty_tuple = tuple()
if empty_tuple:
    print('Кортеж не пустой')
else:
    print('Кортеж пустой')

empty_tuple = (1,)
if empty_tuple:
    print('Кортеж не пустой')
else:
    print('Кортеж пустой')

tuple_with_list = ([1, 2, 3], [4, 5, 6])
tuple_with_list[0].append(4)
print(tuple_with_list)
tuple_with_list[0].remove(4)
print(tuple_with_list)
first_list = tuple_with_list[0]
print(first_list)
for i in range(10):
    first_list.append(i)
print(tuple_with_list)

tuple_with_list[0].append(20)
print(tuple_with_list)
print(first_list)


print('-'*15)

import sys
objects_list = []
for i in range(10000000):
    objects_list.append(i)
print(sys.getsizeof(objects_list))

objects_tuple = tuple(objects_list)
print(sys.getsizeof(objects_tuple))