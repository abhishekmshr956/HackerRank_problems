from treeADT import Tree, AbstractTree

class BinaryTree(Tree):
    def left(self, p):
        return p.left
    
    def right(self, p):
        return p.right
    
    def sibling(self, p):
        pass

class AbstractBinaryTree(AbstractTree, BinaryTree):
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
        
    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
    
    def children(self, p):
        snapshot = []
        if self.left(p) is not None:
            snapshot.add(self.left(p))
        if self.right(p) is not None:
            snapshot.add(self.right(p))
        return snapshot
    
    def inorderSubtree(self, p, snapshot):
        if self.left(p) is not None:
            self.inorderSubtree(self.left(p), snapshot)
        snapshot.add(p)
        if self.right(p) is not None:
            self.inorderSubtree(self.right(p))

    def inorder(self):
        snapshot = []
        if not self.isEmpty():
            self.inorderSubtree(self.root(), snapshot)
        return snapshot

    def positions(self):
        return self.inorder() 
    
class LinkedBinaryTree(AbstractBinaryTree):
    class Node:
        def __init__(self, element, parent = None, left = None, right = None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

        def getElement(self):
            return self.element
        
        def getParent(self):
            return self.parent
        
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setElement(self, e):
            self.element = e

        def setParent(self, parentNode):
            self.parent = parentNode

        def setLeft(self, leftChild):
            self.left = leftChild

        def setRight(self, rightChild):
            self.right = rightChild
    
    def create_node(self, element, parent=None, left=None, right=None):
        return self.Node(element, parent, left, right)
    
    def __init__(self):
        self.root = None
        self.size = 0

    def validate(self, p):
        if not isinstance(p, self.Node):
            raise ValueError("Not a valid position type")
        node = p 
        if node.parent is node:
            raise ValueError("p is no longer in the tree")
        return node
    
    def size(self):
        return self.size
    
    def root(self):
        return self.root
    
    def parent(self, p):
        node = self.validate(p)
        return node.getParent()
    
    def left(self, p):
        node = self.validate(p)
        return node.getLeft()
    
    def right(self, p):
        node = self.validate(p)
        return node.getRight()
    
    def addRoot(self, element):
        if not self.isEmpty:
            raise ValueError("Tree is not empty")
        self.root = self.create_node(element, None, None, None)
        self.size = 1
        return self.root
    
    def addLeft(self, p, e):
        parent = self.validate(p)
        if parent.getLeft() is not None:
            raise ValueError("Position p already has a left child")
        child = self.create_node(e, parent, None, None)
        parent.setLeft(child)
        self.size += 1
        return child
    
    def addRight(self, p, e):
        parent = self.validate(p)
        if parent.getRight() is not None:
            raise ValueError("Position p already has a right child")
        child = self.create_node(e, parent, None, None)
        parent.setRight(child)
        self.size += 1
        return child
    
    def set(self, p, e):
        node = self.validate(p)
        temp = node.getElement()
        node.setElement(e)
        return temp

    def attach(self, p, t1, t2):
        node = self.validate(p)
        if self.isInternal(node):
            raise ValueError("Position p must be a leaf")
        self.size += t1.size() + t2.size()
        if not t1.isEmpty():
            t1.root.setParent(node)
            node.setLeft(t1.root)
            t1.root = None
            t1.size = 0
        if not t2.isEmpty():
            t2.root.setParent(node)
            node.setRight(t2.root)
            t2.root = None
            t2.size = 0

    def remove(self, p):
        node = self.validate(p)
        if self.num_children(node) == 2:
            raise ValueError("p has two children")
        child = node.getLeft() if node.getLeft() is not None else node.getRight()
        if child is not None:
            child.setParent(node.getParent())
        if node == self.root():
            self.root = child
        else:
            parent = node.getParent()
            if node == parent.getLeft():
                parent.setLeft(child)
            else:
                parent.setRight(child)

        self.size -= 1
        temp = node.getElement()
        node.setElement(None)
        node.setLeft(None)
        node.setRight(None)
        node.setParent(node)
        return temp
    
    




    


    
    
        
    