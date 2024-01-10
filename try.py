# num_1 = int(input())
# num_2 = int(input())
# if num_2 == 0:
#     print('Делить на ноль нельзя!')
# else:
#     print(num_1 / num_2)


# try:
#     num_1 = int(input())
#     num_2 = int(input())
#     result = num_1 / num_2    
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except ValueError:
#     print('Введено некорректное значение!')
# else:
#     print(f'Частное от деления {result}')



# try:
#     num_1 = int(input('Введите первое число:'))
#     num_2 = int(input('Введите второе число:'))
#     result = num_1 % num_2
# except ZeroDivisionError:
#     num_2 = int(input('Делить на ноль нельзя, введите новое число:'))
# except ValueError:
#     print('Введены некорректные значения!')
#     num_1 = int(input('Введите первое число:'))
#     num_2 = int(input('Введите второе число:'))
# else:
#     print(f'Остаток от деления: {result}')
# finally:
#     result = num_1 % num_2
#     print(f'Остаток от деления: {result}')
#     print('Работа программы закончена!')



name = input('Укажите свое имя:')
file = open('log_calc.txt', 'a', encoding='utf-8')
file.write(f'Пользователь: {name}\n')
while True:
    try:
        num_1 = int(input('Введите первое число:'))
        oper = input('Введите операцию (+ - * / ** // %):')
        num_2 = int(input('Введите второе число:'))
        file.write(f'Совершается операция: {num_1}{oper}{num_2}\n')
        result = eval(f'{num_1}{oper}{num_2}')
    except ZeroDivisionError:
        num_2 = int(input('Делить на ноль нельзя, введите новое число:'))
        file.write(f'Ошибка деления на ноль\n')
        file.write(f'Введено новое число: {num_2}\n')
    except ValueError:
        print('Введены некорректные значения!')
        num_1 = int(input('Введите первое число:'))
        num_2 = int(input('Введите второе число:'))
        file.write(f'Ввод некорректных данных\n')
        file.write(f'Введены новые числа: {num_1} и {num_2}\n')
    except SyntaxError:
        oper = input('Введите корректную операцию (+ - * / ** // %):')
        file.write(f'Ввод некорректной операции\n')
        file.write(f'Введена новая операция: {oper}\n')
    finally:
        result = eval(f'{num_1}{oper}{num_2}')
        print(f'Результат операции: {num_1}{oper}{num_2} = {result}')
        file.write(f'Результат: {num_1}{oper}{num_2} = {result}\n')
        is_continue = input('Продолжить работу с калькулятором? (Y/N):')
        if is_continue == 'N':
            print('До свидания!')
            file.write('--------------------------------------\n')
            file.close()
            break
print('--------------------------------')