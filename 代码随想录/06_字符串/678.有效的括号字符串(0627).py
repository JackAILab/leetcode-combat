'''
给你一个只包含三种字符的字符串，支持的字符类型分别是 '('、')' 和 '*'。请你检验这个字符串是否为有效字符串，如果是有效字符串返回 true 。

有效字符串符合如下规则：

任何左括号 '(' 必须有相应的右括号 ')'。
任何右括号 ')' 必须有相应的左括号 '(' 。
左括号 '(' 必须在对应的右括号之前 ')'。
'*' 可以被视为单个右括号 ')' ，或单个左括号 '(' ，或一个空字符串。
一个空字符串也被视为有效字符串。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "(*)"
输出：true

示例 3：
输入：s = "(*))"
输出：true

提示：
1 <= s.length <= 100
s[i] 为 '('、')' 或 '*'

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-parenthesis-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []                         #第一个栈用来记录所有(的index
        star_stack = []                    #第二个栈用来记录所有*的index
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if not stack and not star_stack:
                    return False                        #如果直接读到)，直接return False
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()                    #先用(来消)，再用*来消)
        while stack and star_stack:
            if stack.pop() > star_stack.pop():          #在所有)都处理了之后，只需要考虑(和*的index，此时的*全部当作)来考虑，比较index即可
                return False
        return not stack                   #判断是否有多余的(

# 作者：leon_qin
# 链接：https://leetcode.cn/problems/valid-parenthesis-string/solution/pythonzhan-shi-xian-by-leoeoeon/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


























































