input_1 = input("Введите первое число: ")
input_2 = input("Введите второе число: ")

if input_1.isnumeric() and input_2.isnumeric():
    number_1 = int(input_1)
    number_2 = int(input_2)
    oper = input("Введите знак операции: ")
    if oper == "+":
        result = number_1 + number_2
        print("Сумма: " + str(result))
    elif oper == "-":
        result = number_1 - number_2
        print("Разность: " + str(result))
    elif oper == "*":
        result = number_1 * number_2
        print("Произведение: " + str(result))
    elif oper == "/":
        if number_2 != 0:
            result = number_1 / number_2
            print("Обычное деление: " + str(result))
        else:
            print("Деление на ноль!")
    elif oper == "//":
        if number_2 != 0:
            result = number_1 // number_2
            print("Деление с получением целой части: " + str(result))
        else:
            print("Деление на ноль!")
    elif oper == "%":
        if number_2 != 0:
            result = number_1 % number_2
            print("Деление с получением остатка: " + str(result))
        else:
            print("Деление на ноль!")
    elif oper == "**":
        result = number_1 ** number_2
        print("Возведение числа в степень: " + str(result))
    else:
        print("Неизвестный знак опреации!")
else:
    print("Некорректные операнды!")

    