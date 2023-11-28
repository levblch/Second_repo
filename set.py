# my_set = set()
# my_set2 = {1, 2, 3}
# print(type(my_set2))
# my_set.add(1)
# my_set.add(2)
# my_set.add(3)
# print(my_set)

# my_set.discard(1)
# my_set.discard(2)
# my_set.discard(3)
# print(my_set)

# for i in range(100):
#     my_set.add(i)
# print(my_set)

# my_set.clear()
# print(my_set)

# my_set = {1, 2, 3}
# # print(my_set[0])
# # my_set.add([4, 5])

# my_grades = {3, 4, 5}
# your_grades = {2, 4, 5}
# print(my_grades.intersection(your_grades))
# print(my_grades.union(your_grades))
# print(my_grades.difference(your_grades))
# print('-'*15)
# my_grades.intersection_update(your_grades)
# print(my_grades)

# my_grades.difference_update(your_grades)
# print(my_grades)

# my_grades.update(your_grades)
# print(my_grades)


my_list = [1, 2, 1, 3, 4, 2, 4]
for i in set(my_list):
    print(i)

str1 = 'I love cats'
str2 = 'c a t s'
if set(str2).issubset(str1):
    print('Да, является')
else:
    print('Не является')

if set(str1).issuperset(str2):
    print('Да, является')
else:
    print('Не является')


n = int(input())
result = set()
for i in range(1,n + 1):
    result.add(i)
while True:
    ask = input()
    if ask == 'HELP':
        print(result)
        break
    else:
        ask_set = set()
        for elem in ask.split():
            ask_set.add(int(elem))
    answer = input()
    if answer == 'YES':
        result.intersection_update(ask_set)
    if answer == 'NO':
        result.difference_update(ask_set)