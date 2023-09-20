# 7-1
print("7-1")
# car = input("你需要租赁什么品牌的汽车? ")
# print(f"让我看看海有没有{car}汽车。")

# 7-2
print("\n7-2")
# user_num = input("请问您有几位用餐? ")
# user_num = int(user_num)
# if user_num > 8:
#     print("对不起，当前没有空桌")
# else:
#     print("当前有空桌，您这边请。")

# 7-3
print("\n7-3")
# multiples_of_10 = input("输入一个数字，我将告知你该数字是否是10的整数倍. ")
# multiples_of_10 = int(multiples_of_10)
# if multiples_of_10 % 10 == 0:
#     print(f"当前输入的数字为 {multiples_of_10}, 该数字是10的整数倍.")
# else:
#     print(f"当前输入的数字为 {multiples_of_10}, 该数字不是10的整数倍.")

# 7-4
print("\n7-4")
# prompt = "\n请输入披萨配料。\n配料添加完成后，输入'quit'退出。 "
# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(f"将在披萨中添加 {topping}")

# 7-5
print("\n7-5")
# while True:
#     age = int(input("\n输入年龄，查询票价。"))
#     if age < 3:
#         print(f"当前年龄{age}岁，免费。")
#     elif age < 12:
#         print(f"当前年龄{age}岁，票价10元。")
#     else:
#         print(f"当前年龄{age}岁，票价15元。")

# 7-6
print("\n7-6")
# prompt = "\n请输入披萨配料。\n配料添加完成后，输入'quit'退出。 "
# # 1）使用条件测试来结束循环
# topping = ""
# while topping != 'quit':
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"将在披萨中添加 {topping}")
# # 2）使用变量active来控制循环结束
# flag = True
# while flag:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"将在披萨中添加 {topping}")
#     else:
#         flag = False
# # 3）使用break语句在用户输入'quit'时退出循环
# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(f"将在披萨中添加 {topping}")

# 7-7
print("\n7-7")
# print("无限循环错误！")
# current_number = 1
# while current_number < 5:
#     print(current_number)

# 7-8
print("\n7-8")
# sandwich_orders = ['bacon', 'ham', 'vegetable']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich} sandwich.")
#     finished_sandwiches.append(sandwich)
# print("---制作完成的三明治---")
# for sandwich in finished_sandwiches:
#     print(f"\t{sandwich} sandwich")

# 7-9
print("\n7-9")
sandwich_orders = [
    'pastrami', 'pastrami', 'bacon', 'pastrami', 'ham', 'vegetable', 'pastrami'
]
print(f"sandwich_orders: {sandwich_orders}")
finished_sandwiches = []
print("pastrami is sold out!")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        continue
    else:
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)
print("---制作完成的三明治---")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich} sandwich")

# 7-10
print("\n7-10")
dream_places = {}
flag = True
while flag:
    name = input("What's your name? ")
    place = input(
        "If you could visit one place in the world, where would you go? ")
    dream_places[name] = place
    continueFlag = input('Is there anyone else you need to count?(yes or no) ')
    if continueFlag == 'no':
        flag = False
print("--- Poll Results ---")
for name, place in dream_places.items():
    print(f"{name.title()} would like to {place}.")