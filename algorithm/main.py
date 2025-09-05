# 主演示文件：展示五种排序算法的运行效果
# 导入所有排序函数
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
import random  # 用于生成随机列表

# 生成一个随机整数列表作为测试数据
def generate_random_list(size=10, min_val=1, max_val=100):
    """
    生成随机整数列表。

    参数：
    size (int): 列表大小，默认10。
    min_val (int): 最小值，默认1。
    max_val (int): 最大值，默认100。

    返回：
    list: 随机整数列表。
    """
    return [random.randint(min_val, max_val) for _ in range(size)]

# 主函数：演示所有排序算法
def main():
    # 生成随机列表
    original_arr = generate_random_list(10, 1, 100)
    print("原始随机列表:", original_arr)
    print("\n--- 排序算法演示 ---\n")

    # 1. 冒泡排序
    arr_copy = original_arr.copy()  # 复制列表，避免修改原列表
    bubble_sort(arr_copy)
    print("冒泡排序结果:", arr_copy)

    # 2. 选择排序
    arr_copy = original_arr.copy()
    selection_sort(arr_copy)
    print("选择排序结果:", arr_copy)

    # 3. 插入排序
    arr_copy = original_arr.copy()
    insertion_sort(arr_copy)
    print("插入排序结果:", arr_copy)

    # 4. 快速排序
    arr_copy = original_arr.copy()
    quick_sort(arr_copy)
    print("快速排序结果:", arr_copy)

    # 5. 归并排序（返回新列表）
    sorted_arr = merge_sort(original_arr)
    print("归并排序结果:", sorted_arr)

# 运行主函数
if __name__ == "__main__":
    main()