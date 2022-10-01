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
            # print("tmp", nextTmp.to_a() if nextTmp else [])
            current.next = prev
            # print("current", current.to_a() if current else [])
            prev = current
            current = nextTmp
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmp_head = head
        left_minus_one = None
        right_plus_one = None

        start_node = head

        i = 0
        while tmp_head:
            i += 1
            if i == left - 1:
                left_minus_one = tmp_head
                tmp_head = tmp_head.next
                start_node = tmp_head
                left_minus_one.next = None
            elif i == right:
                right_plus_one = tmp_head.next
                tmp_head.next = None
                break
            else:
                tmp_head = tmp_head.next
        # print(head.to_a() if left_minus_one else []) 
        # print(start_node.to_a() if start_node else [])
        start_node = self.rev(start_node)
        
        if right_plus_one:
            current = start_node
            while True:
                if not current.next:
                    current.next = right_plus_one
                    break
                current = current.next
        if left_minus_one:
            left_minus_one.next = start_node
        else:
            head = start_node

        # print(right_plus_one.to_a() if right_plus_one else [])
        return head
        
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

print(a_node.to_a())
print(Solution().reverseBetween(a_node, 2, 4).to_a())