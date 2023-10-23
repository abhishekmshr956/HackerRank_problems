from priorityQueue import K, Entry, PQEntry, AbstractPriorityQueue
from typing import Generic, TypeVar, List, Comparator, Optional

K = TypeVar('K')
V = TypeVar('V')

class UnsortedPriorityQueue(AbstractPriorityQueue[K, V]):
    def __init__(self, comp: Optional[Comparator[K]] = None):
        super().__init__(comp)
        self.elements = []    
    
    def insert(self, key: K, value: V) -> Entry[K, V]:
        self.check_key(key)
        newest = PQEntry(key, value)
        self.positional_list.append(newest)
        return newest
    
    def min(self) -> Entry[K, V]:
        if not self.elements:
            return None
        return min(self.elements, key = lambda entry: entry.get_key(), default=None)
    
    def removeMin(self):
        if not self.elements:
            return None
        
        min_entry = min(self.elements, key = lambda entry: entry.get_key())
        self.elements.remove(min_entry)
        return min_entry

    def size(self) -> int:
        return len(self.elements)        