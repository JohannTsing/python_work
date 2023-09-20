# 10-3
print("\n10-3")
prompt = "What's your name? "
# guest = input(prompt)
# filename = 'text_files/guest.txt'
# with open(filename, 'w') as file_object:
#     file_object.write(guest)

# 10-4
print("\n10-4")
filename = 'text_files/guest_book.txt'
prompt += "\nEnter 'quit' to break at any time.\n"
flag = True
with open(filename, 'w') as file_object:
    while flag:
        guest = input(prompt)
        if guest == 'quit':
            break
        else:
            print(f"welcome, {guest}")
            file_object.write(f"{guest}\n")
