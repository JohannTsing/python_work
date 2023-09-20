from word_count import count_words

filename = 'text_files/alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"{filename} 这个文件不存在.")
# else:
#     # 计算该文件包含多少个单词
#     words = contents.split()
#     num_words = len(words)
#     print(f"这个文件 {filename} 包含了 {num_words} 个单词.")
count_words(filename)