print("Hello, Python!")
'''
变量名规则
1, 变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字打头。
2, 变量名不能包含空格，但能使用下划线来分隔其中的单词。
3, 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print 
'''
message = "hello, python!"
print(message)

# 字符串类型
# 字符串可以使用双引号,也可以使用单引号
single_quotes = 'I told my friend, "Python is my favorite language!"'
print(single_quotes)
python_named = "The language 'Python' is named after Monty Python, not the snake."
print(python_named)

# 方法title()以首字母大写的方式显示每个单词
name = "johann chao"
print(name.title())
print(name.upper())
name_upper = "JOHANN CHAO"
print(name_upper.lower())

# f字符串. f是format（设置格式）的简写, Python通过把花括号内的变量替换为其值来设置字符串的格式.
first_name = "johann"
last_name = "chao"
full_name = f"{first_name} {last_name}"
print("full_name is " + full_name.title())
print(f"full_name is {full_name.title()}!")
'''
f字符串是Python 3.6引入的。如果你使用的是Python 3.5或更早的版本，需要使用format()方法
'''
full_name2 = "{} {}".format(first_name, last_name)
print(full_name2.title())

# 使用制表符(\t)、换行符(\n)来添加空白
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白。rstrip(),lstrip(),strip()分别为删除末尾，开头，两边的空白
strWithBlank = " this is a strip str "
print(f"strWithBlank:{strWithBlank}")
rstripStr = strWithBlank.rstrip()
print(f"rstripStr:{rstripStr}")
lstripStr = strWithBlank.lstrip()
print(f"lstripStr:{lstripStr}")
stripStr = strWithBlank.strip()
print(f"stripStr:{stripStr}")

# 数字类型
# 整数的加减乘除
print("整数运算:")
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
# 两个乘号表示乘方
print(2**3)
# 运算次序
print(2 + 3 * 4)
print((2 + 3) * 4)

# 浮点数
print("浮点数运算:")
print(0.1 + 0.1)
print(0.1 * 0.1)
# 将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除
print(9 / 3)
# 在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数
print(1 + 1.0)
print(1 * 1.0)
print(2.0**3)
'''
数中的下划线
书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读。
打印这种使用下划线定义的数时，Python不会打印其中的下划线。
这种表示法适用于整数和浮点数，但只有Python 3.6和更高的版本支持。
'''
print("数中的下划线:")
mumber_1 = 1_00_000
print(mumber_1)
mumber_2 = 1_000.000_1
print(mumber_2)

# 同时给多个变量赋值
x, y, z = 1, 2.0, "jessie"
print(f"{x}, {y}, {z}")

# 常量类似于变量，但其值在程序的整个生命周期内保持不变。Python没有内置的常量类型，但Python程序员会使用全大写来指出应将某个变量视为常量
INT_MAX = 2147483647