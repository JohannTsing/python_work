# Python数据结构示例 - 列表操作
print("=== 列表基本操作 ===")

# 创建列表
fruits = ["apple", "banana", "cherry", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"水果列表: {fruits}")
print(f"数字列表: {numbers}")
print(f"混合列表: {mixed}")

# 访问列表元素
print(f"\n第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")
print(f"切片操作: {fruits[1:3]}")

# 修改列表
fruits[1] = "blueberry"
print(f"修改后的列表: {fruits}")

# 列表方法
fruits.append("grape")  # 添加元素
print(f"添加葡萄后: {fruits}")

fruits.insert(2, "mango")  # 插入元素
print(f"插入芒果后: {fruits}")

fruits.remove("cherry")  # 删除元素
print(f"删除樱桃后: {fruits}")

popped = fruits.pop()  # 弹出最后一个元素
print(f"弹出的元素: {popped}, 剩余列表: {fruits}")

# 列表排序
numbers.sort(reverse=True)
print(f"降序排序: {numbers}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"平方数列表: {squares}")

print("\n=== 其他数据结构 ===")

# 元组 (不可变)
coordinates = (10, 20)
print(f"坐标元组: {coordinates}")

# 字典 (键值对)
person = {
    "name": "Alice",
    "age": 25,
    "city": "Beijing"
}
print(f"个人信息: {person}")
print(f"姓名: {person['name']}")

# 集合 (无序不重复)
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print(f"唯一数字集合: {unique_numbers}")

# 遍历数据结构
print("\n=== 遍历示例 ===")
print("遍历列表:")
for fruit in fruits:
    print(f"- {fruit}")

print("\n遍历字典:")
for key, value in person.items():
    print(f"{key}: {value}")