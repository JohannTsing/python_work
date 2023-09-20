# 8-1
print("8-1")


def display_message():
    """介绍"""
    print("本章学习的是Python函数")


display_message()

# 8-2
print("\n8-2")


def favorite_book(bookname):
    """最喜欢的书"""
    print(f"我最喜欢的书是<<{bookname}>>.")


favorite_book("百年孤独")

# 8-3
print("\n8-3")


def make_shirt(size, description):
    print(f"T恤的尺码是 {size}, 字样是'{description}'")


# 位置实参调用
make_shirt('L', 'Hello, world!')
# 关键字实参调用
make_shirt(description='Hello, world!', size='M')

# 8-4
print("\n8-4")


def make_shirt2(size='L', description='I love Python'):
    print(f"T恤的尺码是 {size}, 字样是'{description}'")


make_shirt2()
make_shirt2('M')
make_shirt2(description='I love Ruby')

# 8-5
print("\n8-5")


def describe_city(city, country='China'):
    print(f"{city} is in {country}")


describe_city('Beijing')
describe_city('Tokyo')
describe_city('Shanghai')

# 8-6
print("\n8-6")


def city_country(city, country):
    return f"{city}, {country}"


print(city_country('Beijing', 'China'))
print(city_country('Tokyo', 'Japan'))
print(city_country('Paris', 'France'))

# 8-7
print("\n8-7")


def make_album(artist, album_title, album_size=None):
    album = {'artist': artist, 'album_title': album_title}
    if album_size:
        album['album_size'] = album_size
    return album


print(make_album('Jay Chou', 'Common Jasmine Orange'))
print(make_album('JJ Lin', 'Haven'))
print(make_album('Second Hand Rose', 'Stealing The Show', 12))

# 8-8
print("\n8-8")
# while True:
#     print("\nPlease enter the album information: ")
#     print("(enter 'quit' at any time to quit.)")

#     artist = input("Artist: ")
#     if artist == 'quit':
#         break
#     album_title = input("Album title: ")
#     if album_title == 'quit':
#         break
#     album_size = input("Album size: ")
#     if album_size == 'quit':
#         break

#     album = make_album(artist, album_title, album_size)
#     print(f"the album information: {album}")

# 8-9
print("\n8-9")


def show_messages(messages):
    for message in messages:
        print(f"the message is: {message}")


messages = ['hello,world!', 'hello,python!']
show_messages(messages)

# 8-10
print("\n8-10")


def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"the unsent message is: {message}")
        sent_messages.append(message)


unsent_messages = ['hello,world!', 'hello,python!']
sent_messages = []
send_messages(unsent_messages, sent_messages)
print(f"\nunsent_messages: {unsent_messages}")
print(f"sent_messages: {sent_messages}")

# 8-11
print("\n8-11")
unsent_messages = ['hello,world!', 'hello,python!']
sent_messages = []
send_messages(unsent_messages[:], sent_messages)
print(f"\nunsent_messages: {unsent_messages}")
print(f"sent_messages: {sent_messages}")

# 8-12
print("\n8-12")


def make_sandwich(*food_material):
    print("你选择的三明治食材包含以下几种: ")
    for f in food_material:
        print(f" --{f}")


make_sandwich('培根', )
make_sandwich(
    '培根',
    '鸡蛋',
)
make_sandwich(
    '培根',
    '鸡蛋',
    '西红柿',
)

# 8-13
print("\n8-13")


def build_profile(first_name, last_name, **userinfo):
    """创建一个字典，包含用户信息"""
    userinfo['first_name'] = first_name
    userinfo['last_name'] = last_name
    return userinfo


johann_profile = build_profile('Joahnn',
                               'Chao',
                               age=18,
                               city='Beijing',
                               favorite_book=[
                                   '四世同堂',
                                   '百年孤独',
                               ])
print(johann_profile)

# 8-14
print("\n8-14")


def make_car(brand, vehicle_model, **carinfo):
    carinfo['brand'] = brand
    carinfo['vehicle_model'] = vehicle_model
    return carinfo


camry = make_car('toyota', 'camry', color='white', vehicle_type='sedan')
tang = make_car('byd', 'tang', color='black', vehicle_type='SUV')
cc = make_car('volkswagen', 'cc', color='gray', vehicle_type='shooting brake')
print(camry)
print(tang)
print(cc)
