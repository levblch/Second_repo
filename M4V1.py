import json

# human = {
#     'name': 'Dima',
#     'age': 18,
#     'city': 'Moscow'
# }

# human = {
#     'имя': 'Дима',
#     'возраст': 18,
#     'город': 'Москва'
# }

# human_json = json.dumps(human, ensure_ascii=False)
# print(human_json)

# file = open('human.json', 'w', encoding='utf-8')
# json.dump(human, file, ensure_ascii=False, indent=4)
# print(human_json)
# print(json.loads(human_json))

# file = open('human.json', encoding='utf-8')
# human_data = json.load(file)
# print(human_data)

file = open('example.json', encoding='utf-8')
example_data = json.load(file)
# print(type(example_data))
if example_data['isFullTime'] == True and len(example_data['progLanguages']) >=2:
    print('Проходит на 1 этап')
else:
    print('Не проходит на 1 этап')