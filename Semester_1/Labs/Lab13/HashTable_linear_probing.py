from typing import Any, Literal, Generator, LiteralString

class HashTable:
    def __init__(self, capacity=100, load_factor=0.75):
        self.items_count = 0
        self.load_factor = load_factor
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_function(self, key, size=None) -> int:
        if not size: size = self.capacity
        return int(hash(key)) % size
    
    def __rehash(self) -> tuple[list[None], list[int]]:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for key in self.table:
            if not key: continue
            self.__insert(key, new_table)
        return new_table

    def __insert(self, key, table) -> None:
        index = self.hash_function(key, size=len(table))
        while table[index] != None:
            if table[index] == key: return
            index = (index + 1) % len(table)
        table[index] = key
    
    def insert(self, key) -> None:
        self.items_count += 1
        load_factor = self.items_count / len(self.table)
        if (load_factor > self.load_factor) and (self.search(key) == -1):
            self.table = self.__rehash()
            self.load_factor = load_factor
        self.__insert(key, self.table)


    def search(self, key) -> Any | Literal[-1]:
        index = self.hash_function(key)
        while (self.table[index] != key and self.table[index] != None):
            index = (index + 1) % len(self.table)
        if self.table[index] == key:
            return index
        return -1

    def delete(self, key) -> None:
        index = self.search(key)
        if index > -1:
            self.table[index] = None


    # Couple of methods, that are not nescessary for this lab purposes, 
    # # I made them just for fun
    def __len__(self) -> int:
        return len([key for key in self.table if key != None])

    def __iter__(self)-> Generator[Any, Any, None]:
        yield from [key for key in self.table if key != None] 

    def __getitem__(self, key: Any) -> Any:
        search_result = self.search(key)
        if search_result == -1:
            raise KeyError(key)
        return self.table[search_result]

    def __eq__(self, other: "HashTable") -> bool:
        if self is other:
            return True
        if type(self) is not type(other):
            #! Needs to be rewritten, testing only
            if type(other) == type(set()):
                return set([key for key in self.table if key != None]) == other
            #! Needs to be rewritten, testing only
            return False
        return self.table == other.table 
    
    def __str__(self) -> LiteralString:
        pairs = []
        for index, key in enumerate(self.table):
            if key == None: continue
            pairs.append(f"{index!r}: {key!r}")
        return "{" + ", ".join(pairs) + "}"

    def get(self, index: Any) -> Any | None:
        return self.table[index]

    # @property
    # def keys(self) -> list:
    #     return [key for key in self.table if key != None]

    # @property
    # def indexes(self) -> list:
    #     return [i for i in self.table if self.table[i] != None]

    # @property
    # def capacity(self) -> int:
    #     return self.capacity

    # @property
    # def load_factor(self) -> float:
    #     return len(self) / self.capacity

    # def __delitem__(self, key: Any) -> None:
        # match self._find(key):
            # case bucket, index, _:
                # del bucket[index]
                # self.keys.remove(key)
            # case _:
                # raise KeyError(key)

    # def __setitem__(self, key: Any, value: Any) -> None:
        # pass

    # def copy(self) -> "HashTable":
    #     pass

    # def __contains__(self, key: Any) -> bool:
    #     try:
    #         self[key]
    #     except KeyError:
    #         return False
    #     else:
    #         return True