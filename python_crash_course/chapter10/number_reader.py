import json

filename = 'numbers.json'
with open(filename, 'r') as f:
    # 使用json.load()将列表读取到内存
    numbers = json.load(f)
print(numbers)