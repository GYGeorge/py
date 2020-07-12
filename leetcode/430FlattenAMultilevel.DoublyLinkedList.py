# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-10 19:18:59 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-10 19:18:59 
#  */
#
# leetcode id=430 lang=python
#
# [430] Flatten A Multilevel Doubly Linked List
#
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    @classmethod
    def flatten(self, head: 'Node'):
            
        def searchNode(Node):
            front = Node
            # if front.next:
            #     rear = front.next
            while front:
                if front.child:
                    back = searchNode(front.child)
                    i = front.next
                    front.next =front.child
                    front.child = None
                    front.next.prev = front
                    back.next = i
                    if i:
                        i.prev = back
                Node = front
                front = front.next
            return Node
        searchNode(head)
        return head