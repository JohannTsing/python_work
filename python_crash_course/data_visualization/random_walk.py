"""随机漫步数据生成module"""
from random import choice


class RandomWalk:
    """生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有的随机漫步都始于 (0, 0)
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有的点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_value) < self.num_points:

            # 决定前进的方向，以及沿这个方向前进的距离
            # x_direction = choice([1, -1])
            # x_distance = choice([0, 1, 2, 3, 4])
            # x_step = x_direction * x_distance

            # y_direction = choice([1, -1])
            # y_distance = choice([0, 1, 2, 3, 4])
            # y_step = y_direction * y_distance

            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x,y值。并将其加入到列表中
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)

    def get_step(self):
        """确定随机漫步的点前进的方向，以及沿这个方向前进的距离"""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step