# 冒泡排序 (Bubble Sort)
# 核心思想：通过反复交换相邻的逆序元素，将最大元素逐步“冒泡”到末尾。
# 时间复杂度：最好情况O(n)（已排序），平均情况O(n²)，最坏情况O(n²)。

def bubble_sort(arr):
    """
    冒泡排序函数，对整数列表进行原地排序。

    参数：
    arr (list): 需要排序的整数列表。

    返回：
    None: 函数直接修改输入列表。
    """
    n = len(arr)  # 获取列表长度
    for i in range(n):  # 外层循环控制排序趟数，最多n-1趟
        swapped = False  # 标志位，用于优化：如果一趟没有交换，说明已排序
        for j in range(0, n - i - 1):  # 内层循环比较相邻元素
            if arr[j] > arr[j + 1]:  # 如果前一个元素大于后一个，交换
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换操作
                swapped = True  # 标记发生了交换
        if not swapped:  # 如果没有交换，提前结束
            break

# 测试示例
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]  # 定义一个无序整数列表
    print("排序前:", test_arr)  # 打印排序前的列表
    bubble_sort(test_arr)  # 调用排序函数
    print("排序后:", test_arr)  # 打印排序后的列表