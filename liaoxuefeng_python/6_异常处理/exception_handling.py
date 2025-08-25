# Python异常处理示例
print("=== 异常处理基础 ===")

# 基本try-except结构
def basic_exception_handling():
    """基本异常处理"""
    try:
        # 可能引发异常的代码
        num = int(input("请输入一个数字: "))
        result = 10 / num
        print(f"10除以{num}的结果是: {result}")
    except ValueError:
        print("错误：请输入有效的数字！")
    except ZeroDivisionError:
        print("错误：不能除以0！")
    except Exception as e:
        print(f"发生未知错误: {e}")

# basic_exception_handling()

print("\n=== 完整的异常处理结构 ===")

def complete_exception_handling():
    """完整的异常处理结构"""
    try:
        # 可能引发异常的代码
        file_name = input("请输入文件名: ")
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"文件内容:\n{content}")
    
    except FileNotFoundError:
        print("错误：文件不存在！")
    except PermissionError:
        print("错误：没有文件读取权限！")
    except UnicodeDecodeError:
        print("错误：文件编码问题！")
    except Exception as e:
        print(f"发生未知错误: {type(e).__name__}: {e}")
    
    else:
        # 如果没有发生异常，执行这里的代码
        print("文件读取成功！")
    
    finally:
        # 无论是否发生异常，都会执行这里的代码
        print("异常处理完成")

# complete_exception_handling()

print("\n=== 自定义异常 ===")

# 自定义异常类
class InvalidAgeError(Exception):
    """自定义年龄无效异常"""
    def __init__(self, age, message="年龄必须在0-150之间"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}，输入的年龄: {self.age}"

class NegativeBalanceError(Exception):
    """自定义余额不足异常"""
    pass

def validate_age(age):
    """验证年龄"""
    if not 0 <= age <= 150:
        raise InvalidAgeError(age)
    return True

def process_age():
    """处理年龄验证"""
    try:
        age = int(input("请输入年龄: "))
        validate_age(age)
        print(f"年龄验证通过: {age}")
    except InvalidAgeError as e:
        print(f"年龄验证失败: {e}")
    except ValueError:
        print("错误：请输入有效的数字！")

# process_age()

print("\n=== 异常链 ===")

def read_config():
    """读取配置文件"""
    try:
        with open("config.txt", "r") as file:
            return file.read()
    except FileNotFoundError as e:
        raise RuntimeError("配置文件不存在") from e

def setup_application():
    """设置应用程序"""
    try:
        config = read_config()
        print("应用程序设置成功")
        return config
    except RuntimeError as e:
        print(f"设置失败: {e}")
        print(f"原始异常: {e.__cause__}")

# setup_application()

print("\n=== 断言 ===")

def calculate_discount(price, discount):
    """计算折扣"""
    # 使用断言检查前提条件
    assert price > 0, "价格必须大于0"
    assert 0 <= discount <= 1, "折扣必须在0-1之间"
    
    final_price = price * (1 - discount)
    print(f"最终价格: {final_price}")
    return final_price

# 正常情况
try:
    calculate_discount(100, 0.2)
except AssertionError as e:
    print(f"断言错误: {e}")

# 异常情况
try:
    calculate_discount(-50, 0.2)
except AssertionError as e:
    print(f"断言错误: {e}")

print("\n=== 上下文管理器 ===")

class FileManager:
    """自定义文件上下文管理器"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入上下文时调用"""
        self.file = open(self.filename, self.mode, encoding="utf-8")
        print(f"打开文件: {self.filename}")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用"""
        if self.file:
            self.file.close()
            print(f"关闭文件: {self.filename}")
        if exc_type:
            print(f"发生异常: {exc_type.__name__}: {exc_val}")
        return False  # 不抑制异常

# 使用自定义上下文管理器
try:
    with FileManager("test.txt", "w") as f:
        f.write("Hello, Context Manager!\n")
        # 这里可以故意引发异常来测试
        # raise ValueError("测试异常")
except Exception as e:
    print(f"外部捕获异常: {e}")

print("\n=== 日志记录异常 ===")

import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data):
    """处理数据并记录异常"""
    try:
        if not data:
            raise ValueError("数据不能为空")
        
        result = int(data) * 2
        logging.info(f"数据处理成功: {result}")
        return result
    
    except ValueError as e:
        logging.error(f"数据处理失败: {e}")
        raise
    except Exception as e:
        logging.exception(f"未知错误发生: {e}")
        raise

# 测试日志记录
try:
    process_data("123")
    process_data("abc")  # 这会引发异常
except Exception:
    pass

print("\n=== 异常处理最佳实践 ===")

def safe_division(a, b):
    """安全的除法运算"""
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')  # 返回无穷大而不是崩溃
    except TypeError:
        raise ValueError("参数必须是数字类型")

# 测试安全除法
print(f"10 / 2 = {safe_division(10, 2)}")
print(f"10 / 0 = {safe_division(10, 0)}")

try:
    safe_division(10, "a")
except ValueError as e:
    print(f"类型错误: {e}")

print("\n=== 异常处理完成 ===")