# 条件测试
# 检查是否相等
car = 'audi'
print(car == 'audi')
# 忽略大小写
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')
# 检查是否不等
if (car != 'bmw'):
    print(car)
# 数值比较
age = 18
print(age == 18)
if age != 19:
    print(age)
print(age < 18)
print(age <= 18)
print(age > 18)
print(age >= 18)
# 检查多个条件
age_0 = 18
age_1 = 18
if (age_0 >= 18) and (age_1 >= 18):
    print("both >= 18")
age_1 = 17
if (age_0 >= 18) or (age_1 >= 18):
    print("someone >= 18")
# 包含/不包含在列表
banned_users = ['johann', 'jessie', 'peter']
if 'johann' in banned_users:
    print("'johann' in banned_users")
if 'william' not in banned_users:
    print("'william' not in banned_users")
# 布尔表达式
game_active = True
print(game_active)
boo1_yes = (18 == 18)
print(boo1_yes)
bool_no = (18 != 18)
print(bool_no)

# if语句
age = 18
if age >= 18:
    print("You are old enough to vote.")
    print("Go vote!")
# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote.")
    print("Go vote!")
else:
    print("You are too young to vote.")
    print("Wait until you're eighteen.")
# if-elif-else语句
age = 12
if age <= 6:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $20.")
# 其他写法
if age <= 6:
    price = 0
elif age < 18:
    price = 10
else:
    price = 20
print(f"Your admission cost is ${price}.")
# 使用多个elif
age = 18
if age <= 6:
    price = 0
elif age < 18:
    price = 10
elif age < 22:
    price = 15
else:
    price = 20
print(f"Your age is {age},Your admission cost is ${price}.")
'''
if-elif-else结构，遇到通过了的测试后，Python就跳过余下的测试。
总之，如果只想执行一个代码块，就使用if-elif-else结构；如果要执行多个代码块，就使用一系列独立的if语句。
'''
requested_toppings = ['mushrooms', 'extra cheese']
# 多个独立的if语句，执行多个代码块
print("\n多个独立的if语句，执行多个代码块")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")
# if-elif-else结构，执行一个代码块
print("\nif-elif-else结构，执行一个代码块")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!\n")

# 使用if语句处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry,we are out of green peppers right now.')
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!\n")

# 判断列表是否为空
# XXX: 在if语句中将列表名用作条件表达式时，Python将在列表至少包含一个元素时返回True，并在列表为空时返回False。
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?\n")

# 使用多个列表
available_toppings = [
    'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
    'extra cheese'
]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
print("Finished making your pizza!\n")