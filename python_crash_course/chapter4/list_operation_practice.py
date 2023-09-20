# 使用 for循环来遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # 每行缩进的代码，都是for循环的一部分
    # print(magician)
    print(f"{magician.title()}, that is a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}. \n")
# 未缩进的代码，不包含在for循环内
print("Thank you,everyone. That was a great magic show!")

# 数值列表
# 使用 range() 函数生成一系列数，前闭后开
for num in range(1, 5):
    print(num)
# range() 函数还可以设置步长
for num in range(1, 10, 2):
    print(f"奇数: {num}")
# 使用 list() 函数将 range() 的结果转换为列表
numbers = list(range(1, 10, 2))
print(numbers)
# 获取10以内各数的平方列表
squares = []
for num in range(1, 11):
    squares.append(num**2)
print(squares)
# 数字列表的简单统计函数
numbers = list(range(1, 11, 1))
print(numbers)
min_num = min(numbers)
max_num = max(numbers)
sum_num = sum(numbers)
print(f"min: {min_num}")
print(f"max: {max_num}")
print(f"sum: {sum_num}")

# 列表解析
doubles = [num * 2 for num in range(1, 11)]
print(doubles)
squares = [num**2 for num in range(1, 11)]
print(squares)

# 处理列表的部分元素
# 获取切片 列表[start:end],前闭后开
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"初始列表: {players}")
players_section = players[0:3]
print(f"获取切片[0:3]: {players_section}")
# 若没有指定 start索引，则从0开始
players_section = players[:2]
print(f"获取切片[:2]: {players_section}")
# 若没有指定 end索引，则一直到列表末尾
players_section = players[2:]
print(f"获取切片[2:]: {players_section}")
# 索引支持负数
players_section = players[1:-2]
print(f"获取切片[1:-2]: {players_section}")
# 获取切片时，支持步长 列表(start:end:步长)
players_section = players[0::2]
print(f"获取切片[0::2]: {players_section}")
# 遍历切片
for player in players[0::2]:
    print(f"\t{player}")

# 复制列表副本
my_foods = ['pizza', 'falafel', 'carrot cake']
# 此处注意二者的区别：前者是将friend_foods变量指向同一个列表，后者是将friend_foods变量指向一个新的列表
# friend_foods = my_foods
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"My favorite foods are: \n{my_foods}")
print(f"My friend's favorite foods are: \n{friend_foods}")

# 元组，即内部元素不可变的列表
# 元组的定义与访问
seasons = ('spring', 'summer', 'autumn', 'winter')
print(seasons[2])
for season in seasons:
    print(f"season: {season}")
'''
严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
'''
my_tuple = (1, )
# 元组内的元素，不可修改
# 'tuple' object does not support item assignment 元组不支持对单个元素赋值
# seasons[2] = 'fall'
# 元组变量可以被重新赋值，即这个这个元组变量(标签)可以指向其他的元组
seasons = ('spring', 'summer', 'fall', 'winter')
print(seasons)