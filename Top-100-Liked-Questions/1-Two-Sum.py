"""
Problem: Two Sum (https://leetcode.com/problems/two-sum/):

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example2: 
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution(object):

    # O(n^2)
    def twoSum_slow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i,j)

    # O(n)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevmap = {} # val : index

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in prevmap:
                return (prevmap[diff], i)
            else:
                prevmap[n] = i

# nums, target = [2, 7, 11, 15], 9
# nums, target = [3, 2, 4], 6
nums, target = [3, 3], 6
solution = Solution()
print(solution.twoSum(nums, target))
print(solution.twoSum_slow(nums, target))

    

