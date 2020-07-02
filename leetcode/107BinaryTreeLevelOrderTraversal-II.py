# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-02 18:01:31 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-02 18:01:31 
#  */
#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        queue = []
        if root:
            queue.append(root)
        res = []
        if root:
            res.append([root.val])
        while queue:
            value = []
            level = []
            for i in queue:
                if i.left != None:
                    level.append(i.left)
                    value.append(i.left.val)
                if i.right != None:
                    level.append(i.right)
                    value.append(i.right.val)
            if value:
                res.append(value)
            queue = level
        return res[::-1]

# if __name__ == "__main__":
#     inputarray = [3,9,20,None,None,15,7]
#     a = TreeNode(5)
#     b = TreeNode(4)
#     c = TreeNode(3,None,a)
#     d = TreeNode(2,b)
#     e = TreeNode(1,c,d)
#     so = Solution()
#     res = so.levelOrderBottom(e)
#     print(res)
