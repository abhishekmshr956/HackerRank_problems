from abc import ABC, abstractmethod

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
        return p == self.root()
    
    def isEmpty(self):
        return self.size() == 0
    
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
            