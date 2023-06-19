# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-common-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1)+1, len(text2)+1 # 
        dp = [[0 for _ in range(len1)] for _ in range(len2)] # 先对dp数组做初始化操作
        for i in range(1, len2):
            for j in range(1, len1): # 开始列出状态转移方程
                if text1[j-1] == text2[i-1]: # Jack 确定dp数组及其下标含义：
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # Jack 不一致，取最长公共子序列
        return dp[-1][-1] # 表示二维动态规划数组（或矩阵）中的最后一个元素

# 1. 长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]





solver = Solution()

solver








