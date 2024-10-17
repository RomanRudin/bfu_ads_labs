#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <filesystem>

//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK
//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK
//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK

void merge_files(const std::string& output_file, const std::vector<std::string>& temp_files, const std::string& path) {
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> heap_array;
    std::vector<std::ifstream> temp_file_streams;
    for (const auto& temp_file : temp_files) {
        temp_file_streams.emplace_back(temp_file);
    }

    std::ofstream output(output_file);
    for (size_t i = 0; i < temp_files.size(); ++i) {
        std::string element;
        std::getline(temp_file_streams[i], element);
        if (!element.empty()) {
            heap_array.emplace(std::stoi(element), i);
        }
    }

    int counter = 0;
    while (counter < temp_files.size()) {
        auto root = heap_array.top();
        heap_array.pop();
        output << root.first << '\n';

        std::string element;
        std::getline(temp_file_streams[root.second], element);
        if (!element.empty()) {
            heap_array.emplace(std::stoi(element), root.second);
        } else {
            ++counter;
        }
    }

    for (auto& temp_file_stream : temp_file_streams) {
        temp_file_stream.close();
    }
}

std::vector<std::string> create_initial_runs(const std::string& input_file, int run_size, const std::string& path) {
    std::vector<std::string> temp_files;
    std::ifstream input(input_file);
    bool end_of_file = false;
    int temp_files_counter = 0;

    if (!std::filesystem::exists(path)) {
        std::filesystem::create_directory(path);
    }

    while (true) {
        std::vector<int> data;
        for (int i = 0; i < run_size; ++i) {
            std::string line;
            std::getline(input, line);
            if (line.empty()) {
                end_of_file = true;
                break;
            }
            data.emplace_back(std::stoi(line));
        }
        std::sort(data.begin(), data.end());

        std::string temp_file = path + "/f_" + std::to_string(temp_files_counter) + ".txt";
        temp_files.emplace_back(temp_file);
        std::ofstream output(temp_file);
        for (const auto& value : data) {
            output << value << '\n';
        }

        ++temp_files_counter;

        if (end_of_file) {
            break;
        }
    }
    return temp_files;
}

void external_multiphase_sort(const std::string& path, int run_size) {
    std::string input_file = path + "/input.txt";
    std::string output_file = path + "/output.txt";
    std::string temp_files_path = path + "/Temp_files_linear";

    std::vector<std::string> temp_files = create_initial_runs(input_file, run_size, temp_files_path);
    merge_files(output_file, temp_files, temp_files_path);
}

//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK
//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK
//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK