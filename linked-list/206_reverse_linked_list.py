from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def to_a(self):
        a = [ self.val ]
        a_digit = self
        while a_digit.next:
            a.append(a_digit.next.val)
            a_digit = a_digit.next
        return a
class Solution:
    def rev(self, head: ListNode) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            nextTmp = current.next
            current.next = prev
            prev = current
            current = nextTmp
        return prev

from random import randint
a_len = 7
a_node = ListNode()
a_node.val = randint(1, 9)
while a_len > 1:
    a_len -= 1
    a_node_new = ListNode()
    a_node_new.val = randint(0, 9)
    a_node_new.next = a_node
    a_node = a_node_new


print(Solution().rev(a_node).to_a())
        