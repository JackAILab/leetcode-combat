# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

# 示例 1：
# 输入："abc"
# 输出：3
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
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: #情况三
                        result += 1
                        dp[i][j] = True
        return result

















