# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

# root = TreeNode(4)
# t1 = TreeNode(2)
# t2 = TreeNode(7)

# root.left = t1
# root.right = t2

# t3 = TreeNode(1)
# t4 = TreeNode(3)
# t5 = TreeNode(6)
# t6 = TreeNode(9)

# t1.left = t3
# t1.right = t4
# t2.left = t5
# t2.right = t6

# s = Solution()
# x = s.invertTree(root)
# # To make sure that the root node's left and right nodes are inverted.
# print(x.left.val, x.right.val)