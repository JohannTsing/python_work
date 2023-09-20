# 5-1
print("5-1")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
animal = 'lion'
print("Is animal == 'lion'? I predict True.")
print(animal == 'lion')
print("Is animal == 'tiger'? I predict False.")
print(animal == 'tiger')

# 5-2
print("\n5-2")
str_1 = 'Hello'
print(f"str_1 == 'Hello': {str_1 == 'Hello'}")
print(f"str_1 == 'hello': {str_1 == 'hello'}")
print(f"str_1.lower() == 'Hello': {str_1.lower() == 'Hello'}")
print(f"str_1.lower() == 'hello': {str_1.lower() == 'hello'}")
num_1 = 23
print(f"num_1 == 22: {num_1 == 22}")
print(f"num_1 == 23: {num_1 == 23}")
print(f"num_1 != 22: {num_1 != 22}")
print(f"num_1 != 23: {num_1 != 23}")
print(f"num_1 > 22: {num_1 > 22}")
print(f"num_1 > 23: {num_1 > 23}")
print(f"num_1 < 24: {num_1 < 24}")
print(f"num_1 < 23: {num_1 < 23}")
print(f"num_1 >= 24: {num_1 >= 24}")
print(f"num_1 >= 23: {num_1 >= 23}")
print(f"num_1 <= 22: {num_1 <= 22}")
print(f"num_1 <= 23: {num_1 <= 23}")
num_2 = 18
num_3 = 17
print(f"【num_2 >= 18 and num_3 >= 18】: {num_2 >= 18 and num_3 >= 18}")
print(f"【num_2 >= 18 and num_3 >= 17】: {num_2 >= 18 and num_3 >= 17}")
print(f"【num_2 >= 18 or num_3 >= 18】: {num_2 >= 18 or num_3 >= 18}")
print(f"【num_2 >= 19 or num_3 >= 18】: {num_2 >= 19 or num_3 >= 18}")
list_1 = [1, 2, 3, 4, 5]
print(f"【1 in list_1】: {1 in list_1}")
print(f"【-1 in list_1】: {-1 in list_1}")
print(f"【1 not in list_1】: {1 not in list_1}")
print(f"【-1 not in list_1】: {-1 not in list_1}")

# 5-3
print("\n5-3")
alien_color = 'red'
if alien_color == 'green':
    print("得5分")
alien_color = 'green'
if alien_color == 'green':
    print("得5分")

# 5-4
print("\n5-4")
alien_color = 'red'
if alien_color == 'green':
    print("得5分")
else:
    print("得10分")

# 5-5
print("\n5-5")
alien_color = 'red'
if alien_color == 'green':
    print("得5分")
elif alien_color == 'yellow':
    print("得10分")
elif alien_color == 'red':
    print("得15分")

# 5-6
print("\n5-6")
age = 65
if age < 2:
    print(f"{age}岁, 此人是婴儿.")
elif age < 4:
    print(f"{age}岁, 此人是幼儿.")
elif age < 13:
    print(f"{age}岁, 此人是儿童.")
elif age < 20:
    print(f"{age}岁, 此人是青少年.")
elif age < 65:
    print(f"{age}岁, 此人是成年人.")
else:
    print(f"{age}岁, 此人是老年人.")

# 5-7
print("\n5-7")
favorite_fruits = ['apple', 'peach', 'watermelon']
if 'apple' in favorite_fruits:
    print("you really like apple!")
if 'peach' in favorite_fruits:
    print("you really like peach!")
if 'banana' in favorite_fruits:
    print("you really like banana!")
if 'watermelon' in favorite_fruits:
    print("you really like watermelon!")
if 'pear' in favorite_fruits:
    print("you really like pear!")

# 5-8
print("\n5-8")
users = ['johann', 'jessie', 'Admin', 'Peter', 'william']
for user in users:
    if user.lower() == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

# 5-9
print("\n5-9")
users = []
if users:
    for user in users:
        if user.lower() == 'admin':
            print(
                f"Hello {user.title()}, would you like to see a status report?"
            )
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10
print("\n5-10")
current_users = ['johann', 'jessie', 'Alfred', 'bruce', 'Peter', 'william']
new_users = ['Bill', 'Bruce', 'Edward', 'Duke', 'WILLIAM']
# 确保比较时不区分大小写。需要创建current_users小写副本
# 使用列表解析创建小写副本
current_users_copy = [current_user.lower() for current_user in current_users]
print(current_users_copy)
for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f"当前用户名 {new_user} 被占用，请输入其他用户名。")
    else:
        print(f"当前用户名 {new_user} 可用。")

# 5-11
print("\n5-11")
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
