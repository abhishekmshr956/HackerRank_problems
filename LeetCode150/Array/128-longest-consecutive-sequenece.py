"""
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
def longestConsecutive(nums):
    nums_set = set(nums)
    # for n in nums:
    #     nums_set.add(n)

    max_consecutive = 0
    
    for n in nums_set:
        if n - 1 not in nums_set:
            # current_num = n
            current_length = 1

            while n + current_length in nums_set:
                # current_num += 1
                current_length += 1

            max_consecutive = max(max_consecutive, current_length)

    return max_consecutive

if __name__ == '__main__':
    # nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(nums))
