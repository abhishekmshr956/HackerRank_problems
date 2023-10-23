from abc import ABC, abstractmethod
from collections import deque

class Tree(ABC):
    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self, p):
        pass

    @abstractmethod
    def children(self, p):
        pass

    @abstractmethod
    def num_children(self, p):
        pass

    @abstractmethod
    def isInternal(self, p):
        pass

    @abstractmethod
    def isExternal(self, p):
        pass

    @abstractmethod
    def isRoot(self, p):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def positions(self):
        pass

class AbstractTree(Tree):
    def isInternal(self, p):
        return self.num_children(p) > 0
    
    def isExternal(self, p):
        return self.num_children(p) == 0
    
    def isRoot(self, p):
        return p == self.root
    
    def isEmpty(self):
        return self.size == 0
    
    def depth(self, p):
        if self.isRoot(p):
            return 0
        
        return 1 + self.depth(self.parent(p))
    
    def _heightBad(self):
        h = 0
        for p in self.positions():
            if self.isExternal(p):
                h = max(h, self.depth(p))
        return h
    
    def height(self, p):
        h = 0
        for c in self.children(p):
            h = max(h, 1 + self.height(c))
        return h 
    
    class ElementIterator:
        def __init__(self, tree):
            self.pos_iterator = iter(tree.positions())

        def __iter__(self):
            return self
        
        def __next__(self):
            pos = next(self.pos_iterator)
            return pos.get_element()
        
        def remove(self):
            self.pos_iterator.remove()

    def __iter__(self):
        return self.ElementIterator(self)
    
    def iterator(self):
        return self.ElementIterator(self)
    
    def positions(self):
        return self.preorder()
    
    def preorderSubtree(self, p, snapshot: list):
        snapshot.append(p)
        for c in self.children(p):
            self.preorderSubtree(c, snapshot)

    def preorder(self):
        snapshot = []
        if not self.isEmpty():
            self.preorderSubtree(self.root, snapshot)
        return snapshot
    
    def postorderSubtree(self, p, snapshot: list):
        for c in self.children(p):
            self.postorderSubtree(c, snapshot)
        snapshot.append(p)

    def postorder(self):
        snapshot = []
        if not self.isEmpty():
            self.postorderSubtree(self.root(), snapshot)
        return snapshot
    
    def breadthfirst(self):
        snapshot = []
        if not self.isEmpty():
            fringe = deque()
            fringe.append(self.root())
            while fringe:
                node = fringe.popleft()
                snapshot.append(node)
                for c in self.children():
                    fringe.append(c)
        return snapshot
            