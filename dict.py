english_dict = {
    'apple':'яблоко',
    'milk':'молоко',
    'cat':'кот',
}
# print(english_dict)
# print(english_dict['cat'])

# word = input('Введите слово на английском языке:')
# print('Перевод слова ' + word + ' на русском - ' + str(english_dict.get(word)))
# if word in english_dict:
#     print('Перевод слова ' + word + ' на русском - ' + english_dict[word])
# else:
#     print('Такого слова в словаре нет')

english_dict['spring'] = 'весна'
english_dict.update({'spring':'весна, пружина, скачок, источник'})
english_dict.update({'table':'стол'})
# del english_dict['table']
# world_pop = english_dict.pop('milk')
# english_dict.popitem()
english_dict['thing'] = 'вещь'
english_dict['thing'] = 'обстоятельство'
english_dict['thing'] = 'ситуация'
# print(english_dict)
# print(world_pop)

# print(len(english_dict))
# print(f'Английские слова: {english_dict.keys()}')
# print(f'Русские слова: {english_dict.values()}')
# print(f'Все пары ключ-значение: {english_dict.items()}')
print(english_dict)
english_dict_copy = english_dict.copy()

english_dict_copy.clear()
print(english_dict_copy)