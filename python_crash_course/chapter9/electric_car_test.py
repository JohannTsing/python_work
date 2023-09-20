# 1, 从一个模块中导入多个类
# from electric_car import Car, ElectricCar

# my_passat = Car('volkswagen', 'passat', 2020)
# print(my_passat.get_descriptive_name())

# my_han = ElectricCar('byd', 'han', 2021)
# print(my_han.get_descriptive_name())

# 2, 导入整个模块
# import electric_car

# my_passat = electric_car.Car('volkswagen', 'passat', 2020)
# print(my_passat.get_descriptive_name())

# my_han = electric_car.ElectricCar('byd', 'han', 2021)
# print(my_han.get_descriptive_name())

# 3, 导入模块中的所有类【不推荐使用这种导入方式】
'''
1), 不清楚具体导入了哪些类。
2), 如果导入了同名类，将引发错误。
如果需要从一个模块中导入很多类时，最好导入整个模块，并使用 module_name.ClassName 语法来访问类。
'''
# from electric_car import *

# 4, 使用别名
from electric_car import Car, ElectricCar as EC

my_passat = Car('volkswagen', 'passat', 2020)
print(my_passat.get_descriptive_name())

my_han = EC('byd', 'han', 2021)
print(my_han.get_descriptive_name())