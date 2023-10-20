from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validBST(node, min_val, max_val):
            if not node:
                return True
            
            if not (min_val < node.val < max_val):
                return False
            
            return validBST(node.left, min_val, node.val) and validBST(node.right, node.val, max_val)
        
        return validBST(root, float('-inf'), float('inf'))
            
        

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(10)
    root.right.right.right = TreeNode(11)

    sol = Solution()
    print(sol.isValidBST(root))