# 选择排序 (Selection Sort)
# 核心思想：每次从剩余未排序元素中选择最小（或最大）元素，放到已排序部分的末尾。
# 时间复杂度：最好情况O(n²)，平均情况O(n²)，最坏情况O(n²)。

def selection_sort(arr):
    """
    选择排序函数，对整数列表进行原地排序。

    参数：
    arr (list): 需要排序的整数列表。

    返回：
    None: 函数直接修改输入列表。
    """
    n = len(arr)  # 获取列表长度
    for i in range(n):  # 外层循环遍历每个位置
        min_index = i  # 假设当前i是剩余元素中的最小值索引
        for j in range(i + 1, n):  # 内层循环从i+1到末尾寻找更小的元素
            if arr[j] < arr[min_index]:  # 如果找到更小的元素，更新最小索引
                min_index = j
        # 将找到的最小元素与当前位置交换
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 测试示例
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]  # 定义一个无序整数列表
    print("排序前:", test_arr)  # 打印排序前的列表
    selection_sort(test_arr)  # 调用排序函数
    print("排序后:", test_arr)  # 打印排序后的列表