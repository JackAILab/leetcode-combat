# 这段代码通过两次二分查找来找到目标值的第一次和最后一次出现的索引，
# 然后计算它们之间的差值并加1，得到目标值在数组中出现的次数。
# 如果目标值在数组中不存在，那么返回0。

def countOccurrences(nums, target):
    left = 0
    right = len(nums) - 1
    firstOccurrence = findFirstOccurrence(nums, target, left, right)
    
    if firstOccurrence == -1:
        return 0
    
    lastOccurrence = findLastOccurrence(nums, target, firstOccurrence, right)
    
    return lastOccurrence - firstOccurrence + 1

def findFirstOccurrence(nums, target, left, right):
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    return -1

def findLastOccurrence(nums, target, left, right):
    while left < right:
        mid = left + (right - left + 1) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
    if nums[right] == target:
        return right
    return -1

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
