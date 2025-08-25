# Python常用库示例
print("=== 常用库介绍 ===")

print("\n=== requests库 (HTTP请求) ===")
print("""
安装: pip install requests

示例代码:
import requests

# GET请求
response = requests.get('https://httpbin.org/get')
print(f"状态码: {response.status_code}")
print(f"响应内容: {response.text[:100]}...")

# POST请求
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(f"POST响应: {response.json()}")

# 带headers的请求
headers = {'User-Agent': 'my-app/1.0'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(f"Headers响应: {response.json()}")
""")

print("\n=== numpy库 (数值计算) ===")
print("""
安装: pip install numpy

示例代码:
import numpy as np

# 创建数组
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)  # 0到10，步长为2
arr3 = np.zeros((3, 3))     # 3x3零矩阵
arr4 = np.ones((2, 4))      # 2x4一矩阵

print(f"一维数组: {arr1}")
print(f"范围数组: {arr2}")
print(f"零矩阵:\\n{arr3}")
print(f"一矩阵:\\n{arr4}")

# 数组运算
result = arr1 * 2 + 1
print(f"数组运算: {result}")

# 矩阵运算
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(matrix1, matrix2)
print(f"矩阵乘法:\\n{dot_product}")
""")

print("\n=== pandas库 (数据分析) ===")
print("""
安装: pip install pandas

示例代码:
import pandas as pd

# 创建DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# 基本操作
print(f"\\n形状: {df.shape}")
print(f"列名: {df.columns}")
print(f"描述统计:\\n{df.describe()}")

# 数据筛选
young_people = df[df['年龄'] < 30]
print(f"\\n年轻人:\\n{young_people}")

# 读取CSV文件
# df = pd.read_csv('data.csv')
""")

print("\n=== matplotlib库 (数据可视化) ===")
print("""
安装: pip install matplotlib

示例代码:
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('正弦函数图像')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()
plt.grid(True)
# plt.show()

# 绘制柱状图
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=['red', 'green', 'blue', 'orange'])
plt.title('柱状图示例')
plt.xlabel('类别')
plt.ylabel('数值')
# plt.show()
""")

print("\n=== beautifulsoup4库 (网页解析) ===")
print("""
安装: pip install beautifulsoup4

示例代码:
from bs4 import BeautifulSoup
import requests

html_content = '''
<html>
<head><title>测试页面</title></head>
<body>
<h1>欢迎来到测试页面</h1>
<div class="content">
    <p class="text">第一段文字</p>
    <p class="text">第二段文字</p>
    <a href="https://example.com">链接</a>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html_content, 'html.parser')
print(f"页面标题: {soup.title.text}")
print(f"所有段落: {[p.text for p in soup.find_all('p')]}")
print(f"所有链接: {[a['href'] for a in soup.find_all('a')]}")
""")

print("\n=== flask库 (Web框架) ===")
print("""
安装: pip install flask

示例代码:
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '欢迎来到首页!'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from API!', 'status': 'success'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
""")

print("\n=== opencv-python库 (计算机视觉) ===")
print("""
安装: pip install opencv-python

示例代码:
import cv2
import numpy as np

# 创建黑色图像
image = np.zeros((300, 400, 3), dtype=np.uint8)

# 绘制图形
cv2.rectangle(image, (50, 50), (200, 150), (0, 255, 0), 2)
cv2.circle(image, (300, 150), 50, (255, 0, 0), -1)
cv2.putText(image, 'OpenCV', (150, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# 显示图像
# cv2.imshow('示例图像', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print("OpenCV图像处理完成")
""")

print("\n=== pillow库 (图像处理) ===")
print("""
安装: pip install pillow

示例代码:
from PIL import Image, ImageDraw, ImageFont

# 创建新图像
img = Image.new('RGB', (400, 300), color='white')
draw = ImageDraw.Draw(img)

# 绘制图形
draw.rectangle([50, 50, 200, 150], fill='blue', outline='red')
draw.ellipse([250, 50, 350, 150], fill='green')

# 保存图像
# img.save('example.png')
print("Pillow图像创建完成")
""")

print("\n=== 其他常用库 ===")
print("""
1. scikit-learn - 机器学习
   pip install scikit-learn

2. tensorflow/pytorch - 深度学习
   pip install tensorflow
   pip install torch

3. django - 重量级Web框架
   pip install django

4. fastapi - 现代Web框架
   pip install fastapi

5. selenium - 浏览器自动化
   pip install selenium

6. pytest - 测试框架
   pip install pytest

7. jupyter - 交互式笔记本
   pip install jupyter

8. sqlalchemy - ORM框架
   pip install sqlalchemy

9. openpyxl - Excel操作
   pip install openpyxl

10. python-dotenv - 环境变量
    pip install python-dotenv
""")

print("\n=== 库的版本管理 ===")
print("""
查看已安装的包:
pip list

查看特定包信息:
pip show package_name

生成requirements.txt:
pip freeze > requirements.txt

从requirements.txt安装:
pip install -r requirements.txt

升级所有包:
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
""")

print("\n=== 常用库学习完成 ===")
print("""
学习建议:
1. 先掌握基础库: requests, numpy, pandas, matplotlib
2. 根据需求选择学习方向:
   - Web开发: flask/django, fastapi
   - 数据分析: pandas, numpy, matplotlib
   - 机器学习: scikit-learn, tensorflow, pytorch
   - 自动化: selenium, beautifulsoup4
3. 阅读官方文档和示例代码
4. 多动手实践项目
""")