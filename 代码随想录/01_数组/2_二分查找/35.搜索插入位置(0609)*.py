# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 你可以假设数组中无重复元素。

# 示例 1:

# 输入: [1,3,5,6], 5
# 输出: 2

# 示例 2:

# 输入: [1,3,5,6], 2
# 输出: 1

# 示例 3:

# 输入: [1,3,5,6], 7
# 输出: 4

# 示例 4:

# 输入: [1,3,5,6], 0
# 输出: 0

'''===============First Try 0609 二分法====================='''
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right=0, len(nums)
#         while left<=right:
#             middle =  left + (right - left) // 2
#             if nums[middle] > target:
#                 right = middle - 1  # target在左区间，所以[left, middle - 1]
#             elif nums[middle] < target:
#                 left = middle + 1  # target在右区间，所以[middle + 1, right]
#             elif nums[middle] == target:
#                 return middle  # 数组中找到目标值，直接返回下标
#             else:
#                 pass # 0609 不会了.......
            
#         return -1  # 未找到目标值

'''===============Second Try 0609 题解 暴力====================='''
from ast import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target: # 由于是排序的数据，遍历的时候，一旦发现大于等于目标值，即可返回
                return i # 结束循环,返回目标值
        
        return nums.size() # 遍历完整个数组后仍然未得到说明这个值在末尾

# 时间复杂度：O(n)
# 空间复杂度：O(1)

'''===============Second Try 0609 题解 二分法====================='''
# 关键点:想清楚四种情况
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        while left<=right:
            middle =  left + (right - left) // 2 # 前面这些闭区间的操作还是一样的套路0609
            if nums[middle] > target:
                right = middle - 1  # target在左区间，所以[left, middle - 1]
            elif nums[middle] < target:
                left = middle + 1  # target在右区间，所以[middle + 1, right]
            else:
                return middle  # 数组中找到目标值，直接返回下标

    #    // 分别处理如下四种情况
    #         // 目标值在数组所有元素之前  [0, -1] right=-1>>>>right + 1
    #         // 目标值等于数组中某一个元素  return middle; 
    #         // 目标值插入数组中的位置 [left, right]，return  right + 1 right=-1>>>>right + 1
    #         // 目标值在数组所有元素之后的情况 [left, right]， 因为是右闭区间，所以 return right + 1
        return right + 1 # 这一点是关键,没有想明白,前面的操作和704都是一样的 0609
















