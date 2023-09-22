"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""

# def TwoSum(nums, target):
#     prevmap = {}
#     for i in range(len(nums)):
#         rem = target - nums[i]
#         if rem in prevmap:
#             return prevmap[rem], i
#         else:
#             prevmap[nums[i]] = i

# if __name__ == '__main__':
#     nums = [2,7,11,15]
#     target = 9
#     print(TwoSum(nums, target))

#     nums = [3,2,4]
#     target = 6
#     print(TwoSum(nums, target))

#     nums = [3,3]
#     target = 6
#     print(TwoSum(nums, target))

"""
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
Output: 4"""

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
    return low

# nums = [1,3,5,6]; target = 5 # out: 2
# nums = [1,3,5,6]; target = 2 # out: 1
nums = [1,3,5,6]; target = 7 # out: 4
print(binary_search(nums, target))