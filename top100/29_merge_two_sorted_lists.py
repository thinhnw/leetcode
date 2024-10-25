from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val > list2.val:
            tmp = list1
            list1 = list2
            list2 = tmp
        
        cur1 = list1
        cur2 = list2        
        while cur1:
            if not cur2:
                return list1            
            if cur2.val >= cur1.val:
                if cur1.next:
                    if cur2.val <= cur1.next.val:
                        next_cur1 = cur1.next
                        next_cur2 = cur2.next
                        cur1.next = cur2
                        cur2.next = next_cur1
                        cur2 = next_cur2
                else:
                    cur1.next = cur2
                    return list1
            
            cur1 = cur1.next

           
        return list1

        