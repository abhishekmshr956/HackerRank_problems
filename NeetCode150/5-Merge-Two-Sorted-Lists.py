""" Merge two sorted lists (https://leetcode.com/problems/merge-two-sorted-lists/)
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""
def mergeTwoLists(list1, list2):
    m = len(list1)
    n = len(list2)
    i, j, k = 0,0,0
    c = []
    for _ in range(m+n):
        if k >= m+n:
            return c
        elif i == m:
            c.extend(list2[j:])
            k += n - j
        elif j == n:
            c.extend(list1[i:])
            k += m - i
        elif list1[i] < list2[j]:
            c.append(list1[i])
            i, k = i+1, k+1
        else:
            c.append(list2[j])
            j, k = j+1, k+1
    return c

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         dummy = ListNode()
#         tail = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next

#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2

#         return dummy.next


list1 = [1,2,4]
list2 = [1,3,4]
list1 = []; list2 = []
list1 = []; list2 = [0]
print(mergeTwoLists(list1, list2))