"""
https://leetcode.com/problems/longest-repeating-character-replacement/
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        char_count = {}
        max_count = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])

            if (right - left + 1 - max_count) > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


# class Solution:
    
    
#     def characterReplacement(self, s: str, k: int) -> int:
#         l, r = 0, 0
#         max_length = 0
#         char_count = {}
#         max_c = s[0]
#         non_major = 0
       
#         while r < len(s):
#             c = s[r]
#             char_count[c] = char_count.get(c, 0) + 1
#             r += 1
#             if char_count[c] > char_count[max_c]:
#                 max_c = c
#             non_major = r - l - char_count[max_c]
#             if non_major <= k: max_length = max(max_length, r - l)
#             if non_major > k:
#                 l += 1
#                 r = l
#                 max_c = s[l]
#                 char_count = {}
#                 non_major = 0


#         return max_length

if __name__ == '__main__':
    # s = "ABAB"; k = 2 # output 4
    # s = "AABABBA"; k = 1 # output 4
    s = "ABBB"; k = 3 # output 4
    # s = "AABBBC"; k = 2
    sol = Solution()
    print(sol.characterReplacement(s, k))
    # print(sol.isValid(s, k))

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         l, r = 0, 0
#         max_length = 0
#         foul = 0
#         while r < len(s):
#             if s[r] == s[l]:
#                 r += 1
#                 max_length = max(max_length, r - l)
#             else:
#                 foul += 1
#                 if foul == 1:
#                     foul_index = r
#                 if foul <= k:
#                     r += 1
#                     max_length = max(max_length, r - l)
#                 else:
#                     foul = 0
#                     l = foul_index
#                     r = foul_index
#         return max_length
    


