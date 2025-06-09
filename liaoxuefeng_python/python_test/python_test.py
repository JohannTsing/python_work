from functools import reduce
from datetime import datetime
import re

def test():
    print("hello world")
    # lambda表达式
    numbers = [1,2,3,4,5]
    result = reduce(lambda x,y: x+y,numbers)
    print(result)
    result = reduce(lambda x,y: x*y,numbers)
    print(result)
    maped = map(lambda x: x*2,numbers)
    print(list(maped))
    filtered = filter(lambda x: x%2==0,numbers)
    print(list(filtered))
    sorted_list = sorted(numbers, key=lambda x: -x)
    print(list(sorted_list))


    # 原始日期字符串
    date_str = "September 10, 2024"

    # 解析日期字符串为datetime对象
    date_obj = datetime.strptime(date_str, "%B %d, %Y")

    # 格式化datetime对象为指定格式的字符串
    formatted_date_str = date_obj.strftime("%Y-%m-%d")

    print(formatted_date_str)  # 输出: 2024-09-10

    print(f"最大公约数: {gcd(133, 209)}")
    print(f"最大公约数: {lcm(133, 209)}")

# 欧几里得算法, 最大公约数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

def testFindall():
    content = "您的房源发布编码：001212获取成功，您的房源发布编码：F20241024810000676_004。您可复制此编码到授权的互联网平台进行房源发布。感谢您的使用!"
    contentlist = re.findall(r"您的房源发布编码：[a-zA-Z0-9_]+", content)
    # 遍历list
    for item in contentlist:
        print(item)
    publishCode = re.findall(r"您的房源发布编码：[a-zA-Z0-9_]+", content)[0].replace("您的房源发布编码：", "")
    print(publishCode)


def testProgressbar():
    cycle = 10000
    for i in range(cycle):
        for j in range(cycle):
            k = i * j
        #print(f"{i+1} / {cycle}", end="\t")
        print(f"\r{int(i/cycle*100)}%", end="")
    print("\n执行完毕")

    name = "Charlie"
    age = 35
    print("%s is %d years old." % (name, age))  # 输出: Charlie is 35 years old.


def main():
    test()

if __name__ == '__main__':
    main()
