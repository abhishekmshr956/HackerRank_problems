class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

#Iterative DFS
class Solution1:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        good_nodes = 0

        while stack:
            node, path_max = stack.pop()

            if node.val >= path_max:
                good_nodes += 1
                path_max = node.val

            if node.left:
                stack.append((node.left, path_max))

            if node.right:
                stack.append((node.right, path_max))

        return good_nodes
    
#Recursive DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            if node.val >= max_val:
                count = 1
                max_val = node.val
            else:
                count = 0

            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count
        
        return dfs(root, root.val)

if __name__ == '__main__':
    # root = TreeNode(3)
    # root.left = TreeNode(1)
    # root.left.left = TreeNode(3)
    # root.right = TreeNode(4)
    # root.right.left = TreeNode(1)
    # root.right.right = TreeNode(5)

    root = TreeNode(3)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    
    sol = Solution()
    print(sol.goodNodes(root))