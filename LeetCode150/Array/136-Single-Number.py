"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once."""

def SingleNumber_XOR(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res

def SingleNumber(nums):
    freq_map = {}
    for i in range(len(nums)):
        if nums[i] in freq_map:
            # freq_map[nums[i]] += 1
            del freq_map[nums[i]]
        else:
            freq_map[nums[i]] = 1
    for j in freq_map:
        return j
    # for key, value in freq_map.items():
    #     if value == 1:
    #         return key

if __name__ == '__main__':
    # nums = [2,2,1]
    nums = [4,1,2,1,2]
    # nums = [1]
    print(SingleNumber(nums))
    print(SingleNumber_XOR(nums))