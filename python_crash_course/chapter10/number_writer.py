import json

numbers = [1, 2, 5, 7, 9]
filename = 'numbers.json'
with open(filename, 'w') as f:
    # 使用json.dump()来存储数据
    # 函数json.dump()接受两个实参：要存储的数据，以及可用于存储数据的文件对象。
    json.dump(numbers, f)
