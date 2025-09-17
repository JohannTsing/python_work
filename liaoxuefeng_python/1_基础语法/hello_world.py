# Python基础语法示例
print("Hello, World!")  # 打印输出

print("\n使用\\进行字符串转义 或使用 原始字符串'r'raw_string")
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
print("\n多行字符串 ")
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

print("\n字符与Unicode码位 ")
# ord() 函数获取字符的Unicode码位
print(f"'A' 的Unicode码位是：{ord('A')}")
print(f"'中' 的Unicode码位是：{ord('中')}")
# chr() 函数将Unicode码位转换为字符
print(f"chr(66) 是：{chr(66)}")
print(f"chr(20020) 是：{chr(20020)}")
# 也可以直接使用16进制编码书写
print(f'十六进制表示中文字符: \u4e2d\u6587')

# 字符串编码
print("\n字符串编码 ")
abc = 'ABC'.encode('ascii')
print(f"'ABC' 的ASCII编码: {abc}")
print(f"解码: {abc.decode('ascii')}")
print(f"'ABC' 的UTF-8编码: {'ABC'.encode('utf-8')}")
zw = '中文'.encode('utf-8')
print(f"'中文' 的UTF-8编码: {zw}")
print(f"解码: {zw.decode('utf-8')}")

# 字符串长度和字符串对应的字节长度
print("\n字符串长度和字符串对应的字节长度 ")
print(f"len('ABC'): {len('ABC')}")
print(f"len('中文'): {len('中文')}")
print(f"len('ABC'.encode('ascii')): {len('ABC'.encode('ascii'))}")
print(f"len('中文'.encode('utf-8')): {len('中文'.encode('utf-8'))}")

# 字符串的格式化
print("\n字符串的格式化 ")
# 1，使用 % 进行格式化
print("Hello, %s" % "world")
print("Hi, %s, you have $%d. i have $%.2f. The hex is %x" % ("Michael", 1000000, 105.3142, 0xff))
# 2，使用 format() 方法进行格式化
print("Hello, {0}, 成绩提升了 {1:.1f}%".format("小明", 17.125))
# 3，使用 f-string 进行格式化
r = 2.5
s = 3.14 * r ** 2
print(f"The area of a circle with radius {r} is {s:.2f}")
# 变量和数据类型
name = "Python初学者"
age = 20
height = 1.75
is_student = True
print(f"姓名: {name}, 年龄: {age}, 身高: {height}, 学生: {is_student}")

# 基本运算符
print("\n基本运算符")
a = 10
b = 3
print(f"加法: {a + b}")
print(f"减法: {a - b}")
print(f"乘法: {a * b}")
# 除法的结果是浮点数，即使两个数都是整数且能整除
print(f"除法: {a / b}")
# 地板除法（取整） Python的取整规则是向下取整 （Java，Rust，Go语言使用的是向零取整）
print(f"取整: {a // b}")
# 取余时，余数与被除数的符号一致，这是由向下取整决定的
print(f"取余: {a % b}")
print(f"幂运算: {a ** b}")

# 条件语句
print("\n条件语句示例:")
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
print("\nwhile循环示例:")
count = 0
while count < 3:
    print(f"while循环第 {count+1} 次")
    count += 1