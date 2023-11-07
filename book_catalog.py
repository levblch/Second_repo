catalog = {}
while True:
    print('Список возможных действий:')
    print('1 - Добавить новую книгу')
    print('2 - Поиск книги по названию')
    print('3 - Удаление книги из каталога')
    print('4 - Показать информацию о всех книгах в каталоге')
    print('0 - Закончить работу')
    user_choice = int(input('Выберите действие: '))
    if user_choice == 0:
        print('До свидания!')
        break
    elif user_choice == 1:
        title = input('Введите название книги: ')
        while title in catalog:
            title = input('Такая книга уже есть, введите другое название')
        author = input('Введите имя автора: ')
        catalog[title] = author
    elif user_choice == 2:
        title = input('Введите название книги: ')
        if title in catalog:
            print('Информация о книге:')
            print('Название', title)
            print('Автор', catalog[title])
        else:
            print('Книга не найдена')
    elif user_choice == 3:
        title = input('Введите название книги: ')
        if title in catalog:
            del catalog[title]
            print('Книга удалена.')
        else:
            print('Книга не найдена')
    elif user_choice == 4:
        print('Информация о книгах в каталоге:')
        for book in catalog:
            print(f'Название: {book}, Автор: {catalog[book]}')
    else:
        print('Неверное действие. Попробуйте еще раз: ')
    print('-'*25)
