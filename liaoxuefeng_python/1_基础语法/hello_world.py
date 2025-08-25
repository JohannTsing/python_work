# Python基础语法示例
print("Hello, World!")  # 打印输出

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