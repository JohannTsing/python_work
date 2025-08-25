# Python文件操作示例
print("=== 文件读写操作 ===")

# 写入文件
def write_to_file():
    """写入文件示例"""
    try:
        with open("example.txt", "w", encoding="utf-8") as file:
            file.write("Hello, Python!\n")
            file.write("这是文件操作示例\n")
            file.write("第三行内容\n")
        print("文件写入成功")
    except IOError as e:
        print(f"写入文件错误: {e}")

# 读取文件
def read_from_file():
    """读取文件示例"""
    try:
        with open("example.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("文件内容:")
            print(content)
    except FileNotFoundError:
        print("文件不存在")
    except IOError as e:
        print(f"读取文件错误: {e}")

# 逐行读取
def read_line_by_line():
    """逐行读取文件"""
    try:
        with open("example.txt", "r", encoding="utf-8") as file:
            print("\n逐行读取:")
            for line_num, line in enumerate(file, 1):
                print(f"第{line_num}行: {line.strip()}")
    except FileNotFoundError:
        print("文件不存在")

# 追加内容
def append_to_file():
    """追加内容到文件"""
    try:
        with open("example.txt", "a", encoding="utf-8") as file:
            file.write("这是追加的内容\n")
            file.write("文件操作完成\n")
        print("内容追加成功")
    except IOError as e:
        print(f"追加内容错误: {e}")

# 执行文件操作
write_to_file()
read_from_file()
read_line_by_line()
append_to_file()
read_from_file()  # 再次读取查看追加的内容

print("\n=== 文件操作的其他方法 ===")

# 检查文件是否存在
import os

def check_file_exists():
    """检查文件是否存在"""
    if os.path.exists("example.txt"):
        print("文件存在")
        
        # 获取文件信息
        file_size = os.path.getsize("example.txt")
        print(f"文件大小: {file_size} 字节")
        
        # 获取文件修改时间
        mod_time = os.path.getmtime("example.txt")
        print(f"修改时间: {mod_time}")
    else:
        print("文件不存在")

check_file_exists()

print("\n=== 目录操作 ===")

# 创建目录
def create_directory():
    """创建目录示例"""
    dir_name = "test_dir"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"目录 {dir_name} 创建成功")
    else:
        print(f"目录 {dir_name} 已存在")

# 列出目录内容
def list_directory():
    """列出目录内容"""
    print("当前目录内容:")
    for item in os.listdir("."):
        if os.path.isfile(item):
            print(f"文件: {item}")
        elif os.path.isdir(item):
            print(f"目录: {item}")

create_directory()
list_directory()

print("\n=== CSV文件操作 ===")

import csv

def write_csv_file():
    """写入CSV文件"""
    data = [
        ["姓名", "年龄", "城市"],
        ["张三", 25, "北京"],
        ["李四", 30, "上海"],
        ["王五", 28, "广州"]
    ]
    
    with open("data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("CSV文件写入成功")

def read_csv_file():
    """读取CSV文件"""
    try:
        with open("data.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            print("CSV文件内容:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("CSV文件不存在")

write_csv_file()
read_csv_file()

print("\n=== JSON文件操作 ===")

import json

def write_json_file():
    """写入JSON文件"""
    data = {
        "name": "Alice",
        "age": 25,
        "city": "Beijing",
        "hobbies": ["reading", "swimming", "coding"],
        "is_student": True
    }
    
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print("JSON文件写入成功")

def read_json_file():
    """读取JSON文件"""
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            print("JSON文件内容:")
            print(json.dumps(data, ensure_ascii=False, indent=2))
    except FileNotFoundError:
        print("JSON文件不存在")

write_json_file()
read_json_file()

# 清理创建的文件
def cleanup_files():
    """清理创建的文件"""
    files_to_remove = ["example.txt", "data.csv", "data.json"]
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"已删除: {file}")
    
    # 删除测试目录
    if os.path.exists("test_dir"):
        os.rmdir("test_dir")
        print("已删除测试目录")

print("\n=== 文件操作完成 ===")
# cleanup_files()  # 取消注释可以清理文件