""" Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/)
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        s = ''
        n_str = len(strs)
        for i in range(len(strs[0])):
            flag = True
            s = strs[0][:i+1]
            for j in range(1, n_str):
                if s == strs[j][:i+1]:
                    flag = True
                else:
                    flag = False
                    return prefix
            prefix = s
        return prefix
    
    def LCP(strs):
        prefix = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += s[i]
        return prefix
    
solution = Solution()
# strs = ["c","acc","ccc"]
# strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
print(solution.LCP(strs))
