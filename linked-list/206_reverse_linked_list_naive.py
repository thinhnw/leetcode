# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_a(self):
        a = [ self.val ]
        cur = self
        while cur.next:
            a.append(cur.next.val)
            cur = cur.next
        return a


def insert_end(head: ListNode, node: ListNode):
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = node
    node.next = None
    return head


class Solution:
           
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        return insert_end(self.reverseList(head.next), head)
    

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)

print(ll.to_a())

print(Solution().reverseList(ll).to_a())