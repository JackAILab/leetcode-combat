# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

# 示例 1: 输入: "bbbab" 输出: 4 一个可能的最长回文子序列为 "bbbb"。

# 示例 2: 输入:"cbbd" 输出: 2 一个可能的最长回文子序列为 "bb"。

# 提示：

# 1 <= s.length <= 1000
# s 只包含小写英文字母

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
            
        for i in range(len(s)-1, -1, -1): # ![代码随想录递推关系图](https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306251805850.png)
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        # print(dp) # 辅助理解            
        return dp[0][-1]
    
    



a = Solution()

str = "bbbab"

result = a.longestPalindromeSubseq(str)
print(result)



















'''===================================== 笔记0620 ============================================='''
'''
最长公共子序列问题:0620
讲解笔记
https://www.bilibili.com/video/BV1d8411K7W6/?p=134&spm_id_from=pageDriver
![递推示意图](https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306251754865.png)

(1) dp定义
dp[i][j] 定义为字符串s [i,j] 范围内的最长的回文子序列的长度

(2) 递推公式
第一种情况: si==sj
最长的回文子序列的串长+2

第二种情况: si != sj
dp是递推关系,因此要保留上一个dp的最大值(最长回文)以便下一个dp在这个基础上累加

(3) 初始化
从递推公式：dp[i][j] = dp[i + 1][j - 1] + 2; 可以看出 递推公式是计算不到 i 和j相同时候的情况
当i与j相同，那么dp[i][j]一定是等于1的，即：一个字符的回文子序列长度就是1
其他情况dp[i][j]初始为0就行，这样递推公式：dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]); 中dp[i][j]才不会被初始值覆盖。


(4) 遍历顺序
dp[i][j] 依赖于 dp[i + 1][j - 1] ，dp[i + 1][j] 和 dp[i][j - 1]
所以遍历i的时候一定要从下到上遍历，这样才能保证下一行的数据是经过计算的
![代码随想录递推关系图](https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306251805850.png)

{最长公共子序列那题: 有三个方向可以推出dp[i][j], 因此 这三个方向都是经过计算的数值，所以要从前向后，从上到下来遍历这个矩阵 }


(5) 打印dp





'''

















