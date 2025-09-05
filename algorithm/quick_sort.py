# 快速排序 (Quick Sort)
# 核心思想：选择一个基准元素，将数组分为小于基准和大于基准的两部分，递归对两部分排序。
# 时间复杂度：最好情况O(n log n)，平均情况O(n log n)，最坏情况O(n²)（当数据已排序时）。

def partition(arr, low, high):
    """
    分区函数，选择基准元素并将数组分为两部分。

    参数：
    arr (list): 需要分区的列表。
    low (int): 分区起始索引。
    high (int): 分区结束索引。

    返回：
    int: 基准元素的最终位置索引。
    """
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # i指向小于基准的区域末尾
    for j in range(low, high):  # 遍历从low到high-1的元素
        if arr[j] <= pivot:  # 如果当前元素小于等于基准
            i += 1  # 扩展小于区域
            arr[i], arr[j] = arr[j], arr[i]  # 交换
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 将基准放到正确位置
    return i + 1  # 返回基准位置

def quick_sort(arr, low=0, high=None):
    """
    快速排序函数，对整数列表进行原地排序。

    参数：
    arr (list): 需要排序的整数列表。
    low (int): 排序起始索引，默认0。
    high (int): 排序结束索引，默认len(arr)-1。

    返回：
    None: 函数直接修改输入列表。
    """
    if high is None:
        high = len(arr) - 1  # 设置默认high
    if low < high:  # 递归终止条件
        pi = partition(arr, low, high)  # 获取分区索引
        quick_sort(arr, low, pi - 1)  # 递归排序左部分
        quick_sort(arr, pi + 1, high)  # 递归排序右部分

# 测试示例
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]  # 定义一个无序整数列表
    print("排序前:", test_arr)  # 打印排序前的列表
    quick_sort(test_arr)  # 调用排序函数
    print("排序后:", test_arr)  # 打印排序后的列表