class Restaurant:
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆类初始化"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """餐馆描述"""
        print(f"餐馆名: {self.restaurant_name}.")
        print(f"菜系风格: {self.cuisine_type}.")

    def open_restaurant(self):
        """餐馆营业状态"""
        print(f"{self.restaurant_name} 正在营业.")
