"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers) - 1
        
        while low < high:
            curr_sum = numbers[low] + numbers[high]
            if target == curr_sum:
                return [low + 1, high + 1]
            elif target < curr_sum:
                high -= 1
            elif target > curr_sum:
                low += 1

# O(nlogn)
class Solution1:
    def binary_search(self, A: list[int], low: int, high: int, key: int) -> int:
        """ returns the index of the searched element key in A """

        while low <= high:
            mid = (low + high) // 2
            if key == A[mid]:
                return mid
            elif key < A[mid]:
                high = mid - 1
            elif key > A[mid]:
                low = mid + 1
        return None
    
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i1 in range(len(numbers)):
            num = numbers[i1]
            rem = target - num
            i2 = self.binary_search(numbers, i1+1, len(numbers) - 1, rem)
            if i2:
                return [i1 + 1, i2 + 1]


    
if __name__ == '__main__':
    numbers = [2,7,11,15]
    s = Solution()
    # print(s.binary_search(numbers, 0, len(numbers) - 1, 11))
    print(s.twoSum(numbers, 9))