""" Search Insert Position (https://leetcode.com/problems/search-insert-position/)
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
def searchInsert_Naive(nums, target):
    n = len(nums)
    for i, a in enumerate(nums):
        if target == a:
            return i
        elif target < a:
            return i
    return i+1

def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    while l<=r:
        m = (l + r) // 2
        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m - 1
        else:
            l = m + 1
    return l

nums = [1,3,5,6]; target = 5 # out: 2
# nums = [1,3,5,6]; target = 2 # out: 1
# nums = [1,3,5,6]; target = 7 # out: 4
print(searchInsert_Naive(nums, target))
print(searchInsert(nums, target))