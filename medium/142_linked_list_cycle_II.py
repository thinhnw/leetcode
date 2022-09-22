# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        turtle = head
        hare = head
        
        while turtle and hare:
            turtle = turtle.next
            hare = hare.next
            if not hare:
                return None
            hare = hare.next
            if not hare:
                return None
            if hare == turtle:
                p1 = head
                p2 = hare                
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next                    
                return p1
            
        return None