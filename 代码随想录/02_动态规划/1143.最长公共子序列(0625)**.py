# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-common-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len1, len2 = len(text1)+1, len(text2)+1 

        dp = [[0 for _ in range(len1)] for _ in range(len2)] # 先对dp数组做初始化操作 shape = [4,6]

        for i in range(1, len2):
            for j in range(1, len1): # 逐行扫描,大脑里面要有那个矩阵:https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306192334630.png or ![代码随想录递推关系图](https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306251801010.png)
                if text1[j-1] == text2[i-1]: # 第一种情况
                    dp[i][j] = dp[i-1][j-1]+1 # 末尾字符相同,各自减一个字符再去求LCS
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 第二种情况,在最大的基础上再继续LCS
        return dp[-1][-1] # 表示二维动态规划数组（或矩阵）中的最后一个元素,因为LCS问题是不断累加的问题,所以最后一个元素一定就是结果了

# 1. 长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]





solver = Solution()
text1 = "abcde"
text2 = "ace" 
print(solver.longestCommonSubsequence(text1,text2))



























'''===================================== 笔记0619 ============================================='''
'''
最长公共子序列问题:0619
讲解笔记
https://www.bilibili.com/video/BV1ey4y1d7oD/?spm_id_from=333.337.search-card.all.click&vd_source=8f32c6c69c90af448f6be495aeb15c05

(1) 定义
经典LCS问题! 定义dp[i][j]定义为字符串str1的第i个字符和字符串的第j个字符是否相等
关键是找出状态方程,然后递归相加即可!一般是需要分解为若干个子问题,如下.
(2) 分解
[第一种情况]: 重点就是找到一个递推的关系!当某2个字符相等时,他们之前的一段字符(表示为dp[i-1][j-1])也相等,那么这一串就是最长公共子序列了!
从最后一个情况看,往回推! S1的最后一个字符与S2的最后一个字符相等，那么只需要继续去求前面i-1和j-1字符串中的LCS长度即可 \
[第二种情况]:
S1的最后一个字符与S2的最后一个字符不相等，那么就要么把S1的末尾字符舍弃掉，要么把S2的末尾字符舍弃掉 \
问题就转换为求S1'和S2'的LCS长度,这里就取max即可!

(3) 子问题
初始,开头的字符串
'''






