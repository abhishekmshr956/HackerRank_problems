"""
https://leetcode.com/problems/daily-temperatures/
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer



# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         n = len(temperatures)
#         answer = [0] * n
#         for i in range(n-2, -1, -1):
#             if temperatures[i] < temperatures[i+1]:
#                 answer[i] = 1
#             else:
#                 j = answer[i+1]
#                 c = j
#                 while j != 0 and temperatures[i] >= temperatures[i + c + 1]:
#                     j = answer[i + c + 1]
#                     c += j
#                 if j == 0 and temperatures[i] >= temperatures[i+c+1]:
#                     answer[i] = 0
#                 else:
#                     answer[i] = c + 1
#             # print(answer)
#         return answer

if __name__ == '__main__':
    # temperatures = [73,74,75,71,69,72,76,73] # Output: [1,1,4,2,1,1,0,0]
    # temperatures = [30,40,50,60] # Output: [1,1,1,0]
    # temperatures = [30,60,90] # Output: [1,1,0]
    temperatures = [34,80,80,34,34,80,80,80,80,34] # Output: [1,0,0,2,1,0,0,0,0,0]
    sol = Solution()
    print(sol.dailyTemperatures(temperatures))

