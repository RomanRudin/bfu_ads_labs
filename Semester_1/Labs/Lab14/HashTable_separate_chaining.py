from typing import Any, Literal, LiteralString

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

    def hash_function(self, key, size=None) -> int:
        if not size: size = self.capacity
        return int(hash(key)) % size

    def __insert_last(self, index, key, table=None) -> bool:
        if not table: table = self.table
        new_node = Node(key)
        if not table[index]:
            table[index] = new_node
            return
        current = table[index]
        while current.next:
            if current.key == key: return False
            current = current.next
        current.next = new_node
        return True

    def __rehash(self) -> list[None | Any]:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for first_key in self.table:
            if not first_key: continue
            key_list = []
            current = first_key
            while current:
                key_list.append(current.key)
                if not current.next: break
                current = current.next
            for node in key_list:
                index = self.hash_function(node, self.capacity)
                self.__insert_last(index, node, new_table)
        return new_table
    
    def insert(self, key) -> None:
        index = self.hash_function(key)
        was_inserted = self.__insert_last(index, key)
        if not was_inserted: return 
        self.items_count += 1
        load_factor = self.items_count / self.capacity
        if load_factor > self.load_factor:
            self.table = self.__rehash()
            self.load_factor = self.items_count / self.capacity

    def search(self, key) -> Any | Literal[-1]:
        index = self.hash_function(key)
        current = self.table[index]
        if not current:
            return -1
        while True:
            if not current.next: return -1
            if current.key == key: return current.key
            current = current.next
        

    def delete(self, key) -> None:
        index = self.hash_function(key)
        if not self.table[index]:
            raise Exception(f"List is Empty!! key = {key} doesn't exist in the list")
        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            return
        current, previous = self.table[index], self.table[index]
        while current and current.next != key:
            previous, current = current, current.next
        if not current:
            raise Exception(f"key = {key} doesn't exist in the list")
        previous.next = current.next
        self.items_count -= 1


    # Couple of methods, that are not nescessary for this lab purposes, 
    # # I made them just for fun

    @property
    def keys(self) -> list[Any]:
        keys = []
        for first_node in self.table: 
            if first_node != None:
                node = first_node
                while node.next:
                    keys.append(node.key)
                    node = node.next
        return keys
    
    @property
    def pairs(self) -> list[tuple[int, list[Any]]]:
        pairs = []
        for index, first_node in enumerate(self.table): 
            if first_node != None:
                node = first_node
                keys = [node.key]
                while node.next:
                    node = node.next
                    keys.append(node.key)
                keys.pop(-1)
                pairs.append((index, keys))
        return pairs

    def __len__(self) -> int:
        return len(self.keys)

    def __eq__(self, other: "HashTable") -> bool:
        if self is other:
            return True
        if type(self) is not type(other):
            #! Needs to be rewritten, testing only
            if type(other) == type(set()):
                return set(self.keys) == other
            #! Needs to be rewritten, testing only
            return False
        return self.table == other.table 
    
    def __str__(self) -> LiteralString:
        return "{" + ", ".join(map(str, self.pairs)) + "}"