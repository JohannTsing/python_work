# 在Python中，字典是一系列键值对。每个键都与一个值相关联，你可使用键来访问相关联的值。
# 字典用放在花括号{}中的一系列键值对表示
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
print(f"alien_0 type is: {type(alien_0)}")
# 创建一个空字典
empty_dict = {}
print(empty_dict)
print(f"empty_dict type is: {type(empty_dict)}")

# 访问字典值
print(alien_0['color'])
new_points = alien_0['point']
print(f"You just earned {new_points} points!")
# 使用get()来访问字典值
# 使用“字典名[键名]”这种方式访问字典值时，如果键名不存在，此时将引发错误(KeyError)
# x_position = alien_0['x_position']
# 方法get()的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选的。若没有指定第二个参数且键不存在，此时返回值是None
x_position = alien_0.get('x_position', 'This key dose not exist!')
print(x_position)

# 添加键值对
# 在Python 3.7中，字典中元素的排列顺序与定义时相同。如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值
alien_0['color'] = 'yellow'
print(f"alien_0['color'] = {alien_0['color']}")
# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置为旧位置加上移动距离。
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")

# 删除键值对
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
del alien_0['point']
print(alien_0)

# 类对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# 遍历字典
# 遍历字典中的所有键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for k, v in user_0.items():
    print(f"Key: {k}, Value: {v}")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# items()方法的返回值,返回的是一个视图对象。可以使用list()方法，将这个视图对象转换为列表
user_0_items = user_0.items()
print(f"字典.items(): {user_0_items}")
print(f"字典.items() type is {type(user_0_items)}")
print(f"list(字典.items()): {list(user_0_items)}")

# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(f"{name.title()}")
# 遍历字典时，会默认遍历所有的键。因此，keys()可以省略
for name in favorite_languages:
    print(f"{name.title()}")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
# keys()方法的返回值,返回的是一个视图对象。可以使用list()方法，将这个视图对象转换为列表
favorite_languages_keys = favorite_languages.keys()
print(f"字典.keys(): {favorite_languages_keys}")
print(f"字典.keys() type is {type(favorite_languages_keys)}")
print(f"list(字典.keys()): {list(favorite_languages_keys)}")
if 'erin' not in favorite_languages_keys:
    print("Erin, please take our poll!")

# 按照特定的顺序遍历字典
for name in sorted(favorite_languages_keys):
    print(
        f"{name.title()}'s favorite language is {favorite_languages[name].title()}."
    )

# 遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"{language.title()}")
# values()方法的返回值,返回的是一个视图对象。可以使用list()方法，将这个视图对象转换为列表
favorite_languages_values = favorite_languages.values()
print(f"字典.values(): {favorite_languages_values}")
print(f"字典.values() type is {type(favorite_languages_values)}")
print(f"list(字典.values()): {list(favorite_languages_values)}")

# 如果生成的列表中包含重复项，为剔除重复项，可使用集合（set）。
# 集合中的每个元素都必须是独一无二的
print("The following languages have been mentioned:")
favorite_languages_value_set = set(favorite_languages_values)
for language in favorite_languages_value_set:
    print(language.title())

# 集合
# 可使用一对花括号直接创建集合，并在其中用逗号分隔元素
languages = {'python', 'ruby', 'c', 'python'}
print(languages)
# 如果要创建一个新集合，需要使用set()，而不是{}，{}是创建空字典的
empty_set = set()
print(empty_set)
print(f"empty_set type is: {type(empty_set)}")

# 嵌套
# 在列表中存储字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 生成包含多个外星人的列表
aliens = []
for number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 修改前3个外星人的属性
# FIXME: 为何修改切片的属性，原列表的属性也会一起修改？
# aliens_3 = aliens[:3]
# for alien in aliens_3:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# new_alien = {'color': 'red', 'points': 15, 'speed': 'fast'}
# aliens_3[2] = new_alien
# print(aliens_3)

for number in range(6):
    alien = aliens[number]
    if number < 3:
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif number < 6:
        alien['red'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# 显示前8个外星人
for alien in aliens[:8]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}.")

# 在字典中存储列表
# 存储所点比萨的信息。
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点的比萨。
# 如果字符串过长，可以将字符串分行，python会将这些字符串自动合并
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:"
      "")
for topping in pizza['toppings']:
    print("\t" + topping)

print("\nfavorite_languages practice")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# 在字典中存储字典
print("\n在字典中存储字典")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")