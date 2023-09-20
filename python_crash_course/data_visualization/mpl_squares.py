import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def plot_test(**params):
    """绘制简单的折线图"""

    # Matplotlib默认不支持中文字符，需要设置支持中文的字体
    font = fm.FontProperties(fname=r'C:\Windows\Fonts\SimHei.ttf')

    # 生成的图表使用'seaborn'样式
    plt.style.use('seaborn')

    # input_value = [1, 2, 3, 4, 5]
    # squares = [1, 4, 9, 16, 25]
    input_value = params.get('input_value')
    squares = params.get('squares')

    # subplots() 函数可在一张图片中绘制一个或多个图表。变量fig表示整张图片。变量ax表示图片中的各个图表
    fig, ax = plt.subplots()

    # plot()，它尝试根据给定的数据以有意义的方式绘制图表
    # 参数linewidth，决定了plot()绘制的线条粗细
    # ax.plot(squares, linewidth=3)
    # 向plot()提供一系列数时，它假设第一个数据点对应的X坐标值是 0，为plot()同时提供输入值和输出值
    if input_value:
        ax.plot(input_value, squares, linewidth=3)
    else:
        ax.plot(squares, linewidth=3)

    # set_title() 给图表指定标题
    ax.set_title("平方数", fontproperties=font, fontsize=24)

    # set_xlabel()和set_ylabel()让你能够为每条轴设置标题
    ax.set_xlabel("值", fontproperties=font, fontsize=14)
    ax.set_ylabel("值的平方", fontproperties=font, fontsize=14)

    # tick_params()设置刻度的样式。其中指定的实参将影响X轴和Y轴上的刻度（axes='both'），并将刻度标记的字号设置为14（labelsize=14）。
    ax.tick_params(axis='both', labelsize=14)

    # show()打开Matplotlib查看器并显示绘制的图表
    plt.show()


plot_test(input_value=[1, 2, 3, 4, 5], squares=[1, 4, 9, 16, 25])
