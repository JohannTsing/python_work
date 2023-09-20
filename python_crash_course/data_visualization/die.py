"""骰子module"""
from random import randint


class Die:
    """骰子类"""

    def __init__(self, num_sides=6):
        """骰子默认6个面"""
        self.num_sides = num_sides

    def roll(self):
        """投掷骰子，返回一个1~6之间随机的点数"""
        return randint(1, self.num_sides)
