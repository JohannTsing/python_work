# Python面向对象编程示例
print("=== 类和对象基础 ===")

# 定义简单的类
class Dog:
    """狗类"""
    
    # 类属性
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name  # 实例属性
        self.age = age
    
    def bark(self):
        """实例方法"""
        return f"{self.name} says: Woof!"
    
    def get_info(self):
        """获取信息方法"""
        return f"{self.name} is {self.age} years old, species: {self.species}"

# 创建对象
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.bark())
print(dog2.get_info())

print("\n=== 继承和多态 ===")

# 继承示例
class GoldenRetriever(Dog):
    """金毛犬类 - 继承自Dog"""
    
    def __init__(self, name, age, color="golden"):
        super().__init__(name, age)
        self.color = color
    
    def fetch(self):
        """金毛特有的方法"""
        return f"{self.name} is fetching the ball!"
    
    # 方法重写
    def bark(self):
        return f"{self.name} says: Woof! (Golden Retriever style)"

class Poodle(Dog):
    """贵宾犬类 - 继承自Dog"""
    
    def bark(self):
        return f"{self.name} says: Yip! (Poodle style)"

# 多态示例
golden = GoldenRetriever("Max", 2)
poodle = Poodle("Coco", 4)

dogs = [golden, poodle]
for dog in dogs:
    print(dog.bark())  # 多态：不同对象调用相同方法，表现不同

print("\n=== 封装和属性控制 ===")

class BankAccount:
    """银行账户类 - 封装示例"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 私有属性
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            return f"存款成功，当前余额: {self.__balance}"
        return "存款金额必须大于0"
    
    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"取款成功，当前余额: {self.__balance}"
        return "取款金额无效或余额不足"
    
    def get_balance(self):
        """获取余额（封装访问）"""
        return self.__balance
    
    # 属性装饰器
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("余额不能为负数")

# 使用银行账户
account = BankAccount("Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"当前余额: {account.get_balance()}")

print("\n=== 特殊方法 ===")

class Vector:
    """向量类 - 特殊方法示例"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """解释器表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """加法运算"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """乘法运算"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __len__(self):
        """长度（模）"""
        return int((self.x**2 + self.y**2)**0.5)

# 使用特殊方法
v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2
v4 = v1 * 3

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v3}")
print(f"v1 * 3: {v4}")
print(f"v1的长度: {len(v1)}")

print("\n=== 静态方法和类方法 ===")

class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def add(a, b):
        """静态方法"""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """类方法"""
        return a * b

print(f"静态方法: {MathUtils.add(5, 3)}")
print(f"类方法: {MathUtils.multiply(5, 3)}")