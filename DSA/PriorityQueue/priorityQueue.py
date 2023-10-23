from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Comparator, Optional

K = TypeVar('K')
V = TypeVar('V')

class Entry(Generic[K, V]):
    @abstractmethod
    def get_key(self) -> K:
        pass

    @abstractmethod
    def get_value(self) -> V:
        pass

class PQEntry(Entry[K, V]):
    def __init__(self, key: K, value: V):
        self.k = key
        self.v = value

    def get_key(self) -> K:
        return self.k
    
    def get_value(self) -> V:
        return self.v



class AbstractPriorityQueue(ABC, Generic[K, V]):
    def __init__(self, comp: Optional[Comparator[K]] = None):
        self.comp = comp

    @abstractmethod
    def compare(self, a: Entry[K, V], b: Entry[K, V]) -> int:
        return self.comp.compare(a.get_key(), b.get_key())
    
    @abstractmethod
    def check_key(self, key: K) -> bool:
        try:
            return self.comp.compare(key, key) == 0
        except Exception as e:
            raise ValueError("Incompatible key")
        
    @abstractmethod
    def is_empty(self) -> bool:
        return self.size() == 0
    

    