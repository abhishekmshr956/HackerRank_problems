"""
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""
def move_zeroes(A):
    flag = False
    for i in range(len(A)):
        if flag == False and A[i] == 0:
            flag = True
            low = i
        if flag and A[i] != 0:
            A[i], A[low] = A[low], A[i]
            low += 1
    return A

### simplified solutions
def move_zeroes_1(A):
    l = 0
    for r in range(len(A)):
        if A[r]:
            if l != r: # to avoid unnecessary swapping
                A[l], A[r] = A[r], A[l]
            l += 1
    return A

if __name__ == '__main__':
    # nums = [0,0,0,2,0,1,3,5]
    nums = [2,4,0,1,3,5]
    # nums = [0]
    # nums = [0, 1, 0, 3, 12]
    print(move_zeroes(nums))
    print(move_zeroes_1(nums))

    
