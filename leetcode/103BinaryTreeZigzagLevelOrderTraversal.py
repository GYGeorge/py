# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-22 20:40:30 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-22 20:40:30 
#  */
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    @classmethod
    def zigzagLevelOrder(self, root: TreeNode):
        queue,res = [],[]
        i = 0
        if root:
            queue.append(root)
            res.append([root.val])
        while queue:
            temp=[]
            value = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                    value.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    value.append(node.right.val)
            if not i % 2:
                value.reverse()
            i += 1
            if value: 
                res.append(value)
        queue = temp
        return res                   

if __name__ == "__main__":
    a = TreeNode(15)
    b = TreeNode(7)
    a_b = TreeNode(20, a, b)
    c = TreeNode(9)
    root = TreeNode(3, c, a_b)
    print(Solution.zigzagLevelOrder(root))

