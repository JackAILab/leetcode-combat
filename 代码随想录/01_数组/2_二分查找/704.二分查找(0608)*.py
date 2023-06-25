# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

# 输入: nums = [-1,0,3,5,9,12], target = 9     
# 输出: 4       
# 解释: 9 出现在 nums 中并且下标为 4     

# 输入: nums = [-1,0,3,5,9,12], target = 2     
# 输出: -1        
# 解释: 2 不存在 nums 中因此返回 -1    

# 提示：

# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。


'''===============================My Answer 0608 BUG================================'''
from ast import List


def find_num(nums,target):
    count = 0
    for i in range(len(nums)):      
        if  nums[i] is target:
            return count
        else:
            count = count+1 
    
    if count is len(nums):
        return -1         

nums = [-1,0,3,5,9,12]
target = 9  
a = find_num(nums,target)
print(a)

# BUG ![](https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306082342218.png)

# 大算例好像是通过不了! 0608 具体原因未知

'''=================================二分法 0608====================================='''
# 条件:
# (1) 数组为有序数组
# (2) 数组中无重复元素

# 套路:
# 左闭右闭即[left, right]，或者左闭右开即[left, right)

def search(nums,target): # 左闭右闭区间
        left, right = 0, len(nums) - 1  # 定义target在左闭右闭的区间里，[left, right]

        while left <= right:
            middle = left + (right - left) // 2
            
            if nums[middle] > target:
                right = middle - 1  # target在左区间，所以[left, middle - 1]
            elif nums[middle] < target:
                left = middle + 1  # target在右区间，所以[middle + 1, right]
            else:
                return middle  # 数组中找到目标值，直接返回下标
        return -1  # 未找到目标值

nums = [-1,0,3,5,9,12]
target = 9  
a = search(nums,target)
print(a)













