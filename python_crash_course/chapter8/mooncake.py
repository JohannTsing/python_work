def make_mooncake(size, *fillings):
    """制作月饼"""
    print(f"使用以下馅料，制作一个 {size} 英寸的月饼: ")
    for filling in fillings:
        print(f" - {filling}")