""" 
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""

def isPalindrome(s: str) -> bool:
    # # Convert the string to lowercase and filter out non-alphanumeric characters
    # s = ''.join(filter(str.isalnum, s.lower()))

    # # Check if the filtered string reads the same forwards and backwards
    # return s == s[::-1]


    # # s = ''.join(filter(str.isalnum, s.lower()))
    s = ''.join(filter(str.isalnum, s.lower()))
        
    # s_alphanumeric = ''
    # for c in s.lower():
    #     if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
    #         s_alphanumeric += c
    # # print(s_alphanumeric)

    n = len(s)

    i = 0
    j = n - 1
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

# def isPalindrome(s):
    
#     s_alphanumeric = ''
#     for c in s.lower():
#         if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
#             s_alphanumeric += c
#     # print(s_alphanumeric)

#     n = len(s_alphanumeric)

#     i = 0
#     j = n - 1
#     while i < n//2:
#         if s_alphanumeric[i] != s_alphanumeric[j]:
#             return False
#         else:
#             i += 1
#             j -= 1
#     return True

if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    s = " "
    # s = "amanaplanacanalpanama"
    print(isPalindrome(s))