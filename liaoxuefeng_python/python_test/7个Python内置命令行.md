### 1, 终端打印日历

```python
# -m 是一个命令行参数，全称为 --module，它的作用是将后续的模块名当作脚本运行。
# 打印本年度日历
python -m calendar
# 打印指定年月日的日历
python -m calendar 2031
python -m calendar 2031 4
```

### 2, 海龟图形

```python
python -m turtledemo
```

### 3, 使用 json.tool 处理JSON

```python
# 查看当前 json 数据
python -m json.tool test.json
# 缩进 2 空格
python -m json.tool --indent 2 test.json
# 按照键名排序
python -m json.tool --indent 2 --sort-keys test.json
# 将 缩进2空格,按键名排序的数据，输出到指定文件
python -m json.tool --indent 2 --sort-keys test.json > test_sort.json
```

### 4, 建立 HTTP 服务器

```python
# 快速建立一个http服务器. 如果需要在内网传输文件,此时转到传输的文件夹下输入该命令,即可在内网其他电脑中访问下载
python -m http.server 8000
```

### 5, 使用 timeit 进行测试

```python
python -m timeit -n 1000 -r 5 "'-'.join(str(n) for n in range(10))"
python -m timeit -n 1000 -r 5 '''"-".join(str(n) for n in range(10))'''
```

### 6, 快速生成密码

```python
# -c 是一个参数，全称是 --command，它的作用是直接执行后面跟着的 Python 代码字符串，而不需要运行单独的脚本文件
# 导入 Python 标准库的 secrets 模块（用于生成加密安全的随机数）
python -c "import secrets; print(secrets.token_urlsafe(16))"
```

### 7, 压缩文件

```python
# 压缩单个文件. gzip模块一次只能处理单个文件
python -m gzip test.json
# zipfile模块可以将多个文件压缩到一个压缩包. -c testjson.zip 创建一个新的自拍文件并指定压缩包名
python -m zipfile -c testjson.zip test.json test_sort.json test_sorted.json
# 将 testjson.zip 解压缩到当前目录的 my-extract目录下
python -m zipfile -e testjson.zip my-exreact/
```
