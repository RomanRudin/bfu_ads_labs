#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <filesystem> 

using namespace std;
namespace fs = std::filesystem; 

//Алгоритм основан на принципе "разделяй и властвуй": 
//большие данные делятся на небольшие части (блоки), сортируются отдельно и затем объединяются в одну последовательность.

struct Element 
{
    int value;      // Значение элемента
    int block_id;   // Блок откуда элемент

    bool operator > (const Element& other) const 
    {
        return value > other.value;
    }
};

// Чтение блока из файла
bool read_block(ifstream& file, vector<int>& block, size_t block_size) 
{
    block.clear();
    int value;

    while (block.size() < block_size && file >> value) 
    {
        block.push_back(value);
    }
    return !block.empty();
}

// Сортировка данных в блоке и запись в файл
void sort_save_block(const vector<int>& data, const string& filename) 
{
    vector<int> sorted_data = data;

    sort(sorted_data.begin(), sorted_data.end());
    ofstream file(filename, ios::binary);

    for (const auto& value : sorted_data) {
        file << value << endl;
    }
}

// Слияние отсортированных блоков
void merge_blocks(const vector<string>& block_files, const string& output_file) 
{
    priority_queue<Element, vector<Element>, greater<Element>> min_heap;
    vector<ifstream> files;

    for (const auto& block_file : block_files) 
    {
        files.emplace_back(block_file);
    }

    for (int i = 0; i < files.size(); ++i) 
    {
        int value;
        if (files[i] >> value) 
        {
            min_heap.push({value, i});
        }
    }

    ofstream output(output_file);

    while (!min_heap.empty()) 
    {
        Element current = min_heap.top();
        min_heap.pop();
        output << current.value << endl;

        int value;
        if (files[current.block_id] >> value) 
        {
            min_heap.push({value, current.block_id});
        }
    }
}

// Внешняя многофазная сортировка
void external_sort(const string& input_file, const string& output_file, size_t block_size) 
{
    ifstream input(input_file);

    if (!input.is_open()) 
    {
        cerr << "Ошибка при чтении файла!" << endl;
        return;
    }

    vector<string> block_files;
    size_t block_id = 0;

    while (true) 
    {
        vector<int> block;
        if (!read_block(input, block, block_size)) 
        {
            break;
        }
        string block_filename = "block_" + to_string(block_id++) + ".txt";
        sort_save_block(block, block_filename);
        block_files.push_back(block_filename);
    }

    merge_blocks(block_files, output_file);

    // Удаляем временные файлы 
    for (const auto& file : block_files) 
    {
        if (fs::exists(file)) 
        {
            fs::remove(file);
        } else 
        {
            cerr << file << " not existing!" << endl;
        }
    }

    cout << "File is sorted" << output_file << endl;
}

int main() 
{
    string input_file = "C:\\Git\\ADS-Tasks\\Lab 12\\input.txt";
    string output_file = "C:\\Git\\ADS-Tasks\\Lab 12\\output.txt";

    size_t block_size = 1000; 

    external_sort(input_file, output_file, block_size);

    return 0;
}
