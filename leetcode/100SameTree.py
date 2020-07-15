# /*
#  * @Author: gaoyuan
#  * @Date: 2020-07-13 21:27:15
#  * @Last Modified by:   gaoyuan
#  * @Last Modified time: 2020-07-13 21:27:15
#  */
#
# leetcode id= lang=python
#
# [] Same Tree
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def isSameTree(self, p: TreeNode, q: TreeNode):
        def check(a: TreeNode, b: TreeNode):
            if not a and not b:
                return True
            if a and b and p.val == q.val:
                return check(p.left, q.left) and check(p.right, q.right)
            return False
        return check(p, q)