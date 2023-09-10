"""
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
def MajorityElement_FollowUp(nums):
    """ solution with O(1) space complexity"""
    res, count = 0, 0
    for n in nums:
        if count == 0:
            res = n
        count += 1 if n == res else -1
        # if n == res:
        #     count += 1
        # else:
        #     count -= 1
    return res


def MajorityElement(nums):
    """ solution using hash map (dictionary)"""
    n = len(nums)
    count_map = {}
    for i in nums:
        count_map[i] = count_map.get(i, 0) + 1
        # if count_map[i] > n//2:
        #     return i
        # if i in count_map:
        #     count_map[i] += 1 
        # else: 
        #     count_map[i] = 1
    for key, value in count_map.items():
        if value > n//2:
            return key
        

# ### solution using count elements        
# def count_elements(n, nums):
#     count = 0
#     for i in nums:
#         if i == n:
#             count += 1
#     return count

# def MajorityElement_count(nums):
#     for n in nums:
#         count = count_elements(n, nums)
#         if count > len(nums) // 2:
#             return n

if __name__ == '__main__':
    # nums = [3,2,3]
    nums = [2,2,1,1,1,2,2]
    print(MajorityElement(nums))
    print(MajorityElement_FollowUp(nums))
    # print(MajorityElement_count(nums))