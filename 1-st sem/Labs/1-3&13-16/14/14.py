# Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины
# (организовать чтение).
# Выбрав некоторую хеш-функцию, создать хеш-таблицу с:
# Лабораторная №14 “со списками”
# Таблицу записать в результирующий файл.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Инициализация таблицы со списками

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def __str__(self):
        return '\n'.join([f'{i}: {bucket}' for i, bucket in enumerate(self.table)])


def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def write_hash_table_to_file(hash_table, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(hash_table))


def main(input_file, output_file):
    lines = read_text_from_file(input_file)
    hash_table = HashTable(size=10)  # Размер таблицы можно менять по необходимости
    for line in lines:
        hash_table.insert(line)
    write_hash_table_to_file(hash_table, output_file)


if __name__ == '__main__':
    main('input.txt', 'output.txt')
