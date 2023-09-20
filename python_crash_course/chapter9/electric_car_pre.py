class Car:
    """汽车类"""

    def __init__(self, make, model, year):
        """属性初始化"""
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回汽车描述"""
        long_name = f"{self.year} {self.make} {self.model} \nodometer_reading: {self.odometer_reading}"
        return long_name.title()

    def read_odometer(self):
        """汽车里程信息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        设置里程信息
        禁止将里程表读数往回调
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, addmiles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += addmiles

    def fill_gas_tank(self):
        """将油箱加满油"""
        print("The gas tank has been filled up.")


class Battery:
    """电池类"""

    def __init__(self, battery_size=90):
        """电池初始化"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电池容量"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_rang(self):
        """根据电池容量，返回续航里程"""
        if self.battery_size == 90:
            return 600
        elif self.battery_size == 108:
            return 700
        else:
            return None

    def update_battery(self):
        """如果电池容量不为108，将其更新为108"""
        if self.battery_size != 108:
            print("update battery size 108.")
            self.battery_size = 108


'''
编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，可使用继承。
一个类继承另一个类时，将自动获得另一个类的所有属性和方法。
原有的类称为父类，而新类称为子类。
子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。

创建子类时，父类必须包含在当前文件中，且位于子类前面。
定义子类时，必须在圆括号内指定父类的名称。
'''


class ElectricCar(Car):
    """电动汽车类，作为汽车类的子类"""

    def __init__(self, make, model, year, battery_size=90):
        """
        先初始化父类属性
        再初始化子类特有的属性
        """
        # super()是一个特殊函数，让你能够调用父类的方法。
        super().__init__(make, model, year)
        # self.battery_size = battery_size
        # 将电池实例用作电动汽车类的属性
        self.battery = Battery(battery_size)

    # def describe_battery(self):
    #     """子类特有的方法
    #     打印电池容量"""
    #     print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """
        子类重写父类方法
        电动车没有油箱
        """
        print("This car doesn't need a gas tank!")


my_tang = ElectricCar('BYD', 'tang', 2022)
print(my_tang.get_descriptive_name())
# my_tang.describe_battery()
my_tang.fill_gas_tank()
my_tang.battery.describe_battery()
range = my_tang.battery.get_rang()
print(f"This car can go about {range} miles on a full charge.")
my_tang.battery.update_battery()
print(
    f"This car can go about {my_tang.battery.get_rang()} miles on a full charge."
)
