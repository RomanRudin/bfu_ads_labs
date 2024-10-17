#include <iostream>
#include <string>

//! THIS IS JUST A STRUCTURE, I DIDN'T WANT TO IMPLEMENT READING AND WRITING TO FILE, YOU SHOULD DO IT BY YOURSELF

namespace HashTable_sc
{
    template <class T>
    struct Node
    {
        T value;
        Node* next;
        Node(const T& value_) : value(value_), next(nullptr) {}
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
            //std::cout << "REHASH!" << std::endl;
            this->items_count = 0;
            this->capacity *= 2;
            Node<T>** arr2 = new Node<T> *[this->capacity];
            for (int i = 0; i < this->capacity; i++)
                arr2[i] = nullptr;
            std::swap(arr, arr2);
            for (int i = 0; i < this->capacity / 2; i++)
            {
                if (!arr2[i]) continue;
                Node<T>* current = arr2[i];
                while (current)
                {
                    this->insert(current->value);
                    if (current->next == nullptr) break;
                    current = current->next;
                }

            }
            //this->arr = arr2;
            delete[] arr2;
        }


    public:
        HashTable()
        {
            this->capacity = this->size;
            this->items_count = 0;
            this->arr = new Node<T>*[this->capacity];
            for (int i = 0; i < this->capacity; i++)
                this->arr[i] = nullptr;
        }


        ~HashTable()
        {
            for (int i = 0; i < this->capacity; i++)
                if (this->arr[i]) {
                    while (this->arr[i]->next != nullptr) {
                        Node<T>* current = this->arr[i]->next;
                        while (current->next != nullptr)
                            current = current->next;
                        delete current;
                    }
                    delete this->arr[i];
                }
            delete[] this->arr;
        }


        int search(const T& value, const THash& hash = THash())
        {
            unsigned int index = hash(value, this->capacity);
            while (arr[index] != nullptr)
            {
                if (this->arr[index]->value == value) return index;
                index = (index + 1) % this->capacity;
            }
            return -1;
        }


        bool remove(const T& value, const THash& hash = THash())
        {
            unsigned int index = this->search(value);
            if (index == -1) return false;
            Node<T>* current = this->arr[index];
            if (current->value == value) {
                this->arr[index] = current->next;
                delete current;
                return true;
            }
            Node<T>* previous = current;
            while (current != nullptr)
            {
                if (current->value == value) {
                    previous->next = current->next;
                    delete current;
                    return true;
                }
                previous = current;
                current = current->next;
            }
            return false;
        }


        bool insert(const T& value, const THash& hash = THash())
        {
            unsigned int index = hash(value, this->capacity);
            //std::cout << "trying t Insert value: " << value << "\t into " << int(index) << std::endl;
            if (this->arr[index] == nullptr) 
            {
                this->arr[index] = new Node<T>(value);
            }
            else
            {
                Node<T>* current = arr[index];
                while (current != nullptr)
                {
                    if (current->value == value) return false;
                    if (current->next == nullptr) break;
                    current = current->next;
                }
                Node<T>* new_node = new Node<T>(value);
                current->next = new_node;
            }
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
            out << "{";
            for (int i = 0; i < table.capacity; i++)
                if (table.arr[i] != nullptr)
                {
                    out << "(" << i << ", " << "[";
                    Node<T>* current = table.arr[i];
                    while (current != nullptr) {
                        out << current->value;
                        if (current->next != nullptr) out << ", ";
                        current = current->next;
                    }
                    out << "}, ";
                }
            out << "}";
            return out;
        }
    };
};

//! THIS IS JUST A STRUCTURE, I DIDN'T WANT TO IMPLEMENT READING AND WRITING TO FILE, YOU SHOULD DO IT BY YOURSELF

int main() {
    HashTable_sc::HashTable<std::string> hash_table;

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