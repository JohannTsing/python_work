# 函数input()的工作原理
# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其赋给一个变量，以方便你使用。
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# 函数input()接受一个参数——要向用户显示的提示（prompt）或说明，让用户知道该如何做。
# name = input("Please enter your name: ")
# print(f"Hello, {name}!")
# prompt = "If you tell me who you are, i can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"Hello, {name}!")

# XXX:使用int()来获取数值输入
# age = input("How old are you? ")
# print(f"age = {age}, type(age): {type(age)}")
# # 报错：'>=' not supported between instances of 'str' and 'int'
# age = int(age)
# if age >= 18:
#     print("你可以去投票了！")

# 求模运算（%），它将两个数相除并返回余数
'''
有两数 a,b
两数相除取整运算（//），即将除法的结果向着负无穷方向取整数
c = a // b
a % b = a - (b * c)
'''
print(f"4 // 3 = {4 // 3}, 4 % 3 = {4 % 3}")
print(f"4 // -3 = {4 // -3}, 4 % -3 = {4 % -3}")
print(f"-4 // 3 = {-4 // 3}, -4 % 3 = {-4 % 3}")
print(f"-4 // -3 = {-4 // -3}, -4 % -3 = {-4 % -3}")
# 判断输入的数字的奇偶
# input_number = int(
#     input("Enter a number, and I'll tell you if it's even or odd: "))
# if input_number % 2 == 0:
#     print(f"The number {input_number} is even.")
# else:
#     print(f"The number {input_number} is odd.")

# while循环
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
prompt = "\nTell me something, and I'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# 使用标志来控制循环
flag = True
# while flag:
#     message = input(prompt)
#     if message == 'quit':
#         flag = False
#     else:
#         print(message)

# 使用break退出循环
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# 使用continue返回循环开头。它会跳过循环中的剩余步骤，返回到循环开头，而不会终止循环
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# 使用while循环处理列表和字典
# for循环是一种遍历列表的有效方式，但不应在for循环中修改列表，否则将导致Python难以跟踪其中的元素。
# 要在遍历列表的同时对其进行修改，可使用while循环。

# 在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 列表名用作条件表达式时，列表至少包含一个元素时返回True，列表为空时返回False
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user}")
    confirmed_users.append(current_user)
print("The following users have been confirmed:")
for user in confirmed_users:
    print(f"\t{user.title()}")

# 删除为特定值的所有列表元素
pets = ['rabbit', 'cat', 'dog', 'cat', 'cat', 'cat']
print(f"初始pets: {pets}")
while 'cat' in pets:
    pets.remove('cat')
print(f"循环删除完后的pets: {pets}")

# 使用用户输入来填充字典
responses = {}
flag = True
while flag:
    name = input("\n你的名字? ")
    response = input("你最想哪个城市旅游? ")
    responses[name] = response
    continueFlag = input("是否还有其他人参与?(yes or no) ")
    if continueFlag == 'no':
        flag = False
print("\n--- 调查结果如下: --- ")
for name, response in responses.items():
    print(f"{name.title()} 最想去 {response} 旅游.")