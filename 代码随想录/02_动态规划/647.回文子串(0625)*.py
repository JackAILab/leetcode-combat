# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

# 回文字符串 是正着读和倒过来读一样的字符串。
# 子字符串 是字符串中的由连续字符组成的一个序列。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

# 示例 1：
# 输入："abc"
# 输出：3 ###
# 解释：三个回文子串: "a", "b", "c"

# 示例 2：
# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
# 提示：输入的字符串长度不会超过 1000 。

# 代码随想录: https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序,和1143最长公共子序列不同,这里需要从右下往左上遍历(要由i+1,j-1推向i,j)
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                        print(s[i:j+1]) # 辅助理解
                    elif dp[i+1][j-1]: #情况三
                        result += 1
                        dp[i][j] = True 
                        print(s[i:j+1]) # 辅助理解
        # print(dp) # 辅助理解
        return result
    

a = Solution()

str = "bbab"

result = a.countSubstrings(str)
print(result)








'''===================================== 笔记0625 ============================================='''
'''
最长公共子序列问题:0625
讲解笔记
https://www.bilibili.com/video/BV17G4y1y7z9/?spm_id_from=333.337.search-card.all.click&vd_source=8f32c6c69c90af448f6be495aeb15c05

(1) dp定义
dp[i][j] 定义为字符串s [i,j] 范围内的是否是回文子串
使用辅助变量result记录子串数量

(2) 递推公式
i==j,只有一个字符a; 
i和j仅仅相差一个字符aa；
j-i>1则判断dp[i+1][j-1]是否是True

[第1/2种情况]:
j-i <=1
dp[i][j]一定为True
result变量:发现一个回文子串则++

[第3种情况]:
j-i >1
判断 dp[i+1][j-1] 为True, 则发现回文子串
这里 dp[i+1][j-1] 是由上一步的(1/2情况)中 dp[i][j] 中赋值为True的
因为i是在不断递减的,j是在不断递增的,所以上一步的i是覆盖了下一步的i+1,下一步的j-1相当于上一步的j

(3) 初始化
只能都初始化为False,不然会混乱


(4) 遍历顺序
注意是从左下往右上递推的,因此s的遍历应该为
i从后向先遍历   range(len(s)-1, -1, -1)
j在i的基础上从前往后遍历  range(i, len(s)):
dp[i+1][j-1] 推  dp[i][j]
![递推map](https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306251653872.png)
![总结](https://jack-1310222578.cos.ap-guangzhou.myqcloud.com/typora_PicGo/202306251654776.png)
比如bbab字符串, i=2,j=2时, dp[i][j]被赋值为True
当遍历到i=1,j=3时, 子字符串为bab, dp[i+1][j-1]即dp[2][2], 即判断这个更长的字符串中包含的子字符串是否是回文(根据上一步判断)

所以这里包含了一种递推关系,即由 dp[i][j] (内部更小的) 的关系外推 dp[i-1][j+1] (外部更大的)

[BUG] 因此, 循环应该是从 外部i不断往回减, j在i的基础上不断增加, 相当于一个动态判别窗口, 从末尾往前移动, 窗口会不断扩大(想象一下这个画面,这题你就背下来了)

(5) 打印dp


'''

