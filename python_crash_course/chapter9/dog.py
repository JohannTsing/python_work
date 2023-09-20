class Dog:
    """创建小狗类"""

    def __init__(self, name, age):
        """初始化小狗属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下动作"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗打滚动作"""
        print(f"{self.name} rolled over.")


'''
1, 根据约定，在Python中，首字母大写的名称指的是类。这个类定义中没有圆括号，因为要从空白创建这个类。
2, 方法__init__()是一个特殊方法，每当你根据类创建新实例时，Python都会自动运行它。
在这个方法的定义中，形参self必不可少，而且必须位于其他形参的前面。
为何必须在方法定义中包含形参self呢？因为Python调用这个方法来创建实例时，将自动传入实参self。
3, 以self为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问。
self.name = name获取与形参name相关联的值，并将其赋给变量name，然后该变量被关联到当前创建的实例。
像这样可通过实例访问的变量称为属性。
'''
# 根据类创建实例
my_dog = Dog('Doudou', 2)
# 访问属性
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# 调用方法
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Maomao', 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()