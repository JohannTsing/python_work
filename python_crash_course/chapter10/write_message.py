# 写入文件
'''
第一个实参也是要打开的文件的名称。
第二个实参('w')告诉Python，要以写入模式打开这个文件。
打开文件时，可指定读取模式('r')、写入模式('w')、附加模式('a')或读写模式('r+')。
如果省略了模式实参，Python将以默认的只读模式打开文件。

XXX: 当以写入模式('w')打开一个文件时，如果该文件不存在，则open()将自动创建它；
如果指定的文件已存在，此时将在返回文件对象前清空该文件的内容
'''
filename = 'text_files/programming.txt'
with open(filename, 'w') as file_object:
    # Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。
    file_object.write("I love programming.")
    # 写入多行时，需要手动换行
    file_object.write("\nI love creating new games.")

# 附加到文件
# 如果要给文件添加内容，而不是覆盖原有的内容，可以以附加模式('a')打开文件。
with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.")
    file_object.write("\nI love creating apps that can run in a browser.")