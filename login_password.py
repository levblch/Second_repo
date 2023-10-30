login = "Max"
password = "123456!"
login_input = input("Введите логин: ")
password_input = input("Ввeдите пароль: ")
if login_input != login and password_input != password:
    print("Доступ запрещен - логин и пароль неверные!")
elif login_input != login:
    print("Неверный логин!")
elif password_input != password:
    print("Неверный пароль!")
else:
    print("Добро пожаловать!")
