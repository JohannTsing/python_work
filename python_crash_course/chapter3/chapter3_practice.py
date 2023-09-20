# 3-1
print("3-1")
names = ['johann', 'jessie', 'peter', 'willam']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# 3-2
print("\n3-2")
print(f"Hello, {names[0].title()}.")
print(f"Hello, {names[1].title()}.")
print(f"Hello, {names[2].title()}.")
print(f"Hello, {names[3].title()}.")

# 3-3
print("\n3-3")
commuting_mode = ["bike", "motorcycle", "car"]
print(f"I would like to own a Honda {commuting_mode[0]}.")
print(f"I would like to own a Honda {commuting_mode[1]}.")
print(f"I would like to own a Honda {commuting_mode[2]}.")

# 3-4
print("\n3-4")
inviters = ['johann', 'jessie', 'peter']
print(f"诚邀以下诸位: {inviters}")

# 3-5
print("\n3-5")
absence = inviters[-1]
print(f"抱歉, {absence}将缺席")
inviters[-1] = 'william'
print(f"诚邀以下诸位: {inviters}")

# 3-6
print("\n3-6")
print("找到了一个更大的餐桌")
inviters = ['johann', 'jessie', 'peter']
inviters.insert(0, 'bill')
inviters.insert(2, 'duke')
inviters.append('able')
print(f"诚邀以下诸位: {inviters}")

# 3-7
print("\n3-7")
print("这个餐桌无法送达，因此只能邀请两位")
absence = inviters.pop()
print(f"抱歉，无法邀请你来共进晚餐了，{absence}")
absence = inviters.pop()
print(f"抱歉，无法邀请你来共进晚餐了，{absence}")
absence = inviters.pop()
print(f"抱歉，无法邀请你来共进晚餐了，{absence}")
absence = inviters.pop()
print(f"抱歉，无法邀请你来共进晚餐了，{absence}")
print(f"你依然在邀请之列，{inviters[0]}")
print(f"你依然在邀请之列，{inviters[1]}")
print("用餐结束！")
del inviters[0]
del inviters[0]
print(f"愉快的用餐，当前邀请之列为 {inviters}")

# 3-8
print("\n3-8")
scenic_spots = ['Kyoto', 'Hokkaido', 'Lijiang', 'Dali', 'Bali']
print(f"初始景点: {scenic_spots}")
sorted_spots = sorted(scenic_spots)
print(f"sorted()升序排序后景点: {sorted_spots}")
print(f"初始景点: {scenic_spots}")
sorted_spots = sorted(scenic_spots, reverse=True)
print(f"sorted()降序排序后景点: {sorted_spots}")
print(f"初始景点: {scenic_spots}")
reversed_spots = scenic_spots.reverse()
print(f"反转景点: {scenic_spots}")
print(f"reverse()无返回值: {reversed_spots}")
scenic_spots.reverse()
print(f"再次反转，得到初始景点: {scenic_spots}")
sort_spots = scenic_spots.sort()
print(f"sort()升序排序后景点: {scenic_spots}")
print(f"sort()无返回值: {sort_spots}")
scenic_spots.sort(reverse=True)
print(f"sort()降序排序后景点: {scenic_spots}")

# 3-9
print("\n3-9")
inviters = ['johann', 'jessie', 'peter']
inviters.insert(0, 'bill')
inviters.insert(2, 'duke')
inviters.append('able')
print(f"诚邀以下诸位: {inviters} 共进晚餐, 共计 {len(inviters)} 人.")

# 3-10
print("\n3-10")
every_thing = ['beijing']
print(f"初始列表为: {every_thing}")
every_thing[0] = 'Shanghai'
print(f"根据索引修改列表元素: {every_thing}")
every_thing.append('Nike say "Just do it"')
every_thing.insert(0, 'Beijing')
every_thing.insert(-99, 'Kyoto')
every_thing.insert(99, 'Dali')
print(f"执行添加操作后的列表: {every_thing}")
del every_thing[0]
pop_thing = every_thing.pop()
print(f"删除末尾元素: {pop_thing}")
pop_thing = every_thing.pop(-1)
print(f"删除指定索引元素: {pop_thing}")
every_thing.remove('Shanghai')
print(f"执行删除操作后的列表: {every_thing}")
every_thing.append('Wuhan')
every_thing.append('Harbin')
every_thing.append('Taipei')
print(f"当前列表: {every_thing}")
sorted_thing = sorted(every_thing)
print(f"升序排序后列表: {sorted_thing}")
sorted_thing = sorted(every_thing, reverse=True)
print(f"降序排序后列表: {sorted_thing}")
print(f"当前列表: {every_thing}")
every_thing.reverse()
print(f"反转当前列表: {every_thing}")
every_thing.reverse()
print(f"二次反转当前列表: {every_thing}")
every_thing.sort()
print(f"永久升序排序后，当前列表: {every_thing}")
every_thing.sort(reverse=True)
print(f"永久降序排序后，当前列表: {every_thing}")
print(f"当前列表的长度为: {len(every_thing)}")

# 3-11
print("\n3-11")
index_erros = ['Beijing']
'''
print(f"获取元素，list index out of range: {index_erros[1]}")
del index_erros[1] # list assignment index out of range
index_erros.pop(1) # pop index out of range
index_erros.remove('Shanghai') # list.remove(x): x not in list
'''