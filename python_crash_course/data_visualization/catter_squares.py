import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def scatter_test(x, y):
    """使用 scatter() 绘制散点图并设置样式"""

    # Matplotlib默认不支持中文字符，需要设置支持中文的字体
    font = fm.FontProperties(fname=r'C:\Windows\Fonts\SimHei.ttf')

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    # 使用 scatter() 绘制单个点，需要传入X轴和Y轴的坐标值。
    # 使用参数s设置绘制图形时使用的点的尺寸。
    # 使用参数c设置点的颜色，既可以使用颜色名称，也可以使用RGB元组，元组包含三个0~1的小数值，值越接近0，指定的颜色越深；值越接近1，指定的颜色越浅
    # ax.scatter(x, y, c='green', s=5)
    # ax.scatter(x, y, c=(0, 0.5, 0), s=5)

    # 颜色映射（colormap）是一系列颜色，从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律。
    # 将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。
    ax.scatter(x, y, c=y, cmap=plt.cm.Greens, s=5)

    # 设置标题，并给坐标轴添加标签
    ax.set_title("平方数", fontproperties=font, fontsize=20)
    ax.set_xlabel("值", fontproperties=font, fontsize=14)
    ax.set_ylabel("值的平方", fontproperties=font, fontsize=14)

    # 设置刻度标记大小
    ax.tick_params(axis='both', which='major', labelsize=12)

    # 设置每个坐标轴的取值范围
    ax.axis([0, 1100, 0, 1100000])

    # show()打开Matplotlib查看器并显示绘制的图表
    # plt.show()

    # 自动保存图表。第一个实参指定要以什么文件名保存图表，该文件将存储到当前py文件所在的目录。第二个实参指定将图表多余的空白区域裁剪掉（可省略）。
    plt.savefig('square_plot.png', bbox_inches='tight')


# 绘制单个点
# scatter_test(2, 4)

# 绘制一系列点
# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
# scatter_test(x_value, y_value)
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
scatter_test(x_values, y_values)
