#include <iostream>
#include <fstream>
#include <string>
#include <vector>

const int INITIAL_TABLE_SIZE = 100; //Ксловная начальная вместительность таблицы

class HashTable {
private:
    std::vector<std::string> table; // Используем строки напрямую
    size_t size; 

    int hash_function(const std::string& key) { //хэш функция по алгоритму DJB2
        unsigned long hash = 5381;       //магическое число 5381       
        for (char c : key) {
            hash = ((hash << 5) + hash) + c;   //по-факту эквивалентно hash * 33 (тоже магическое число)
        }
        return hash % table.size();
    }

    void rehash() {
        size_t newSize = table.size() * 2 + 1; // Увеличиваем размер 
        std::vector<std::string> newTable(newSize, ""); // Все ячейки пустые
        for (const auto& item : table) {
            if (!item.empty()) { // Переносим только непустые элементы
                int index = hash_function(item);
                while (!newTable[index].empty()) {
                    index = (index + 1) % newSize;
                }
                newTable[index] = item;
            }
        }
        table = std::move(newTable); //перемещаем ресурсы 
    }

public:
    HashTable() : table(INITIAL_TABLE_SIZE, ""), size(0) {}

    void insert(const std::string& key) {
        if (size > table.size() * 0.75) { // Перехеширование при загрузке > 75%
            rehash();
        }

        int index = hash_function(key);
        while (!table[index].empty()) {
            if (table[index] == key) {
                return; // Элемент уже существует, то скип
            }
            index = (index + 1) % table.size(); //переход в проценты позволяет нам рекурсировать
        }
        table[index] = key;
        size++;
    }

    void readFrom(const std::string& file) {
        std::ifstream inpt(file);
        std::string word;

        if (inpt.is_open()) {
            while (inpt >> word) {
                insert(word);
            }
            inpt.close();
        } else {
            std::cerr << "Ошибка чтения файла" << std::endl;
        }
    }

    void writeTo(const std::string& file) {
        std::ofstream outpt(file);
        if (!outpt) {
            std::cerr << "Ошибка при создании файла записи" << std::endl;
            return;
        }

        for (size_t i = 0; i < table.size(); ++i) {
            if (table[i].empty()) {
                outpt << i << ": \n";
            } else {
                outpt << i << ": " << table[i] << "\n";
            }
        }

        outpt.close();
        std::cout << "Хеш-таблица сохранена в " << file << std::endl;
    }
};

int main() {
    HashTable my_table;
    my_table.readFrom("C:\\Git\\ADS-Tasks\\Lab 13\\input.txt");
    my_table.writeTo("C:\\Git\\ADS-Tasks\\Lab 13\\output.txt");
    return 0;
}
