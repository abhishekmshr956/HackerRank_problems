"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            h1 = height[left]
            h2 = height[right]
            min_height = min(h1, h2)
            width = right - left
            area = min_height * width
            max_area = max(max_area, area)

            if h1 < h2:
                left += 1
            else:
                right -= 1
        return max_area

class Solution1:
    def maxArea(self, height: list[int]) -> int:
        left_possible = {}
        left_possible[0] = height[0]
        max_current_height = height[0]
        max_area = 0
        for i in range(1, len(height)):
            h = height[i]
            for key, value in left_possible.items():
                area_i = (i - key) * (min(value, h))
                max_area = max(max_area, area_i)
            if h > max_current_height:
                left_possible[i] = h
                max_current_height = h
        return max_area
    
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    # height = [1,1]
    s = Solution()
    print(s.maxArea(height))