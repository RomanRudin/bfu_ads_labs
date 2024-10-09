from Labs.Lab13.HashTable_linear_probing import HashTable as HashTable_linear_probing
# from Labs.Lab13.HashTable_quadratic_probing import HashTable as HashTable_quadratic_probing
# from Labs.Lab13.HashTable_double_hashing import HashTable as HashTable_double_hashing
# from Labs.Lab13.lab_14 import HashTable as HashTable_chaining_method


table = HashTable_linear_probing()
table.insert(1)
table.insert(2)
table.insert(3)
table.insert(4)
table.insert(5)
table.insert(6)
table.insert(7)
table.insert(8)
table.insert(9)
table.insert(10)
table.insert("abs")
table.insert(11)
table.insert(12)
table.insert(13)
table.insert(14)
table.insert(15)
for i in range(1, 16):
    print(f"{i}: {table.search(i)}")