from treeADT import Tree, AbstractTree

class LinkedGeneralTree(AbstractTree):
    class Node:
        def __init__(self, element, parent=None):
            self.element = element
            self.parent = parent
            self.children = []

        def getElement(self):
            return self.element
        
        def getParent(self):
            return self.parent
        
        def getChildren(self):
            return self.children
        
    def children(self, p):
        node = self.validate(p)
        return p.children
    
    def num_children(self, p):
        node = self.validate(p)
        return len(p.children)
    
    def parent(self, p):
        node = self.validate(p)
        return p.parent

        
    def create_node(self, element, parent=None):
        return self.Node(element, parent)
    
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
    
    def addRoot(self, element):
        if not self.isEmpty():
            raise ValueError("Tree is not empty")
        self.root = self.create_node(element, None)
        self.size = 1
        return self.root
    
    def addChild(self, p, e):
        parent = self.validate(p)
        child = self.create_node(e, parent)
        parent.children.append(child)
        self.size += 1
        return child
    
    def set(self, p, e):
        node = self.validate(p)
        temp = node.getElement()
        node.element = e
        return temp
