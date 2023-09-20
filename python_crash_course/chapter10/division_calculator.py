# 使用try-except代码块，捕获异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print("除数不能为零")
'''
try-except-else代码块的工作原理大致如下:
Python尝试执行try代码块中的代码，只有可能引发异常的代码才需要放在try语句中。
有时候，有一些仅在try代码块成功执行时才需要运行的代码，这些代码应放在else代码块中。
except代码块告诉Python，如果尝试运行try代码块中的代码时引发了指定的异常该怎么办。
'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("除数不能为零")
    # 依赖try代码块成功执行的代码都应放到else代码块中
    else:
        print(answer)
