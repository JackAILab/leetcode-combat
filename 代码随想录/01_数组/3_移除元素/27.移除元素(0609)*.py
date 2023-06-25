# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。

# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

# 示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。

# 示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

# 你不需要考虑数组中超出新长度后面的元素。


# nums = [0,1,2,2,3,0,4,2]

# val = 2

'''=============================================Error======================================'''

from ast import List


nums = [3,2,2,3]
val = 3

def move(nums, val):
    count = 0
    new_nums = []
    for i in range(len(nums)):
        if nums[i] is not val:
            new_nums.append(nums[i]) # 不要使用额外的数组空间 这里出 BUG 了
            count = count + 1

    return new_nums, count


new_nums, count = move(nums, val)
print(new_nums)
print(count)



'''========================Version 1 暴力 BUG 0609============================================'''
nums = [0,1,2,2,3,0,4,2]

val = 2

def move(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] is val:
            for j in range(i+1,len(nums)):
                nums[j-1]=nums[j] # 删除当前这个节点
                count = count+1 # 删除的节点数加一
    return len(nums)-count                

'''暴力  参考代码'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val: # 找到等于目标值的节点
                for j in range(i+1, l): 
                    nums[j - 1] = nums[j] # 覆盖该元素，并将后面元素向前平移
                l -= 1
                i -= 1 # BUG 这里是关键，要往前回溯一个值 0609
            i += 1
        return l

# 时间复杂度：O(n^2)
# 空间复杂度：O(1)

'''========================Version 2 双指针 ============================================'''

# 总结: 快指针一直往前走寻找新元素, 慢指针指向待更新的元素(比如本次指向的元素是目标元素,下一次快指针的元素若不是目标元素就会覆盖掉这个慢指针的目标元素,下一次快指针的元素仍然是目标元素的话就继续等待更新)
# nice的课程讲解: https://www.bilibili.com/video/BV12A4y1Z7LP/?vd_source=8f32c6c69c90af448f6be495aeb15c05

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(nums): # 快指针一直往前走
            if nums[fast] is not val: # 快指针指向的不是目标元素,slow和fast均进行++,同时将fast指向的数据替换掉slow指向的数据
                nums[slow]=nums[fast] 
                slow+=1 
        return slow


'''双指针  参考代码'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# 时间复杂度：O(n)
# 空间复杂度：O(1)

# 要知道数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖。









