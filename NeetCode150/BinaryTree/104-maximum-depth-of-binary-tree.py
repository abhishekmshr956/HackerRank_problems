"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ maximum depth using recursion depth first search DFS """
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
    
    def maxDepth_iterDFS(self, root: Optional[TreeNode]) -> int:
        """ maximum depth using depth first search DFS. uses preorder traversal of nodes. """
        if root is None:
            return 0
        
        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth
            
    
    def maxDepth_iterBFS(self, root: Optional[TreeNode]) -> int:
        """ maximum depth using breadth first search """
        if not root:
            return
        
        queue = deque()
        max_depth = 0
        queue.append(root)

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            max_depth += 1

        return max_depth
        
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.maxDepth(root))
    print(s.maxDepth_iterDFS(root))
    print(s.maxDepth_iterBFS(root))