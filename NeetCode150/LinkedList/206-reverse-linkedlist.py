"""
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional
class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = None

    def __str__(self):
        s = ''
        current = self
        while current:
            if current.next == None:
                s += f'{current.val}'
            else:
                s += f'{current.val} -> '
            current = current.next
        return s

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(head)
    
    s = Solution()
    reversed_head = s.reverseList(head)
    print(reversed_head)
    




