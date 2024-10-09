from typing import Any, Literal, Generator, LiteralString

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable:
    def __init__(self, capacity=100, load_factor=0.75):
        self.items_count = 0
        self.load_factor = load_factor
        self.capacity = capacity
        self.table = [None] * capacity
        self.state = [0] * capacity

    def hash_function(self, key, size=None) -> Any:
        if not size: size = len(self.table)
        return key % size
    
    def __rehash(self) -> tuple[list[None], list[int]]:
        self.capacity *= 2
        new_table = [None] * self.capacity
        new_state = [0] * self.capacity
        for bucket in self.table:
            if not bucket: continue
            self.__insert(bucket, new_table, new_state)
        return new_table, new_state

    def __insert(self, key, table=None, state=None) -> None:
        if not table: table = self.table
        if not state: state = self.state
        index = self.hash_function(key)
        while self.state[index] == 1:
            index = (index + 1) % len(self.table)
        table[index], state[index] = key, 1
    
    def insert(self, key) -> None:
        self.items_count += 1
        load_factor = self.items_count / len(self.table)
        if load_factor > self.load_factor:
            self.table, self.state = self.__rehash()
            self.load_factor = load_factor
        self.__insert(key)


    def search(self, key) -> Any | Literal[-1]:
        index = self.hash_function(key)
        while (self.table[index] != key or\
            self.state[index] == -1) and\
                self.state[index] == 1:
            index = (index + 1) % len(self.table)
        if self.table[index] == key:
            return index
        return -1

    def delete(self, key) -> None:
        index = self.search(key)
        if index > -1:
            self.state[index] = -1


    # Couple of methods, that are not nescessary for this lab purposes, 
    # # I made them just for fun
    # def copy(self) -> "HashTable":
    #     pass

    # @classmethod
    # def from_dict(cls, dictionary: dict, capacity=None) -> "HashTable":
    #     hash_table = cls(capacity or len(dictionary))
    #     for key, value in dictionary.items():
    #         hash_table[key] = value
    #     return hash_table
    
    # def __len__(self) -> int:
    #     return len(self.pairs)

    # def __iter__(self)-> Generator[Any, Any, None]:
    #     yield from self.keys

    # def __delitem__(self, key: Any) -> None:
    #     match self._find(key):
    #         case bucket, index, _:
    #             del bucket[index]
    #             self.keys.remove(key)
    #         case _:
    #             raise KeyError(key)

    # def __setitem__(self, key: Any, value: Any) -> None:
    #     pass

    # def __getitem__(self, key: Any) -> Any:
    #     match self.search(key):
    #         case _, _, pair:
    #             return pair.value
    #         case _:
    #             raise KeyError(key)

    # def __contains__(self, key: Any) -> bool:
    #     try:
    #         self[key]
    #     except KeyError:
    #         return False
    #     else:
    #         return True

    # def __eq__(self, other: "HashTable") -> bool:
    #     if self is other:
    #         return True
    #     if type(self) is not type(other):
    #         return False
    #     return set(self.pairs) == set(other.pairs)

    # def __str__(self) -> LiteralString:
    #     pairs = []
    #     for key, value in self.pairs:
    #         pairs.append(f"{key!r}: {value!r}")
    #     return "{" + ", ".join(pairs) + "}"

    # def __repr__(self) -> str:
    #     cls = self.__class__.__name__
    #     return f"{cls}.from_dict({str(self)})"


    # def copy(self) -> "HashTable":
    #     return HashTable.from_dict(dict(self.pairs), self.capacity)

    # def get(self, key: Any, default=None) -> Any | None:
    #     try:
    #         return self[key]
    #     except KeyError:
    #         return default

    # @property
    # def pairs(self) -> list[tuple]:
    #     return [(key, self[key]) for key in self.keys]

    # @property
    # def values(self) -> list:
    #     return [self[key] for key in self.keys]

    # @property
    # def keys(self) -> list:
    #     return self.keys.copy()

    # @property
    # def capacity(self) -> int:
    #     return len(self.buckets)

    # @property
    # def load_factor(self) -> float:
    #     return len(self) / self.capacity