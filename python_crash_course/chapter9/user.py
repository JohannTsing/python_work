class User:
    """用户类"""

    def __init__(self, first_name, last_name, age, native):
        """用户类初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.native = native

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


user_1 = User('johann', 'chao', 18, 'Hebei')
user_1.describe_user()
user_1.greet_user()
user_2 = User('jessie', 'chang', 17, 'Hebei')
user_2.describe_user()
user_2.greet_user()
user_3 = User('andrew', 'lee', 19, 'Shandong')
user_3.describe_user()
user_3.greet_user()