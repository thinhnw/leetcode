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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a_len = b_len = 0

        while True:
            a_len += 1
            if not a_digit.next:
                break
            a_digit = a_digit.next

        while b_digit:
            b_len += 1
            if not b_digit.next:
                break
            b_digit = b_digit.next

        if a_len < b_len:
            a_digit, b_digit = b_digit, a_digit
            a_len, b_len = b_len, a_len
            l1, l2 = l2, l1
        
        while b_len < a_len:
            b_digit.next = ListNode()
            b_digit = b_digit.next
            b_len += 1

        a_digit, b_digit = l1, l2
        carry = 0
        while True:
            a_digit.val += b_digit.val + carry
            if a_digit.val > 9:
                a_digit.val %= 10
                carry = 1
            else:
                carry = 0
            if not a_digit.next:
                break
            a_digit = a_digit.next
            b_digit = b_digit.next
        if carry:
            a_digit.next = ListNode(1)
        return l1

from random import randint
a_len = 7
b_len = 7
a_node = ListNode()
a_node.val = randint(1, 9)
b_node = ListNode()
b_node.val = randint(1, 9)
while a_len > 1:
    a_len -= 1
    a_node_new = ListNode()
    a_node_new.val = randint(0, 9)
    a_node_new.next = a_node
    a_node = a_node_new
while b_len > 1:
    b_len -= 1
    b_node_new = ListNode()
    b_node_new.val = randint(0, 9)
    b_node_new.next = b_node
    b_node = b_node_new

print(a_node.to_a())
print(b_node.to_a())
print(Solution().addTwoNumbers(a_node, b_node).to_a())
