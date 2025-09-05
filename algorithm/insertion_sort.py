# 插入排序 (Insertion Sort)
# 核心思想：将元素逐个插入到已排序部分的正确位置，类似于整理扑克牌。
# 时间复杂度：最好情况O(n)（已排序），平均情况O(n²)，最坏情况O(n²)。

def insertion_sort(arr):
    """
    插入排序函数，对整数列表进行原地排序。

    参数：
    arr (list): 需要排序的整数列表。

    返回：
    None: 函数直接修改输入列表。
    """
    n = len(arr)  # 获取列表长度
    for i in range(1, n):  # 从第二个元素开始遍历
        key = arr[i]  # 当前要插入的元素
        j = i - 1  # 已排序部分的最后一个元素的索引
        # 将大于key的元素向右移动，为key腾出位置
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 移动元素
            j -= 1  # 继续向左比较
        arr[j + 1] = key  # 将key插入到正确位置

# 测试示例
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]  # 定义一个无序整数列表
    print("排序前:", test_arr)  # 打印排序前的列表
    insertion_sort(test_arr)  # 调用排序函数
    print("排序后:", test_arr)  # 打印排序后的列表