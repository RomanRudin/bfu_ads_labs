import Labs.Lab13.HashTable_linear_probing
import Labs.Lab13.HashTable_quadratic_probing
import Labs.Lab13.HashTable_double_hashing
import Labs.Lab14.HashTable_separate_chaining
from os import getcwd

def main_test(hash_table, path: str, name: str) -> bool:
    words = set()
    with open(path + r"\input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                hash_table.insert(word)
                words.add(word)
    with open(path + fr"\output_{name}.txt", 'w', encoding="utf-8") as output:
        output.write(str(hash_table))
    print(len(hash_table), len(words), words == hash_table)
    # for elem in hash_table.keys:
        # if hash_table.keys.count(elem) > 1: print(elem)
    if words == hash_table and len(hash_table) == len(words): return True
    return False

hash_table_linear = Labs.Lab13.HashTable_linear_probing.HashTable()
hash_table_quadratic = Labs.Lab13.HashTable_quadratic_probing.HashTable()
# hash_table_double = Labs.Lab13.HashTable_double_hashing.HashTable()
hash_table_chaining = Labs.Lab14.HashTable_separate_chaining.HashTable()

print(f'Linear probing realisation (open addressation): {main_test(hash_table_linear, getcwd() + r"\Semester_1\Labs\Lab13", "Linear")}')
print(f'Quadratic probing realisation (open addressation): {main_test(hash_table_quadratic, getcwd() + r"\Semester_1\Labs\Lab13", "Quadratic")}')
# print(f'Double hashing realisation (open addressation): {main_test(hash_table_double, getcwd() + r"\Semester_1\Labs\Lab13", "Double")}')
print(f'Chaining method realisation: {main_test(hash_table_chaining, getcwd() + r"\Semester_1\Labs\Lab14", "Chaining")}')