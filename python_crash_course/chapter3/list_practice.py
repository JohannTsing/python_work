students = ['johann', 'jessie', 'peter', 'willam']
print(students)

# 列表是有序集合，可以通过索引访问列表元素
print(students[0].title())
# 通过 -1 访问列表的最后一个元素
print(students[-1].title())
# 使用列表中的值
my_friend = f"My best friend is {students[1].title()}."
print(my_friend)

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[-1] = 'ducati'
print(motorcycles)

# 在列表中添加元素
# 使用 append() 在末尾添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('peugeot')
print(motorcycles)
# 使用 insert() 在列表中添加元素，需要指定新元素的索引
motorcycles.insert(1, 'suzuki')
print(motorcycles)
motorcycles = ['honda', 'yamaha']
# 如果新元素的指定索引超出索引范围，则会在边界加入新元素，边界可以是左边界也可以是右边界
motorcycles.insert(99, 'suzuki')
motorcycles.insert(-99, 'peugeot')
print(f"insert(-99): {motorcycles}")

# 删除列表中的元素
# 使用 del 删除元素【无返回值】。
# 如果超出索引范围，将报错 list assignment index out of range
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
# del motorcycles[99]
print(f"del: {motorcycles}")
'''
使用 pop() 删除元素【将返回删除的元素值】
使用pop()不加参数，默认删除列表末尾的元素；
使用pop(index)可以添加参数，参数为待删除元素的索引，
如果超出索引范围将报错，pop index out of range
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
pop_motorcycle = motorcycles.pop()
print(f"pop(0): {motorcycles}")
print(f"pop_motorcycle = {pop_motorcycle}")
pop_motorcycle = motorcycles.pop(-1)
# pop_motorcycle = motorcycles.pop(-99)
print(f"pop(-1): {motorcycles}")
print(f"pop_motorcycle = {pop_motorcycle}")
# 使用 remove() 删除元素【无返回值】，即返回值为 None。
# 如果该元素不存在，报错 list.remove(x): x not in list
motorcycles = ['honda', 'yamaha', 'suzuki']
remove_motorcycle = motorcycles.remove('yamaha')
print(f"remove('yamaha'): {motorcycles}")
print(f"remove_motorcycle = {remove_motorcycle}")
# 如果列表中存在多个同值的元素，remove()将随机删除一个元素
pets = ['rabbit', 'cat', 'dog', 'cat', 'cat', 'cat']
print(f"初始pets: {pets}")
pets.remove('cat')
print(f"remove执行完,pets: {pets}")

# 组织列表
# 使用 sort() 方法对列表进行【升序】排序【无返回值】，该方法将永久性地修改列表元素的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(f"sort(): {cars}")
# 使用 'reverse=True' 参数，进行【降序】排序
cars.sort(reverse=True)
print(f"sort(reverse=True): {cars}")
# 使用 sorted() 方法对列表进行【升序】临时排序，该方法会返回一个排序后的新列表，原来的列表不受影响
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"原来的列表: {cars}")
sorted_cars = sorted(cars)
print(f"临时升序排序后的列表: {sorted_cars}")
sorted_cars = sorted(cars, reverse=True)
print(f"临时降序排序后的列表: {sorted_cars}")
print(f"原来的列表: {cars}")
# 使用 reverse() 反转列表【无返回值】，该方法方法永久性地修改列表元素的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(f"反转列表reverse(): {cars}")
# 使用 len() 获取链表长度
cars_len = len(cars)
print(f"列表长度len(): {cars_len}")