"""生成投掷骰子的可视化数据"""
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


def die_test():
    # 创建骰子实例
    die = Die()

    # 投掷骰子，并将结果存储在列表中
    results = []
    for roll_num in range(1_000):
        results.append(die.roll())

    # print(results)

    # 分析投掷的结果
    frequencies = {}
    for value in range(1, die.num_sides + 1):
        frequency = results.count(value)
        frequencies[value] = frequency

    print(frequencies)

    # 对结果进行可视化分析
    x_values = list(frequencies.keys())
    y_values = list(frequencies.values())

    # 类Bar()表示用于绘制条形图的数据集，需要一个存储x值的列表和一个存储y值的列表。
    # 这个类必须放在方括号内，因为数据集可能包含多个元素
    data = [Bar(x=x_values, y=y_values)]

    # 每个坐标轴都能以不同的方式进行配置，而每个配置选项都是一个字典元素。这里只设置了坐标轴标签
    x_axis_config = {'title': '结果'}
    y_axis_config = {'title': '结果的频率'}
    # 类Layout()返回一个指定图表布局和配置的对象。这里设置了图表名称，并传入了x轴和y轴的配置字典。
    my_layout = Layout(title='投掷一个D6 1000次的结果',
                       xaxis=x_axis_config,
                       yaxis=y_axis_config)

    # 调用函数offline.plot()来生成图表
    # 这个函数需要一个包含数据和布局对象的字典，还接受一个文件名，指定要将图表保存到哪里。
    offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')


die_test()