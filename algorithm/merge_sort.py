# 归并排序 (Merge Sort)
# 核心思想：将数组递归分成两半，分别排序后再合并两个有序子数组。
# 时间复杂度：最好情况O(n log n)，平均情况O(n log n)，最坏情况O(n log n)。

def merge(left, right):
    """
    合并两个已排序的列表。

    参数：
    left (list): 左半部分已排序列表。
    right (list): 右半部分已排序列表。

    返回：
    list: 合并后的有序列表。
    """
    result = []  # 结果列表
    i = j = 0  # 左右列表的指针
    while i < len(left) and j < len(right):  # 比较并合并
        if left[i] <= right[j]:
            result.append(left[i])  # 添加左边元素
            i += 1
        else:
            result.append(right[j])  # 添加右边元素
            j += 1
    result.extend(left[i:])  # 添加剩余左边元素
    result.extend(right[j:])  # 添加剩余右边元素
    return result

def merge_sort(arr):
    """
    归并排序函数，对整数列表进行排序。

    参数：
    arr (list): 需要排序的整数列表。

    返回：
    list: 排序后的新列表（不修改原列表）。
    """
    if len(arr) <= 1:  # 递归终止条件
        return arr
    mid = len(arr) // 2  # 找到中间点
    left = merge_sort(arr[:mid])  # 递归排序左半部分
    right = merge_sort(arr[mid:])  # 递归排序右半部分
    return merge(left, right)  # 合并结果

# 测试示例
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]  # 定义一个无序整数列表
    print("排序前:", test_arr)  # 打印排序前的列表
    sorted_arr = merge_sort(test_arr)  # 调用排序函数，返回新列表
    print("排序后:", sorted_arr)  # 打印排序后的列表