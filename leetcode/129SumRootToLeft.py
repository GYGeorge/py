#  * @Author: gaoyuan
#  * @Date: 2020-07-01 16:57:08
#  * @Last Modified by:   gaoyuan
#  * @Last Modified time: 2020-07-01 16:57:08


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """
        Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
        An example is the root-to-leaf path 1->2->3 which represents the number 123.
        Find the total sum of all root-to-leaf numbers.
    """

    def sumNumbers(self, root: TreeNode):
        self.sum = 0
        self.recursive(root, 0)
        return self.sum

    def recursive(self, node: TreeNode, v):
        if not node:
            return
        node.val += v*10
        if (not node.left) and (not node.right):
            self.sum += node.val
            return
        if node.left != None:
            self.recursive(node.left, node.val)
        if node.right != None:
            self.recursive(node.right, node.val)


if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(1)
    a_b = TreeNode(9, a, b)
    d = TreeNode(0)
    root = TreeNode(4, a_b, d)
    so = Solution()
    so.sumNumbers(root)
