# 9-1
print("9-1")


class Restaurant:
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆类初始化"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆描述"""
        describe = f"餐馆名: {self.restaurant_name}, 菜系风格: {self.cuisine_type}."
        return describe

    def open_restaurant(self):
        """餐馆营业状态"""
        print(f"{self.restaurant_name} 正在营业.")

    def get_number_served(self):
        """餐馆就餐人数"""
        print(f"今日已有 {self.number_served} 人前来就餐.")

    def set_number_served(self, number_served):
        """设置餐馆就餐人数"""
        self.number_served = number_served

    def increment_number_served(self, addnumber):
        """就餐人数递增"""
        self.number_served += addnumber


qiluyuan = Restaurant('齐鲁苑', '山东菜')
print(qiluyuan.restaurant_name)
print(qiluyuan.cuisine_type)
print(qiluyuan.describe_restaurant())
qiluyuan.open_restaurant()

# 9-2
print("\n9-2")
shouxiangyuan = Restaurant('首湘缘', '湖南菜')
zhumulangma = Restaurant('珠穆朗玛餐厅', '西藏菜')
baminshifu = Restaurant('八闽食府', '福建菜')
print(shouxiangyuan.describe_restaurant())
print(zhumulangma.describe_restaurant())
print(baminshifu.describe_restaurant())

# 9-2
print("\n9-3")


class User:
    """用户类"""

    def __init__(self, first_name, last_name, age, native):
        """用户类初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.native = native
        self.login_attempts = 0

    def describe_user(self):
        """用户描述"""
        print(f"user profile:")
        print(
            f"- user name: {self.first_name.title()} {self.last_name.title()}")
        print(f"- user age: {self.age}")
        print(f"- user native: {self.native}")

    def greet_user(self):
        """用户问候"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """登录尝试次数递增1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """登录尝试次数重置为0"""
        self.login_attempts = 0


user_1 = User('johann', 'chao', 18, 'Hebei')
user_1.describe_user()
user_1.greet_user()
user_2 = User('jessie', 'chang', 17, 'Hebei')
user_2.describe_user()
user_2.greet_user()
user_3 = User('andrew', 'lee', 19, 'Shandong')
user_3.describe_user()
user_3.greet_user()

# 9-4
print("\n9-4")
yuntengshifu = Restaurant('云腾食府', '云南菜')
yuntengshifu.get_number_served()
yuntengshifu.number_served = 10
yuntengshifu.get_number_served()
yuntengshifu.set_number_served(15)
yuntengshifu.get_number_served()
yuntengshifu.increment_number_served(100)
yuntengshifu.get_number_served()

# 9-5
print("\n9-5")
user_4 = User('duke', 'ye', 19, 'shanxi')
user_4.describe_user()
user_4.greet_user()
print(f"login_attempts: {user_4.login_attempts}")
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
print(f"login_attempts: {user_4.login_attempts}")
user_4.reset_login_attempts()
print(f"login_attempts: {user_4.login_attempts}")

# 9-6
print("\n9-6")


class IceCreamStand(Restaurant):
    """
    冰淇淋店类，继承自餐馆类
    """

    def __init__(self, restaurant_name, cuisine_type):
        """先初始化父类-餐馆类属性，再初始化子类-冰激凌店类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'Sweet taro', 'rum']

    def show_flavors(self):
        """展示冰淇淋口味"""
        print(f"冰淇淋口味如下: ")
        for flavor in self.flavors:
            print(f" - {flavor}")


my_iceCreamStand = IceCreamStand('冰爽一夏', '冷饮类')
my_iceCreamStand.show_flavors()

# 9-7
print("\n9-7")

# class Admin(User):
#     """管理员类"""

#     def __init__(self, first_name, last_name, age, native):
#         """管理员类属性初始化"""
#         super().__init__(first_name, last_name, age, native)
#         self.privileges = ["can add post", "can delete post", "can ban user"]

#     def show_privileges(self):
#         """展示权限"""
#         print(f"管理员权限如下: ")
#         for privilege in self.privileges:
#             print(f" - {privilege}")

# my_admin = Admin('johann', 'chao', 18, 'Hebei')
# my_admin.show_privileges()

# 9-8
print("\n9-8")


class Privileges:
    """权限类"""

    def __init__(self,
                 privileges=[
                     'can add post', 'can delete post', 'can ban user'
                 ]):
        """权限类初始化"""
        self.privileges = privileges

    def show_privileges(self):
        """展示权限"""
        print(f"权限如下: ")
        for privilege in self.privileges:
            print(f" - {privilege}")


class Admin(User):
    """管理员类"""

    def __init__(self, first_name, last_name, age, native):
        """管理员类属性初始化"""
        super().__init__(first_name, last_name, age, native)
        self.privileges = Privileges()


my_admin = Admin('johann', 'chao', 18, 'Hebei')
my_admin.privileges.show_privileges()

# 9-13
print("\n9-13")
from random import randint, choices, sample


class Die:
    """创建一个骰子类"""

    def __init__(self, sides=6):
        """骰子属性初始化"""
        print(f"\n创建一个 {sides} 面的骰子实例.")
        self.sides = sides

    def roll_die(self):
        """投掷骰子"""
        print(f"当前掷出来的是 {randint(1,self.sides)} 点.")


die_6 = Die()
for i in range(1, 11):
    print(f"第 {i} 次投掷：")
    die_6.roll_die()
die_10 = Die(10)
for i in range(1, 11):
    print(f"第 {i} 次投掷：")
    die_10.roll_die()
die_20 = Die(20)
for i in range(1, 11):
    print(f"第 {i} 次投掷：")
    die_20.roll_die()

# 9-14
print("\n9-14")
lottery_poll = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
# choices()方法会根据列表中的元素的权重,随机选择指定数量(k)的元素,选择的元素允许重复。
winning_numbers = choices(lottery_poll, k=4)
print(winning_numbers)
# sample() 方法可以从列表中随机选择指定数量(k)的元素,而不重复。
# winning_numbers = sample(lottery_poll, k=4)
# print(winning_numbers)

# 9-15
print("\n9-15")
my_ticket = []
flag = False
count = 0
while not flag:
    count += 1
    my_ticket = choices(lottery_poll, k=4)
    flag = all(a == b for a, b in zip(winning_numbers, my_ticket))
print(f"循环了 {count} 次，才中奖！")