from Labs.Lab13.HashTable_linear_probing import HashTable as HashTable_linear_probing
# from Labs.Lab13.HashTable_quadratic_probing import HashTable as HashTable_quadratic_probing
# from Labs.Lab13.HashTable_double_hashing import HashTable as HashTable_double_hashing
# from Labs.Lab13.lab_14 import HashTable as HashTable_chaining_method

from os import getcwd

def main_test(path: str) -> bool:
    hash_table = HashTable_linear_probing()
    with open(path + r"\input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                hash_table.insert(word)
                print(word)
    with open(path + r"\output.txt", 'w', encoding="utf-8") as output:
        output.write(str(hash_table))
    # HashTable_quadratic_probing(path)
    # HashTable_double_hashing(path)
    # HashTable_chaining_method(path)

main_test(getcwd() + r"\Semester_1\Labs\Lab13")