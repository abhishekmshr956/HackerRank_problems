"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        char_index = {}
        max_length = 0
        l = 0

        for r in range(len(s)):
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1
            
            char_index[s[r]] = r
            max_length = max(max_length, r - l + 1)

        return max_length
    
#using set
class Solution1:
    def lengthOfLongestSubstring(self, s:str) -> int:
        charSet = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max_length = max(max_length, len(charSet))

        return max_length




class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        l, r = 0, 0
        length, max_length = 0, 0
        while r < len(s):
            c = s[r]
            if c not in substring or substring[c] < l:
                substring[c] = r
                r += 1
                length = r - l
                max_length = max(length, max_length)
            else:
                l = substring[c] + 1
                substring[c] = r
                r += 1
        return max_length

class Solution2:
    def findIndex(self, s: str, c: str) -> int:
        for i in range(len(s)):
            if c == s[i]:
                return i
            
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length, length = 0, 0
        substring = ""

        while right < len(s):
            c = s[right]
            if c not in substring:
                substring += c
                right += 1
                length += 1
                max_length = max(max_length, length)
            else:
                c_index = self.findIndex(substring, c)
                substring = substring[c_index+1:]
                length = len(substring)
        return max_length



if __name__=='__main__':
    sol = Solution()
    # s = "abcabcbb" # 3
    s = "pwwkew" # 3
    # s = "apbcdpfg" # 6
    # s = "tmmzuxt" #5
    # s = " "
    print(sol.lengthOfLongestSubstring(s))



