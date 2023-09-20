# 打开 pi_digits.txt 文件并读取内容
# 使用 with 语句可以确保文件对象在使用完毕后被正确关闭。
with open('text_files/pi_digits.txt') as file_object:
    # 读取全部内容
    contents = file_object.read()
# 输出文件内容
print(contents.rstrip())
'''
显示文件路径时，Windows系统使用反斜杠（\）而不是斜杠（/），但在代码中依然可以使用斜杠。
'''
with open('text_files\\china.txt') as file_object:
    contents = file_object.read()
# 输出文件内容
print(contents.rstrip())

# 逐行读取
filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    # 每行的末尾都有一个看不见的换行符，而函数调用print()也会加上一个换行符，因此每行末尾都有两个换行符
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。
with open(filename) as file_object:
    # readlines()从文件中读取每一行，并将其存储在一个列表中
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
'''
读取文本文件时，Python将其中的所有文本都解读为字符串。如果读取的是数，并要将其作为数值使用，就必须使用函数int()将其转换为整数或使用函数float()将其转换为浮点数。
'''
print(type(pi_string))

# 读取大型文件
bigfilename = 'text_files/pi_million_digits.txt'
with open(bigfilename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"圆周率: {pi_string[:52]}...")
print(f"圆周率长度: {len(pi_string)}")
birth_str = '930202'
# 检查生日是否出现在圆周率值中
if birth_str in pi_string:
    index_number = pi_string.index(birth_str)
    print(f"你的生日 {birth_str} 出现在圆周率小数点之后的第 {index_number-2} 位.")
    print(f"3.14...{pi_string[index_number-2:index_number+8]}...")
else:
    print("圆周率值中不包含你的生日")
