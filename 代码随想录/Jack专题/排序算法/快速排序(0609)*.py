def quickSort(arr):
    # 判断数组长度是否小于等于1，如果是则已排序完成
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素
    pivot = arr[len(arr) // 2]
    
    # 初始化左右子数组
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归对左右子数组进行快速排序
    left = quickSort(left)
    right = quickSort(right)
    
    # 合并左子数组、中间元素和右子数组
    return left + middle + right


# 测试用例
arr = [6, 8, 3, 9, 2, 1, 7, 5, 4]
sorted_arr = quickSort(arr)
print(sorted_arr)


'''
0609
'''














