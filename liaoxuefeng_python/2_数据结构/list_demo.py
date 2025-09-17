# python在list中操作数据
# 初始化一个list
country_list = ['China','Russia','USA','UK','France']
print(country_list)

# 获取list的长度
print(f'列表的长度是：{len(country_list)}')

# 使用索引获取list中的元素
print(f'列表的第一个元素是：{country_list[0]}')
print(f'列表的最后一个元素是：{country_list[-1]}')

# 往list中添加元素
# 1, 在列表末尾添加元素
print("执行: country_list.append('Germany')")
country_list.append('Germany')
print(country_list)
# 2, 在指定位置添加元素
print("执行: country_list.insert(5, 'Japan')")
country_list.insert(5, 'Japan')
print(country_list)
# 3, 还可以使用extend()方法，在列表末尾添加多个元素
print("执行: country_list.extend(['Canada', 'Australia', 'Canada'])")
country_list.extend(['Canada', 'Australia', 'Canada'])
print(country_list)

# 删除元素
# 1, 使用remove()方法，会删除第一个匹配的元素
print("执行: country_list.remove('Canada')")
country_list.remove('Canada')
print(country_list)
# 2, 使用del语句，删除指定位置的元素
print("执行: del country_list[5]")
del country_list[5]
print(country_list)
# 3, 使用pop()方法，删除并返回列表末尾的元素
print("执行: pop_country = country_list.pop()")
pop_country = country_list.pop()
print(pop_country)
print(country_list)
# pop()方法也可以删除指定位置的元素
print("执行: pop_country = country_list.pop(5)")
pop_country = country_list.pop(5)
print(pop_country)
print(country_list)

# 修改元素
print("执行: country_list[-1] = 'South Korea'")
country_list[-1] = 'South Korea'
print(country_list)

# 排序与翻转
print("执行: country_list.sort()")
country_list.sort()
print(country_list)
print("执行: country_list.reverse()")
country_list.reverse()
print(country_list)


# 二维数组
print("\n 二维数组")
asia_country_list = ['China', 'Japan', 'Korea', 'Thailand']
europe_country_list = ['Germany', 'France', 'Italy', 'Spain']
america_country_list = ['USA', 'Canada', 'Mexico', 'Brazil']
africa_country_list = ['Egypt', 'Morocco', 'South Africa', 'Nigeria']
world_country_list = [asia_country_list, europe_country_list, america_country_list, africa_country_list]
print(world_country_list)

# lambda表达式
from functools import reduce
numbers = [1,2,3,4,5]
result = reduce(lambda x,y: x+y,numbers)
print(result)
result = reduce(lambda x,y: x*y,numbers)
print(result)
maped = map(lambda x: x*2,numbers)
print(type(maped))
# 直接迭代 map 对象
for value in maped:  
    print(value)
print(list(maped))

filtered = filter(lambda x: x%2==0,numbers)
print(list(filtered))
sorted_list = sorted(numbers, key=lambda x: -x)
print(list(sorted_list))

# 列表推导式
list2 = [i for i in range(1, 11)]
print(list2)
list3 = [i * i for i in range(1, 11)]
print(list3)

# 列表生成式
list4 = [i for i in range(1, 11) if i % 2 == 0]
print(list4)

# 列表解析
list5 = [i * i for i in range(1, 11) if i % 2 == 0]
print(list5)
