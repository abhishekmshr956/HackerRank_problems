""" Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
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

def isValid_1(s):
    n = len(s) 
    open = []
    m = {'(' : ')', '{' : '}', '[' : ']'}
    if n % 2 == 0:
        for c in s:
            if c in '({[':
                open.append(c)
            elif open == []:
                return False
            elif m[open[-1]] != c:
                return False
            else:
                del open[-1]
        if len(open) != 0:
            return False
        else:
            return True
    else:
        return False
    
def isValid(s):
    m = {')':'(', '}':'{', ']':'['}
    if len(s) < 2 or s[0] in m or len(s) % 2 != 0:
            return False
    stack = []
    for c in s:
        if c in m:
            top_element = stack.pop() if stack else '#'

            if m[c] != top_element:
                return False
            
        else:
            stack.append(c)

    return not stack
    
# s = "){" # False
# s = "()[]{}" # True
# s = "(]" # False
s = "{[]}" # should return True
print(isValid(s))