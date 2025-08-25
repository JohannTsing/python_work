# Python函数示例
print("=== 函数基础 ===")

# 定义简单函数
def greet(name):
    """打招呼的函数"""
    return f"Hello, {name}!"

# 调用函数
message = greet("Alice")
print(message)

# 带默认参数的函数
def introduce(name, age=25, city="Beijing"):
    """自我介绍函数"""
    return f"我叫{name}, {age}岁, 来自{city}"

print(introduce("Bob"))
print(introduce("Charlie", 30, "Shanghai"))

# 可变参数
def sum_numbers(*args):
    """计算任意数量数字的和"""
    total = 0
    for num in args:
        total += num
    return total

print(f"数字和: {sum_numbers(1, 2, 3, 4, 5)}")

# 关键字参数
def print_info(**kwargs):
    """打印关键字参数信息"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="David", age=28, occupation="Engineer")

print("\n=== 函数返回值 ===")

# 返回多个值
def calculate(a, b):
    """计算加、减、乘、除"""
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b if b != 0 else "不能除以0"
    return add, subtract, multiply, divide

result = calculate(10, 5)
print(f"计算结果: {result}")

print("\n=== 高阶函数 ===")

# 函数作为参数
def apply_operation(func, x, y):
    """应用操作函数"""
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(f"加法结果: {apply_operation(add, 3, 4)}")
print(f"乘法结果: {apply_operation(multiply, 3, 4)}")

# lambda函数
square = lambda x: x ** 2
print(f"平方: {square(5)}")

# map函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"平方列表: {squared}")

# filter函数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

print("\n=== 作用域和闭包 ===")

# 闭包示例
def outer_function(x):
    """外部函数"""
    def inner_function(y):
        """内部函数"""
        return x + y
    return inner_function

closure = outer_function(10)
print(f"闭包结果: {closure(5)}")

# 装饰器
def my_decorator(func):
    """简单的装饰器"""
    def wrapper():
        print("函数执行前...")
        result = func()
        print("函数执行后...")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()