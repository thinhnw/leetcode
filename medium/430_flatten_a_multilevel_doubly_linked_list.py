"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:    
    def flatten_and_return_left_right(self, node):
        current = node
        while current:
            nextTmp = current.next
            if current.child:
                left, right = self.flatten_and_return_left_right(current.child)
                current.child = None
                current.next = left
                left.prev = current
                right.next = nextTmp
                if nextTmp:                    
                    nextTmp.prev = right
                current = right
            if current.next:
                current = current.next
            else:
                return [node, current]
            
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':        
        if head:
            return self.flatten_and_return_left_right(head)[0]
        return None