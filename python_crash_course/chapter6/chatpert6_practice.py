# 6-1
print("6-1")
johann = {
    'first_name': 'johann',
    'last_name': 'Chao',
    'age': '18',
    'city': 'Bj'
}
print(f"johann info {johann}")

# 6-2
print("\n6-2")
favorite_numbers = {}
favorite_numbers['Johann'] = 1
favorite_numbers['Jessie'] = 2
favorite_numbers['Duke'] = 3
favorite_numbers['Andrew'] = 4
favorite_numbers['Donald'] = 3
print(f"favorite_numbers info {favorite_numbers}")

# 6-3
print("\n6-3")
vocabularys = {}
vocabularys['variable'] = "变量是可以赋给值的标签，也可以说变量指向特定的值。"
vocabularys['number'] = "Python 数字数据类型用于存储数值。包括整数，浮点数和复数。"
vocabularys['string'] = "字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号。"
vocabularys['list'] = "列表由一系列按特定顺序排列的元素组成。"
vocabularys['tuple'] = "Python将不能修改的值称为不可变的，而不可变的列表被称为元组。"
print(f"variable: {vocabularys['variable']}")
print(f"number: {vocabularys['number']}")
print(f"string: {vocabularys['string']}")
print(f"list: {vocabularys['list']}")
print(f"tuple: {vocabularys['tuple']}")

# 6-4
print("\n6-4")
for terminology, definition in vocabularys.items():
    print(f"{terminology}: {definition}")

# 6-5
print("\n6-5")
rivers = {
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Mississippi': 'USA',
    'Nile': 'Egypt',
}
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
for country in sorted(rivers.values()):
    print(country)

# 6-6
print("\n6-6")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
survey_list = ['phil', 'sarah', 'johann', 'jessie', 'jen', 'andrew', 'edward']
favorite_languages_keys = favorite_languages.keys()
for name in survey_list:
    if name in favorite_languages_keys:
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll!")

# 6-7
print("\n6-7")
johann = {
    'first_name': 'johann',
    'last_name': 'Chao',
    'age': '18',
    'city': 'Beijing'
}
jessie = {
    'first_name': 'jessie',
    'last_name': 'Chang',
    'age': '17',
    'city': 'Shanghai'
}
andrew = {
    'first_name': 'andrew',
    'last_name': 'Lee',
    'age': '19',
    'city': 'Chengdu'
}
people = [johann, jessie, andrew]
for user in people:
    print(user)

# 6-8
print("\n6-8")
maomao = {'name': 'maomao', 'species': 'cat', 'master': 'Andrew'}
doudou = {'name': 'doudou', 'species': 'dog', 'master': 'Johann'}
hanhan = {'name': 'hanhan', 'species': 'rabbit', 'master': 'Jessie'}
pets = [maomao, doudou, hanhan]
for pet in pets:
    print(pet)

# 6-9
print("\n6-9")
favorite_places = {}
favorite_places['Johann'] = ['Beijing', 'Shanghai', 'Harbin']
favorite_places['Jessie'] = ['Dali', "Xi'an"]
favorite_places['Andrew'] = ['Lijiang']
for name, palaces in favorite_places.items():
    print(f"{name} favorite palace is ")
    for palace in palaces:
        print(f"\t{palace}")

# 6-10
print("\n6-10")
favorite_numbers = {}
favorite_numbers['Johann'] = [1, 2, 3]
favorite_numbers['Jessie'] = [4, 5, 6, 7]
favorite_numbers['Duke'] = [8]
favorite_numbers['Andrew'] = [9, 10, 11]
favorite_numbers['Donald'] = 12
for name, numbers in favorite_numbers.items():
    print(f"{name} favorite number is ")
    print(type(numbers))
    if isinstance(numbers, (tuple, list)):
        for number in numbers:
            print(f"\t{number}")
    else:
        print(numbers)

# 6-11
print("\n6-11")
cities = {}
beijing = {
    'country': 'China',
    'population': '21843k',
    'fact': 'The capital of China'
}
newDelhi = {
    'country': 'India',
    'population': '25000k',
    'fact': 'The capital of India'
}
washington = {
    'country': 'USA',
    'population': '700k',
    'fact': 'The capital of USA'
}
cities['beijing'] = beijing
cities['newDelhi'] = newDelhi
cities['washington'] = washington
for city, info in cities.items():
    print(f"city: {city}")
    print(f"\tcountry: {info['country']}")
    print(f"\tpopulation: {info['population']}")
    print(f"\tfact: {info['fact']}")
