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





