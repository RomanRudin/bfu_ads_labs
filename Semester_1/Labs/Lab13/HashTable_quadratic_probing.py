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
    
    def __rehash(self) -> list[None]:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for key in self.table:
            if not key: continue
            self.__insert(key, new_table)
        return new_table

    def __insert(self, key, table) -> None:
        index, counter = self.hash_function(key, size=len(table)), 1
        while table[index] != None:
            if table[index] == key: return
            index = (index + counter ** 2) % len(table)
            counter += 1
        table[index] = key
    
    def insert(self, key) -> None:
        self.items_count += 1
        load_factor = self.items_count / len(self.table)
        if (load_factor > self.load_factor) and (self.search(key) == -1):
            self.table = self.__rehash()
            self.load_factor = load_factor
        self.__insert(key, self.table)


    def search(self, key) -> Any | Literal[-1]:
        index, counter = self.hash_function(key), 1
        while (self.table[index] != key and self.table[index] != None):
            index = (index + counter ** 2) % len(self.table)
            counter += 1
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