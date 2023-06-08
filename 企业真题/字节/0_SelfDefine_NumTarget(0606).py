# 这段代码通过两次二分查找来找到目标值的第一次和最后一次出现的索引，
# 然后计算它们之间的差值并加1，得到目标值在数组中出现的次数。
# 如果目标值在数组中不存在，那么返回0。

def countOccurrences(nums, target):
    left = 0  # 左边界的索引
    right = len(nums) - 1  # 右边界的索引
    firstOccurrence = findFirstOccurrence(nums, target, left, right)  # 找到目标值的第一次出现的索引
    
    if firstOccurrence == -1:
        return 0
    
    lastOccurrence = findLastOccurrence(nums, target, firstOccurrence, right)  # 找到目标值的最后一次出现的索引
    
    return lastOccurrence - firstOccurrence + 1  # 计算目标值在数组中出现的次数

def findFirstOccurrence(nums, target, left, right):
    while left < right:  # 当左边界小于右边界时循环
        mid = left + (right - left) // 2  # 取中间索引
        if nums[mid] < target:  # 如果中间值小于目标值
            left = mid + 1  # 更新左边界为中间索引+1
        else:
            right = mid  # 否则，更新右边界为中间索引
    if nums[left] == target:  # 如果左边界对应的值等于目标值
        return left  # 返回左边界
    return -1  # 否则，返回-1，表示目标值不存在于数组中

def findLastOccurrence(nums, target, left, right):
    while left < right:  # 当左边界小于右边界时循环
        mid = left + (right - left + 1) // 2  # 取中间索引
        if nums[mid] > target:  # 如果中间值大于目标值
            right = mid - 1  # 更新右边界为中间索引-1
        else:
            left = mid  # 否则，更新左边界为中间索引
    if nums[right] == target:  # 如果右边界对应的值等于目标值
        return right  # 返回右边界
    return -1  # 否则，返回-1，表示目标值不存在于数组中


# 这段代码中，我们首先定义了两个辅助函数 findFirstOccurrence 和 findLastOccurrence 来找到目标值的第一次和最后一次出现的索引。
# 然后，countOccurrences 函数使用这些索引计算目标值在数组中出现的次数。

# 测试用例
nums = [1, 2, 2, 2, 3, 4, 4, 5]
target = 2
print(countOccurrences(nums, target))  # 输出: 3

nums = [1, 2, 2, 2, 3, 4, 4, 5]
target = 4
print(countOccurrences(nums, target))  # 输出: 2

nums = [1, 2, 2, 2, 3, 4, 4, 5]
target = 6
print(countOccurrences(nums, target))  # 输出: 0

