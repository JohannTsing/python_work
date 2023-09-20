"""生成散点图，折线图"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from random_walk import RandomWalk


def scatter_test():
    """绘制随机漫步散点图"""
    while True:
        # 创建 RandomWalk 实例
        rw = RandomWalk(50_000)
        rw.fill_walk()

        # Matplotlib默认不支持中文字符，需要设置支持中文的字体
        font = fm.FontProperties(fname=r'C:\Windows\Fonts\SimHei.ttf')

        # 将所有的点绘制出来
        plt.style.use('seaborn')
        # 创建图表时，可传递参数figsize以指定生成的图形的尺寸。
        # 给参数figsize指定一个元组，向Matplotlib指出绘图窗口的尺寸，单位为英寸
        # Matplotlib假定屏幕分辨率为100像素/英寸,可通过参数dpi传递该分辨率
        fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

        # 使用颜色映射，根据漫步点生成的先后顺序来着色。
        # 传递实参edgecolors='none'以删除每个点周围的轮廓
        point_numbers = range(rw.num_points)
        # ax.scatter(rw.x_value, rw.y_value, s=5)
        ax.scatter(rw.x_value,
                   rw.y_value,
                   c=point_numbers,
                   cmap=plt.cm.Reds,
                   edgecolors='none',
                   s=1)

        # 突出起点和终点
        ax.scatter(rw.x_value[0],
                   rw.y_value[0],
                   c='green',
                   edgecolors='none',
                   s=100)
        ax.scatter(rw.x_value[-1],
                   rw.y_value[-1],
                   c='yellow',
                   edgecolors='none',
                   s=100)

        # 隐藏坐标轴
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_title("随机漫步散点图", fontproperties=font, fontsize=20)

        plt.show()

        # keep_running = input("continue? y/n: ")
        # if 'n' == keep_running:
        #     break
        break


def plot_test():
    """绘制模拟分子运动的折线图"""
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Matplotlib默认不支持中文字符，需要设置支持中文的字体
    font = fm.FontProperties(fname=r'C:\Windows\Fonts\SimHei.ttf')

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    plt.figure

    # 绘制折线图
    point_numbers = range(rw.num_points)
    print(type(point_numbers))
    ax.plot(rw.x_value, rw.y_value, color='c', label='line 1', linewidth=0.7)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_title("分子运动折线图", fontproperties=font, fontsize=20)
    plt.show()


# scatter_test()
plot_test()
