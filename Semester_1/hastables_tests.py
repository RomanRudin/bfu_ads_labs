from Labs.Lab13.HashTable_linear_probing import HashTable as HashTable_linear_probing
from os import getcwd

def main_test(path: str) -> bool:
    hash_table = HashTable_linear_probing()
    words = set()
    with open(path + r"\input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                hash_table.insert(word)
                words.add(word)
    with open(path + r"\output.txt", 'w', encoding="utf-8") as output:
        output.write(str(hash_table))
    print(len(hash_table), len(words), words == hash_table)

main_test(getcwd() + r"\Semester_1\Labs\Lab13")