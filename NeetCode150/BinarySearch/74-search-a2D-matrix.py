"""
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        low = 0
        high = (m * n) - 1

        while low <= high:
            mid = (low + high) // 2
            midElement = matrix[mid // n][mid % n]
            if target == midElement:
                return True
            elif target < midElement:
                high = mid - 1
            elif target > midElement:
                low = mid + 1

        return False




# class Solution:
#     def findColumn(self, matrix: list[list[int]], target: int) -> int:
#         m = len(matrix) # number of rows
#         n = len(matrix[0]) # number of columns
#         low = 0
#         high = m - 1
#         while low < high:
#             mid = (low + high) // 2
#             if matrix[mid][0] <= target <= matrix[mid][n-1]:
#                 return mid
#             elif target < matrix[mid][0]:
#                 high = mid - 1
#             elif target > matrix[mid][n-1]:
#                 low = mid + 1
#         return low
    
#     def binarySearch(self, row: list[int], target: int) -> bool:
#         low = 0
#         high = len(row) - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if target == row[mid]:
#                 return True
#             elif target < row[mid]:
#                 high = mid - 1
#             elif target > row[mid]:
#                 low = mid + 1
#         return False

#     def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
#         m = len(matrix) # number of rows
#         n = len(matrix[0]) # number of columns
#         row = self.findColumn(matrix, target)
#         return self.binarySearch(matrix[row], target)


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 34
    sol = Solution()
    print(sol.searchMatrix(matrix, target))
    # print(sol.findColumn(matrix, target))
