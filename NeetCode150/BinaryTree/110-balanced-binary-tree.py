"""
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#O(n)
class Solution:
    def calculate_height(self, node):
        if not node:
            return 0
        
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)

    def isBalanced(self, root):
        
        return self.calculate_height(root) != -1

# O(n^2)
class Solution1:
    def height(self, root):
        if not root:
            return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def isBalancedHelper(self, root):
        if not root:
            return True
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalancedHelper(root.left) and self.isBalancedHelper(root.right)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isBalancedHelper(root)

if __name__ == '__main__':
    # # # Tree 1 balanced
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    # Tree 2 unbalanced
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)



    s = Solution()
    print(s.isBalanced(root))