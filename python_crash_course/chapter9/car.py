"""在一个模块中存储一个类"""


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