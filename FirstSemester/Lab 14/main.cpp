#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>

const int INITIAL_TABLE_SIZE = 100; 

class HashTable {
private:
    std::vector<std::list<std::string>> table; // Вектор из списков
    size_t size; 

    int hash_function(const std::string& key) {
        unsigned long hash = 5381;
        for (char c : key) {
            hash = ((hash << 5) + hash) + c;
        }
        return hash % table.size();
    }

    void rehash() {
        size_t newSize = table.size() * 2 + 1; 
        std::vector<std::list<std::string>> newTable(newSize);

        for (const auto& chain : table) {       //создаём новую увеличенную таблицу
            for (const auto& key : chain) {
                int newIndex = hash_function(key) % newSize;
                newTable[newIndex].push_back(key);
            }
        }
        table = std::move(newTable); 
    }

public:
    HashTable() : table(INITIAL_TABLE_SIZE), size(0) {}

    void insert(const std::string& key) {
        if (size > table.size()) { // Перехеширование при коэффициенте загрузки > 1
            rehash();
        }

        int index = hash_function(key);
        auto& chain = table[index];

        // Проверка, существует ли ключ
        for (const auto& item : chain) {
            if (item == key) {
                return; // Элемент уже существует
            }
        }

        chain.push_back(key); // Добавляем новый ключ в цепочку
        ++size;
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
            outpt << "Index " << i << ":";
            for (const auto& key : table[i]) {
                outpt << key;
            }
            outpt << "\n";
        }

        outpt.close();
        std::cout << "Хеш-таблица сохранена в " << file << std::endl;
    }
};

int main() {
    HashTable my_table;
    my_table.readFrom("C:\\Git\\ADS-Tasks\\Lab 13\\input.txt");
    my_table.writeTo("C:\\Git\\ADS-Tasks\\Lab 14\\output.txt");
    return 0;
}
