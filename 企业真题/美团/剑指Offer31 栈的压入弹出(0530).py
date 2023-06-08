# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。

# 例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

# 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1


def validateStackSequences(pushed, popped):
    stack = []  # 模拟栈
    i = 0  # 弹出序列的索引

    for num in pushed:
        stack.append(num)  # 将数字入栈

        while stack and stack[-1] == popped[i]:
            stack.pop()  # 栈顶元素与弹出序列相同，弹出栈顶元素
            i += 1  # 更新弹出序列的索引

    return len(stack) == 0  # 如果栈为空，则弹出序列有效


# 测试用例
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validateStackSequences(pushed, popped))  # 输出: True

pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(validateStackSequences(pushed, popped))  # 输出: False
















