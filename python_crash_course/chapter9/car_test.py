# 从一个模块中导入一个类
from car import Car

my_new_car = Car('Benz', 'GLC 260', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(1600)
my_new_car.read_odometer()