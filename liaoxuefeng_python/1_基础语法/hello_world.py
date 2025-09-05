# Python基础语法示例
print("Hello, World!")  # 打印输出

# 字符串转义
greet = "Hi, I'm \"OK\"! \n"
print(greet)

# 如果希望保留原始字符串（raw_string），可以在字符串前方添加r
greet = r"I'm \"OK\"! \n"
print(greet)
path = r'C:\Users\name\data.txt'
print(path)
path = 'C:\\Users\\name\\data.txt'
print(path)
path = 'C:/Users/name/data.txt'
print(path)

# 多行字符串
# 不保留换行
long_string = (
    "这是一个非常长的字符串，它需要"
    "被分成多行书写，Python会自动"
    "将这些字符串连接在一起"
)
print(long_string)
# 保留换行
long_string = """这是一个非常长的字符串，
它需要被分成多行书写，
Python会保留这些换行符"""
print(long_string)

# 变量和数据类型
name = "Python初学者"
age = 20
height = 1.75
is_student = True

print(f"姓名: {name}, 年龄: {age}, 身高: {height}, 学生: {is_student}")

# 基本运算符
a = 10
b = 3
print(f"加法: {a + b}")
print(f"减法: {a - b}")
print(f"乘法: {a * b}")
print(f"除法: {a / b}")
print(f"取整: {a // b}")
print(f"取余: {a % b}")
print(f"幂运算: {a ** b}")

# 条件语句
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 循环语句
print("\n循环示例:")
for i in range(5):
    print(f"循环第 {i+1} 次")

# while循环
count = 0
while count < 3:
    print(f"while循环第 {count+1} 次")
    count += 1