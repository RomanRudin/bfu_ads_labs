#include <iostream>
#include <string>

//! THIS IS JUST A STRUCTURE, I DIDN'T WANT TO IMPLEMENT READING AND WRITING TO FILE, YOU SHOULD DO IT BY YOURSELF

namespace HashTable_lp
{
    template <class T>
    struct Node
    {
        T value;
        Node(const T& value_) : value(value_) {}
    };



    template <class T>
    struct HashFunction
    {
        std::hash<T> hasher;
        unsigned int operator()(const T& value, int capacity) const
        {
            return (unsigned int)this->hasher(value) % capacity;
        }
    };



    template <class T, class THash = HashFunction<T>>
    class HashTable
    {
    public:
        const int size = 5; // начальный размер нашей таблицы
        const double rehash_size = 0.75; // коэффициент, при котором произойдет рехэш

        Node<T>** arr; // сам массив
        int items_count; // сколько элементов у нас сейчас в массиве 
        int capacity; // размер самого массива


    private:
        void rehash()
        {
            this->items_count = 0;
            this->capacity *= 2;
            Node<T>** arr2 = new Node<T> * [this->capacity];
            for (int i = 0; i < this->capacity; i++)
                arr2[i] = nullptr;
            std::swap(arr, arr2);
            for (int i = 0; i < this->capacity / 2; i++)
            {
                if (arr2[i])
                    insert(arr2[i]->value);
                    delete arr2[i];
            }
            delete[] arr2;
        }


    public:
        HashTable()
        {
            this->capacity = this->size;
            this->items_count = 0;
            this->arr = new Node<T>* [this->capacity];
            for (int i = 0; i < this->capacity; i++)
                this->arr[i] = nullptr;
        }

        ~HashTable()
        {
            for (int i = 0; i < this->capacity; i++)
                if (this->arr[i])
                    delete this->arr[i];
            delete[] this->arr;
        }


        int search(const T& value, const THash& hash = THash())
        {
            unsigned int index = hash(value, this->capacity);
            if (this->arr[index]->value == value) return index;
            return -1;
        }


        bool remove(const T& value, const THash& hash = THash())
        {
            unsigned int index = this->search(value);
            if (index == -1) return false;
            this->arr[index] = nullptr;
            this->items_count--;
            return true;
        }


        bool insert(const T& value, const THash& hash = THash())
        {
            unsigned int index = hash(value, this->capacity);
            this->arr[index] = new Node<T>(value);
            this->items_count++;
            if (this->items_count > int(this->rehash_size * this->capacity))
                rehash();
            return true;
        }

        int len() 
        {
            return this->items_count;
        }

        friend std::ostream& operator<<(std::ostream& out, const HashTable& table)
        {
            for (int i = 0; i < table.capacity; i++)
                if (table.arr[i] != nullptr)
                    out << "(" << i << ", " << table.arr[i]->value << ") ";
            return out;
        }
    };
};

//! THIS IS JUST A STRUCTURE, I DIDN'T WANT TO IMPLEMENT READING AND WRITING TO FILE, YOU SHOULD DO IT BY YOURSELF


int main() {
    HashTable_lp::HashTable<std::string> hash_table;

    hash_table.insert("abc");
    std::cout << hash_table << std::endl;
    hash_table.insert("abc");
    std::cout << hash_table << std::endl;
    hash_table.insert("abc");
    std::cout << hash_table << std::endl;
    hash_table.insert("a");
    std::cout << hash_table << std::endl;
    hash_table.insert("b");
    std::cout << hash_table << std::endl;
    hash_table.insert("c");
    std::cout << hash_table << std::endl;
    hash_table.insert("d");
    std::cout << hash_table << std::endl;
    hash_table.insert("efghikj");
    std::cout << hash_table << std::endl;
    hash_table.insert("efghikj");
    std::cout << hash_table << std::endl;

    return 0;
}

//! THIS IS JUST A STRUCTURE, I DIDN'T WANT TO IMPLEMENT READING AND WRITING TO FILE, YOU SHOULD DO IT BY YOURSELF