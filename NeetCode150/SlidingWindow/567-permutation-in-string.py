"""
https://leetcode.com/problems/permutation-in-string/
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
class Solution:
    def sCount(self, s:str) -> dict:
        s_count = {}
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1

        return s_count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_count = self.sCount(s1)
        s2_count = {}
        l = 0
        # print(s1_count)
        # print(s2)

        for r in range(len(s2)):
            if r - l + 1 > n:
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0: del s2_count[s2[l]]
                l += 1
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            if s1_count == s2_count:
                return True
            

        return False


# class Solution:
#     def isPermutation(self, s1: str, s2:str) -> bool:
#         s1_count = {}
#         s2_count = {}
#         for c in s1:
#             s1_count[c] = s1_count.get(c, 0) + 1
#         for c in s2:
#             s2_count[c] = s2_count.get(c, 0) + 1
#         return s1_count == s2_count

#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         n = len(s1)
#         for i in range(len(s2)):
#             print(s1)
#             print(s2[i : i + n])
#             if self.isPermutation(s1, s2[i : i + n]):
#                 return True

#         return False
    
if __name__ == '__main__':
    # s1 = "ab"
    # s2 = "ba"
    s1 = "ab"; s2 = "eidbaooo"
    sol = Solution()
    # print(sol.isPermutation(s1, s2))
    print(sol.checkInclusion(s1, s2))