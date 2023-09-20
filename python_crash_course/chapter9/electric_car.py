"""在一个模块中存储多个类"""

# 在一个模块中，导入另外一个模块
from car import Car


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