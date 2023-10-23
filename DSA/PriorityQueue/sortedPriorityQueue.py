from priorityQueue import K, Entry, PQEntry, AbstractPriorityQueue
from typing import Generic, TypeVar, List, Comparator, Optional

K = TypeVar('K')
V = TypeVar('V')

class SortedPriorityQueue(AbstractPriorityQueue[K, V]):
    def __init__(self, comp: Optional[Comparator[K]] = None):
        super().__init__(comp)
        self.elements = []

    def insert(self, key: K, value: V) -> Entry[K, V]:
        self.check_key(key)
        newest = PQEntry(key, value)

        if not self.elements:
            self.elements.append(newest)
        else:
            for i, entry in enumerate(self.elements):
                if self.compare(newest, entry) <= 0:
                    self.elements.insert(i, newest)
                    break
                else:
                    self.elements.append(newest)
        
        return newest
    
    def min(self) -> Entry[K, V]:
        if not self.elements:
            return None
        return self.elements[0]
    
    def remove_min(self) -> Entry[K, V]:
        if not self.elements:
            return None
        return self.elements.pop(0)
    
    def size(self) -> int:
        return len(self.elements)