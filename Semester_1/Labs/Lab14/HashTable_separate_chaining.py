class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable:
    def __init__(self, size=100, load_factor=0.75):
        self.size = size
        self.items_count = 0
        self.load_factor = load_factor
        self.table = [None] * self.size

    # insertion:
    def __insert_last(self, index, key):
        new_node = Node(key)
        if not self.table[index]:
            self.table[index] = new_node
            return
        current = self.table[index]
        while current.next:
            current = current.next
        current.next = new_node

    def __rehash(self):
        new_table = [None] * (self.size * 2)
        for bucket in self.table:
            if not bucket: continue
            index = self.hash_function(bucket.key, len(new_table))
            new_table[index] = bucket
        return new_table
    
    def insert(self, key):
        self.items_count += 1
        load_factor = self.items_count / self.size
        if load_factor > self.load_factor:
            self.table = self.__rehash()
            self.size *= 2
            self.load_factor = self.items_count /self.size
        index = self.hash_function(key)
        self.__insert_last(index, key)

    # search:
    def find(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current or current.key != key:
            current = current.next
        if not current:
            raise Exception(f"key = {key} doesn't exist in the list")
        return current.key

    # remove:
    def __remove(self, index, key):
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

    def remove(self, key):
        index = self.hash_function(key)
        self.__remove(index, key)

    def hash_function(self, key, size=None):
        if not size: size = self.size
        return key % size