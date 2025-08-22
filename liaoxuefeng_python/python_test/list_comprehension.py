ANALYST_CONFIG = {
    "ben_graham": {
        "display_name": "Ben Graham",
        "agent_func": "ben_graham_agent",
        "order": 1,
    },
    "aswath_damodaran": {
        "display_name": "Aswath Damodaran",
        "agent_func": "aswath_damodaran_agent",
        "order": 0,
    },
}
print(f"type(ANALYST_CONFIG) {type(ANALYST_CONFIG)}")

ANALYST_ORDER = [(config["display_name"], key) for key, config in sorted(ANALYST_CONFIG.items(), key=lambda x: x[1]["order"])]
print(f"type(ANALYST_ORDER)  {type(ANALYST_ORDER)}")
print(ANALYST_ORDER)

'''字典的items()方法返回 dict_items 视图对象（view object），属于可迭代对象（实现了__iter__）。每个元素是 严格二元组（tuple），形式为 (key, value)'''
itms = ANALYST_CONFIG.items()
print(f"type(itms)  {type(itms)}") # <class 'dict_items'>
print(itms)

# 此处的 x 是二元组，x[1]是元组的第二个元素，对当前数据即为一个字典，x[1]["order"] 是字典的order属性值
sortitem = sorted(itms,key=lambda x: x[1]["order"])
print(f"type(sortitem)  {type(sortitem)}") # <class 'list'> 元素类型为列表，该列表中的子元素是包含两个子元素的元组
print(sortitem)

# 遍历元素
for v1,v2 in sortitem:
    print(f"v1: {v1}")
    print(f"v2: {v2}")

# 错误示例：尝试解包非二元组
# 无法将类型为 "tuple[str]" 的表达式分配给目标 tuple   类型 "tuple[str]" 与目标 tuple 不兼容     Tuple 大小不匹配; 应为 2，但收到 1
#for k,v in [('a',)]:  # ValueError: not enough values to unpack
#    print(k)


"""
列表推导式
[expression for item in iterable if condition]
"""
# 相比 for 循环，代码更短，可读性更高。
squares = [x**2 for x in range(10)]
print(squares)

# 嵌套循环
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# 输出：[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(pairs)

# 条件表达式
numbers = [1, 2, 3, 4, 5]
number_result = ["even" if x % 2 == 0 else "odd" for x in numbers]
# 输出：['odd', 'even', 'odd', 'even', 'odd']
print(number_result)

# 字典推导式
squares_dict = {x: x**2 for x in range(5)}
# 输出：{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(squares_dict)

# 集合推导式
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
# 输出：{0, 1, 4}
print(unique_squares)


'''生成器表达式（惰性计算）
生成器（generator）是一种特殊的迭代器，通过生成器表达式（如(x**2 for x in range(1000))）或yield关键字（函数中使用yield返回值）创建。其核心特点是惰性计算（按需生成值）。
生成器是迭代器，只能遍历一次（与enumerate类似），耗尽后无法重复使用。若需重复遍历，需重新创建生成器。
'''
squares_gen = (x**2 for x in range(1000))  # 不会立即计算
print(type(squares_gen))
print(f"生成器迭代: {next(squares_gen)}")
print(f"生成器迭代: {next(squares_gen)}")
print(f"生成器迭代: {next(squares_gen)}")
print(f"生成器迭代: {next(squares_gen)}")
# for num in squares_gen:  # 按需计算
#     print(num)

# ❌ 过于复杂，可读性差
result = [x**2 for x in range(100) if x % 2 == 0 if x > 50 if x % 3 == 0]
print(result)

# ✅ 改用 for 循环更清晰
result = []
for x in range(100):
    if x % 2 == 0 and x > 50 and x % 3 == 0:
        result.append(x**2)
print(result)

# 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)
# 输出：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 结合 enumerate 
words = ["hello", "world", "python"]
indexed_words = [(i, word) for i, word in enumerate(words,start=1)]
# 输出：[(0, 'hello'), (1, 'world'), (2, 'python')]
print(indexed_words)

"""enumerate对象是一个迭代器，所以只能遍历一次，遍历完就会耗尽。""" 
lst = ['apple', 'banana', 'cherry']
enum = enumerate(lst, start=1)  # 索引从1开始
print(list(enum))  # 输出：[(1, 'apple'), (2, 'banana'), (3, 'cherry')]
enum = enumerate(lst)
print(next(enum))  # 输出：(0, 'apple')
print(next(enum))  # 输出：(1, 'banana')
print(list(enum))  # 输出：[(2, 'cherry')]（剩余元素）
print(list(enum))  # 输出：[]（已耗尽）
