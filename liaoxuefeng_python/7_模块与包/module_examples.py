# Python模块与包示例
print("=== 模块导入和使用 ===")

# 导入标准库模块
import math
import random
import datetime

# 使用模块功能
print(f"圆周率: {math.pi}")
print(f"平方根: {math.sqrt(16)}")
print(f"随机数: {random.randint(1, 100)}")
print(f"当前时间: {datetime.datetime.now()}")

print("\n=== 导入特定功能 ===")

# 导入特定功能
from math import sin, cos, tan
from random import choice, shuffle

print(f"正弦: {sin(math.pi/2)}")
print(f"余弦: {cos(0)}")
fruits = ["apple", "banana", "cherry"]
print(f"随机选择: {choice(fruits)}")

print("\n=== 别名导入 ===")

# 使用别名
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 模拟numpy和pandas的使用
print("使用别名导入模块 (需要安装相应库)")

print("\n=== 自定义模块 ===")

# 创建简单的自定义模块
# 先创建一个math_utils.py模块
math_utils_content = '''
"""数学工具模块"""

def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b

PI = 3.14159
'''

# 写入math_utils.py文件
with open("math_utils.py", "w", encoding="utf-8") as f:
    f.write(math_utils_content)

# 导入自定义模块
import math_utils

print(f"自定义模块加法: {math_utils.add(5, 3)}")
print(f"自定义模块乘法: {math_utils.multiply(4, 6)}")
print(f"PI值: {math_utils.PI}")

print("\n=== 包的结构 ===")

# 创建包结构
import os
os.makedirs("mypackage/utils", exist_ok=True)
os.makedirs("mypackage/models", exist_ok=True)

# 创建__init__.py文件（空文件表示这是一个包）
with open("mypackage/__init__.py", "w") as f:
    f.write('''"""我的包"""\n''')

# 创建工具模块
utils_content = '''
"""工具模块"""

def format_name(first, last):
    """格式化姓名"""
    return f"{first} {last}".title()

def calculate_age(birth_year):
    """计算年龄"""
    from datetime import datetime
    return datetime.now().year - birth_year
'''

with open("mypackage/utils/helpers.py", "w", encoding="utf-8") as f:
    f.write(utils_content)

# 创建模型模块
models_content = '''
"""模型模块"""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_info(self):
        return f"用户: {self.name}, 邮箱: {self.email}"
'''

with open("mypackage/models/user.py", "w", encoding="utf-8") as f:
    f.write(models_content)

print("包结构创建完成")

print("\n=== 包的使用 ===")

# 导入包中的模块
from mypackage.utils.helpers import format_name, calculate_age
from mypackage.models.user import User

print(f"格式化姓名: {format_name('john', 'doe')}")
print(f"计算年龄: {calculate_age(1990)}")

user = User("Alice", "alice@example.com")
print(user.get_info())

print("\n=== 相对导入 ===")

# 在包内部创建使用相对导入的模块
relative_content = '''
"""相对导入示例"""

# 从同一包中的其他模块导入
from ..utils.helpers import format_name
from .user import User

def create_user_profile(first, last, email):
    """创建用户资料"""
    name = format_name(first, last)
    user = User(name, email)
    return user.get_info()
'''

with open("mypackage/models/profile.py", "w", encoding="utf-8") as f:
    f.write(relative_content)

print("相对导入模块创建完成")

print("\n=== 模块属性 ===")

# 查看模块属性
print(f"模块名: {math_utils.__name__}")
print(f"模块文档: {math_utils.__doc__}")
print(f"模块文件: {math_utils.__file__}")

print("\n=== 动态导入 ===")

# 动态导入模块
module_name = "math_utils"
try:
    module = __import__(module_name)
    print(f"动态导入成功: {module.add(2, 3)}")
except ImportError:
    print(f"无法导入模块: {module_name}")

print("\n=== 搜索路径 ===")

# 查看模块搜索路径
import sys
print("模块搜索路径:")
for path in sys.path:
    if "site-packages" in path or "lib" in path:
        print(f"  {path}")

print("\n=== 安装第三方包 ===")

print("""
安装第三方包的常用命令:
pip install numpy      # 安装numpy
pip install pandas     # 安装pandas
pip install requests   # 安装requests

升级包:
pip install --upgrade package_name

查看已安装的包:
pip list

卸载包:
pip uninstall package_name
""")

print("\n=== 虚拟环境 ===")

print("""
创建虚拟环境:
python -m venv myenv

激活虚拟环境 (Windows):
myenv\\Scripts\\activate

激活虚拟环境 (Linux/Mac):
source myenv/bin/activate

停用虚拟环境:
deactivate
""")

# 清理创建的文件
import shutil
def cleanup():
    """清理创建的文件"""
    files_to_remove = ["math_utils.py"]
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
    
    # 删除包目录
    if os.path.exists("mypackage"):
        shutil.rmtree("mypackage")
    
    print("清理完成")

print("\n=== 模块与包学习完成 ===")
# cleanup()  # 取消注释可以清理文件