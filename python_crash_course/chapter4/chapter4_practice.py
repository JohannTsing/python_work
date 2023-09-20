# 4-1
print("4-1")
pizzas = ['bacon pizza', 'fruit pizza', 'pepperoni pizza']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza}.\n")
print("I really love pizza!")

# 4-2
print("\n4-2")
cats = ['jaguar', 'tiger', 'lion', 'puma', 'cheetah', 'snow leopard']
for cat in cats:
    print(f"A {cat} is a cat.")
print("Any of these animals is a cat!")

# 4-3
print("\n4-3")
for num in range(1, 21):
    print(num)

# 4-4
print("\n4-4")
# for num in range(1,1000001):
#     print(num)

# 4-5
print("\n4-5")
numbers = list(range(1, 1000001))
print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")
print(f"sum: {sum(numbers)}")

# 4-6
print("\n4-6")
odds = list(range(1, 20, 2))
for odd in odds:
    print(f"odd number: {odd}")

# 4-7
print("\n4-7")
multipleOf3 = list(range(3, 30, 3))
for num in multipleOf3:
    print(f"3的倍数: {num}")

# 4-8
print("\n4-8")
cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
for cube in cubes:
    print(f"cube: {cube}")

# 4-9
print("\n4-9")
cubes = [num**3 for num in range(1, 11)]
print(cubes)

# 4-10
print("\n4-10")
cats = ['jaguar', 'tiger', 'lion', 'puma', 'cheetah', 'snow leopard']
print(f"list are: {cats}")
print(f"The first three items in the list are: {cats[:3]}")
print(f"Three items from the middle of the list are: {cats[2:5]}")
print(f"The last three items in the list are: {cats[-3:]}")

# 4-11
print("\n4-11")
my_pizzas = ['bacon pizza', 'fruit pizza', 'pepperoni pizza']
friend_pizzas = my_pizzas[:]
my_pizzas.append('bar pizza')
friend_pizzas.append('cheese pizza')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"\t{pizza}")
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")

# 4-12
print("\n4-12")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite food are:")
for food in my_foods:
    print(f"\t{food}")
print("My friend's favorite food are:")
for food in friend_foods:
    print(f"\t{food}")

# 4-13
print("\n4-13")
foods = ('bread', 'baguette', 'pasta', 'pizza', 'fried noodles')
print("调整前的食物:")
for food in foods:
    print(f"\t{food}")
# foods[2] = 'macaroni'dumpling
foods = ('dumpling', 'baguette', 'pasta', 'pizza', 'macaroni')
print("调整后的食物:")
for food in foods:
    print(f"\t{food}")