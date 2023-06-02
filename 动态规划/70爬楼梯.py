# 1. 0602 Jack DP(Dynamic Programming)
# (1) Step1: 确定dp数组以及下标的含义: dp[i], 爬到有i个台阶的楼顶，有dp[i]种方法
# (2) Step2: 确定递推公式(递推公式一般都是dp[i] += dp[i - nums[j]]): 
# dp[i]有几种来源，dp[i - 1]，dp[i - 2] 等等，即：dp[i - j]. (nums为输入的数组,这里只有1/2)
# 因此递推公式为：dp[i] += dp[i - j]
# (3) Step3: dp数组如何初始化：既然递归公式是 dp[i] += dp[i - j]，那么dp[0] 一定为1
# dp[0]是递归中一切数值的基础所在，如果dp[0]是0的话，其他数值都是0了。
# (4) Step4: 确定遍历顺序
# 背包里求排列问题，即：1、2 步 和 2、1 步都是上三个台阶，但是这两种方法不一样！
# 所以需将target放在外循环，将nums放在内循环。
# (5) Step5: 举例来推导dp数组


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1) # 初始化dp数组
        dp[0] = 1 # 初始化背包
        m = 2 # 最大爬台阶
        # 遍历背包
        for j in range(n+1):
            # 遍历物品
            for step in range(1, m+1):
                if j >= step:
                    dp[j] += dp[j-step]
        
        return dp[n]



