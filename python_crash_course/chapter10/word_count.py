def count_words(filename):
    """计算一个文件大致有多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # 使用pass语句，静默失败
        pass
        # print(f"{filename} 这个文件不存在.")
    else:
        # 计算该文件包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"这个文件 {filename} 包含了 {num_words} 个单词.")


# filename = 'text_files/alice.txt'
# count_words(filename)

filenames = [
    'text_files/alice.txt', 'text_files/little_women.txt', 'siddhartha.txt',
    'text_files/moby_dick.txt'
]
for filename in filenames:
    count_words(filename)

# filenames_copy = filenames[:]
# while filenames_copy:
#     current_filename = filenames_copy.pop()
#     count_words(current_filename)
# print(filenames)