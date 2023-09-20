from random import randint, choice

# randint(a,b) 返回范围[a，b]内的随机整数，包括两个端点
print(randint(1, 5))

players = ['johann', 'jessie', 'andrew', 'duke', 'william']
# choice() 非空序列中选择一个随机元素
first_up = choice(players)
print(first_up)