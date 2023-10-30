# Объявление строки

# string = 'строка'
# another_string = "еще одна строка 123"

# for i in range(10):
#     print(f'Элемент i = {i} следующий')


# Метод split()
 
# syms = input()
# syms_list = syms.split(', ')
# print(syms_list)
# print(f'Количество символов в строке за исключением запятых:{len(syms_list)}')


# Метод replace()

# syms = input()
# cleaned_syms = syms.replace(' ',',')
# print(cleaned_syms)
# print(f'Количество символов в строке за исключением пробелов:{len(cleaned_syms)}')

# hello_word = ['Привет','мир!']
# list_to_str = ' '.join(hello_word)
# print(list_to_str)

# string = 'abacaba'
# print(f'Количество символов a: {string.count("a")}')
# print(string.count('aba'))


# print('привет' == 'Привет')

# city = input()
# if city.lower() == 'москва':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Москве : (')


# city = input()
# if city.upper() == 'МОСКВА':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Москве : (')

# city = input()
# if city.capitalize() == 'Москва':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Москве : (')

# city = input()
# if city.title() == 'Нижний Новгород':
#     print('Мы готовы вас обслужить!')
# else:
#     print('Мы делаем доставку только по Нижнему : (')

# string = 'abcdefg'
# print(string[0])
# print(string[-1])
# print(string[1:6])
# print(string[1:])
# print(string[1:6:2])
# print(string[6:1:-1])

# string = 'Нижний Новгород'
# if 'Новгород' in string:
#     print('Такая строка там есть.')
# else:
#     print('Такой строки там нет.')

for sym in 'year2023':
    if sym.isdigit():
        print(sym)