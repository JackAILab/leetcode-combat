# 将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。

# 对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

# 特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。

#  示例 1：
# 输入：root = [4,2,5,1,3] 
# 输出：[1,2,3,4,5]

# 示例 2：
# 输入：root = [2,1,3]
# 输出：[1,2,3]

# 示例 3：
# 输入：root = []
# 输出：[]
# 解释：输入是空树，所以输出也是空链表。

# 示例 4：
# 输入：root = [1]
# 输出：[1]


# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 思路和心得：

# 1.BST的LNR就是有序的。一般就用中序LNR

# 2.全局指针

# 3.dfs的过程其实就是思路

# 作者：HanXin_HanXin
# 链接：https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/solution/c-python3-zhong-xu-huan-xu-zhong-xu-jie-y04fh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

from tables import Node

class Solution:
    def dfs_LNR(self, rt: 'Node') -> None:
        if rt:
            self.dfs_LNR(rt.left)

            if self.last:           #左子不空，从全局的中序遍历，已经遍历完last了，当前rt要和last链接起来
                self.last.right = rt
                rt.left = self.last
            else:                   #左子为空
                self.first = rt
            
            self.last = rt          #rt也在全局范围内统计了，成为统计好的最后一个

            self.dfs_LNR(rt.right)

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        self.first = None
        self.last = None

        self.dfs_LNR(root)

        self.first.left = self.last     #首尾链接起来
        self.last.right = self.first

        return self.first               #返回头




# 将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。

# 对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

# 特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。


# Python3 中序遍历
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head = Node(-1)
        pre = head
        def inorder(root):
            nonlocal pre
            if not root:
                return
            inorder(root.left)
            pre.right = root
            root.left = pre
            pre = pre.right
            inorder(root.right)
        inorder(root)
        head.right.left = pre
        pre.right = head.right
        return head.right


# 输入：root = [2,1,3]
# 输出：[1,2,3]
















