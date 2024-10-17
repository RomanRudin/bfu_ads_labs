from typing import Any, Literal, LiteralString

#! DOES NOT WORK CORRECTLY RN
#! DOES NOT WORK CORRECTLY RN
#! DOES NOT WORK CORRECTLY RN

class HashTable:
    def __init__(self, capacity=100, load_factor=0.75):
        self.items_count = 0
        self.load_factor = load_factor
        self.capacity = capacity
        self.table = [None] * capacity
        self.divider_of_capacity = self.get_dividers()

    def hash_function(self, key, size=None) -> int:
        if not size: size = self.capacity
        return int(hash(key)) % size
    
    def second_hash_function(self, key, size=None) -> Any:
        if not size: size = len(self.table)
        hash_two = int(hash(key)) % size
        while any([not (hash_two % divider) for divider in self.divider_of_capacity]):
            hash_two += 1
        return hash_two
    
    def get_dividers(self) -> list[int]:
        answer = set()
        cap = self.capacity
        while cap > 1:
            for i in range(2, cap + 1):
                if cap % i == 0:
                    answer.add(i)
                    cap //= i
                    break
        return answer

    def __rehash(self) -> list[None]:
        # print("REHASH!")
        self.capacity *= 2
        self.divider_of_capacity = self.get_dividers()
        new_table = [None] * self.capacity
        for key in self.table:
            if not key: continue
            # print(self.__insert(key, new_table))
        # print("rahsh ended")
        return new_table

    def __insert(self, key, table) -> bool:
        index, counter = self.hash_function(key), 0
        hash_two = self.second_hash_function(key)
        # print("trying to insert ", key)
        while table[index] != None:
            # print('into', index, 'hash2', hash_two, 'capacity', len(table), 'prime', self.divider_of_capacity)
            if table[index] == key: return False
            index = (index + hash_two) % len(table)
            counter += 1
        table[index] = key
        return True
    
    def insert(self, key) -> None:
        was_inserted = self.__insert(key, self.table)
        # print(was_inserted)
        if not was_inserted: return
        self.items_count += 1
        load_factor = self.items_count / len(self.table)
        if (load_factor > self.load_factor):
            self.table = self.__rehash()
            self.load_factor = load_factor

    def search(self, key) -> Any | Literal[-1]:
        index, counter = self.hash_function(key), 0
        hash_two = self.second_hash_function(key)
        while (self.table[index] != None):
            if (self.table[index] != key): return index
            index = (index + hash_two) % len(self.table)
            counter += 1
        return -1

    def delete(self, key) -> None:
        index = self.search(key)
        if index > -1:
            self.table[index] = None
            self.items_count -= 1

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
    
#! DOES NOT WORK CORRECTLY RN
#! DOES NOT WORK CORRECTLY RN
#! DOES NOT WORK CORRECTLY RN