# Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины
# (организовать чтение).
# Выбрав некоторую хеш-функцию, создать хеш-таблицу с:
# Лабораторная №13 “с наложением”
# Таблицу записать в результирующий файл.

import hashlib


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return int(hashlib.sha256(key.encode()).hexdigest(), 16) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def get_table(self):
        return [entry for entry in self.table if entry is not None]


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def write_to_file(file_path, hash_table):
    with open(file_path, 'w', encoding='utf-8') as file:
        for key, value in hash_table.get_table():
            file.write(f"{key}: {value}\n")


if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    hash_size = 100

    text = read_file(input_file)
    hash_table = HashTable(hash_size)

    # Инициализируем хеш-таблицу с данными из текста
    for line in text.splitlines():
        key = line
        value = len(line)
        hash_table.insert(key, value)

    write_to_file(output_file, hash_table)

    print(f"Хеш-таблица записана в файл {output_file}.")
