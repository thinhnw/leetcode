# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0
        cur = head
        while cur:
            m += 1
            cur = cur.next
        if n == m:
            return head.next
        i = 0
        cur = head
        while cur:
            i += 1
            if i == m - n:
                cur.next = cur.next.next
                break
            cur = cur.next
        
        return head