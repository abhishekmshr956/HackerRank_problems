from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversal:

    def preorder_recursive(self, root):
        if not root:
            return
        else:
            print(root.val, end = " ")
            self.preorder_recursive(root.left)
            self.preorder_recursive(root.right)

    def preorder_iterative(self, root):
        if not root:
            return []
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val, end = " ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return
    
    def inorder_recursive(self, root):
        if not root:
            return
        else:
            self.inorder_recursive(root.left)
            print(root.val, end = " ")
            self.inorder_recursive(root.right)

    def inorder_iterative(self, root):
        if not root:
            return []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                print(node.val, end = " ")
                root = node.right
        return
    
    def postorder_recursive(self, root):
        if not root:
            return
        else:
            self.postorder_recursive(root.left)
            self.postorder_recursive(root.right)
            print(root.val, end = " ")

    def postorder_iterative(sefl, root):
        if not root:
            return
        
        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            print(node.val, end = " ")

        return 
    
    def bfs_iterative(self, root):
        if not root:
            return
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            print(node.val, end = " ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return
        



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right.left = TreeNode(8)
    root.right.left.left = TreeNode(10)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(11)
    root.right.right.right = TreeNode(12)
    s = TreeTraversal()
    print(" ##### Preorder recursive ######")
    s.preorder_recursive(root)
    print("\n #### Preorder iterative #######")
    s.preorder_iterative(root)
    print(" #### \n Inorder recursive ######")
    s.inorder_recursive(root)
    print(' ##### \n Inorder iterative ######')
    s.inorder_iterative(root)
    print('\n #### Postorder recursive #####')
    s.postorder_recursive(root)
    print('\n #### Postorder iterative #####')
    s.postorder_iterative(root)
    print('\n #### BFS traversal ##### ')
    s.bfs_iterative(root)

