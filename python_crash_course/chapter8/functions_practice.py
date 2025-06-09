# 使用 def 关键字定义一个函数
def greet_user():
    """文档字符串注释"""
    print("Hello,Python!")


greet_user()


# 带有形参的函数
def greet_user_name(username):
    """问候语"""
    print(f"Hello, {username.title()}.")


'''
函数定义中的变量，称之为形参。
函数调用中的变量，称之为实参。
'''
greet_user_name("Johann")


# 传递实参的方式
# 位置实参，实参的顺序与形参的顺序相同
def describe_pet(animal_type, pet_name):
    """宠物信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("dog", "doudou")

# 关键字实参
'''
关键字实参是传递给函数的名称值对。
因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆。
关键字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
XXX: 使用关键字实参时，务必准确指定函数定义中的形参名。
'''
describe_pet(pet_name="maomao", animal_type="cat")


# 给形参指定默认值
# XXX: 使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的形参。
def describe_pet2(pet_name, animal_type='dog'):
    """宠物信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet2(pet_name='damao')
# 该函数由于指定了animal_type的默认值，因此在函数调用中只包含一个实参，指向第一个形参
describe_pet2('damao')
describe_pet2('ermao', 'cat')


# 函数返回值，使用 return 关键字返回一个或一组值
def get_formatted_name(firstname, lastname):
    """名字格式化"""
    return f"{firstname.title()} {lastname.title()}"


johann = get_formatted_name('johann', 'chao')
print(johann)


# 实参变为可选，其实就是给形参设置默认值
def get_formatted_name1(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    # Python将非空字符串解读为True
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name1('john', 'hooker', 'lee')
print(musician)


# 返回字典
def build_person(firstname, lastname, age=None):
    """返回字典，包含一个用户的信息"""
    person = {'firstname': firstname, 'lastname': lastname}
    if age:
        person['age'] = age
    return person


person = build_person('Johann', 'Chao', 18)
print(person)

# 结合使用函数和while循环
# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'quit' at any time to quit.)")

#     first_name = input("First name: ")
#     if first_name == 'quit':
#         break
#     last_name = input("Last name: ")
#     if last_name == 'quit':
#         break

#     formatted_name = get_formatted_name(first_name, last_name)
#     print(f"Hello, {formatted_name.title()}!")


# 传递列表
def greet_users(names):
    for name in names:
        print(f"Hello, {name.title()}.")


names = ['johann', 'jessie', 'andrew']
greet_users(names)

# 在函数中修改列表
print("\n在函数中修改列表")


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 业务操作中，如果需要保留源列表，则此时只需在函数中传入源列表的副本即可
print_models(unprinted_designs[:], completed_models)
# print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(f"\nunprinted_designs: {unprinted_designs}")


# 传递任意数量的实参
# XXX: 当预先不知道函数需要接收多少个实参时，可以给函数设置 "*参数名" 这种格式的形参。# 形参 "*参数名" 中的星号让Python创建一个名为"参数名"的空元组，并将收到的所有值都封装到这个元组中。
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    # print(toppings)
    print("\nPizza toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量实参
# XXX: 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza1(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza1(16, 'pepperoni')
make_pizza1(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
# XXX: 当预先不知道传递给函数的会是什么样的信息时，可将函数编写成能够接受任意数量的键值对——调用语句提供了多少就接受多少。即给函数设置 "**参数名" 这种格式的形参。
# 形参 "**参数名" 中的两个星号让Python创建一个名为 "参数名" 的空字典，并将收到的所有名称值对都放到这个字典中。
def build_profile(first_name, last_name, **userinfo):
    """创建一个字典，包含用户信息"""
    userinfo['first_name'] = first_name
    userinfo['last_name'] = last_name
    return userinfo


user_profile = build_profile("Johann",
                             "Chao",
                             age=19,
                             location='princeton',
                             field='physics')
print(user_profile)

# 将函数存储在模块中
# 1, 导入整个模块.
# 格式为: import module_name
import mooncake

mooncake.make_mooncake(
    3,
    '蛋黄',
    '莲蓉',
)

# 2, 使用as给模块指定别名
# 格式为: import module_name as mn
import mooncake as mc

mc.make_mooncake(
    2,
    '杏仁',
    '核桃仁',
    '花生仁',
    '麻仁',
    '瓜子仁',
    '青红丝',
)

# 3, 导入特定的函数.
# 格式为: from module_name import function_0, function_1, function_2
from mooncake import make_mooncake

make_mooncake(
    1,
    '红豆沙',
)

# 4, 使用as给函数指定别名
# 格式为: from module_name import function_name as fn
from mooncake import make_mooncake as mm

mm(2, '冬瓜蓉')

# 5, 导入模块中的所有函数, 使用星号（*）运算符可以导入模块中的所有函数
from mooncake import *
