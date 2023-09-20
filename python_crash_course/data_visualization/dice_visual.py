"""生成投掷骰子的可视化数据"""
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


def die_test(d1_num_sides, d2_num_sides, roll_nums):
    # 创建两个骰子实例
    die1 = Die(d1_num_sides)
    die2 = Die(d2_num_sides)

    # 投掷骰子，并将结果存储在列表中
    results = []
    for roll_num in range(roll_nums):
        results.append(die1.roll() + die2.roll())

    # print(results)

    # 分析投掷的结果
    frequencies = []
    for value in range(2, die1.num_sides + die2.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    print(frequencies)

    # 对结果进行可视化分析
    x_values = list(range(2, die1.num_sides + die2.num_sides + 1))

    # 类Bar()表示用于绘制条形图的数据集，需要一个存储x值的列表和一个存储y值的列表。
    # 这个类必须放在方括号内，因为数据集可能包含多个元素
    data = [Bar(x=x_values, y=frequencies)]

    # 每个坐标轴都能以不同的方式进行配置，而每个配置选项都是一个字典元素。这里只设置了坐标轴标签
    # dtick属性用于设定x轴显示的刻度间距，Plotly默认只显示某些刻度值，而设置'dtick': 1让Plotly显示每个刻度值。
    x_axis_config = {'title': '结果', 'dtick': 1}
    y_axis_config = {'title': '结果的频率'}
    # 类Layout()返回一个指定图表布局和配置的对象。这里设置了图表名称，并传入了x轴和y轴的配置字典。
    my_layout = Layout(
        title=f'投掷一个D{die1.num_sides}和一个D{die2.num_sides} {roll_nums}次的结果',
        xaxis=x_axis_config,
        yaxis=y_axis_config)

    # 调用函数offline.plot()来生成图表
    # 这个函数需要一个包含数据和布局对象的字典，还接受一个文件名，指定要将图表保存到哪里。
    filename = f"d{die1.num_sides}_d{die2.num_sides}_{roll_nums}.html"
    offline.plot({'data': data, 'layout': my_layout}, filename=filename)


die_test(6, 10, 50000)
