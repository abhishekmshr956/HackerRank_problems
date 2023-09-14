"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""

def valid_parenthesis(s):
    stack = []
    m = {')':'(', '}':'{', ']':'['}
    for c in s:
        if c in m:
            top_element = stack.pop() if stack else '#'
            if m[c] != top_element:
                return False
        else:
            stack.append(c)
    return not stack

if __name__ == '__main__':
    # s = "()" # true
    # s = "()[]{}" # true
    # s = "(]" # false
    s = "()[" # false
    print(valid_parenthesis(s))