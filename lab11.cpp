#include "lab11.h"
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

std::unordered_map<int, int> graph_coloring(const std::vector<std::vector<int>>& graph, int num_colors) {
    std::unordered_map<int, int> colors; 

    for (int node = 0; node < graph.size(); node++) {
        std::unordered_set<int> used_colors; 

        for (int neighbor : graph[node]) {
            if (colors.find(neighbor) != colors.end()) {
                used_colors.insert(colors[neighbor]);
            }
        }
        for (int color = 1; color <= num_colors; color++) {
            if (used_colors.find(color) == used_colors.end()) {
                colors[node] = color;
                break;
            }
        }
    }
    return colors;
}

int main() {
    std::vector<std::vector<int>> graph = {
        {1, 2},     //  0 соединена с 1 и 2
        {0, 2, 3},  //  1 соединена с  0, 2 и 3
        {0, 1, 3},  //  2 соединена с  0, 1 и 3
        {1, 2}      //  3 соединена с  1 и 2
    };
    int num_colors = 3; 

    std::unordered_map<int, int> coloring = graph_coloring(graph, num_colors);

    std::cout << "GRAPH:" << std::endl;
    for (const auto& pair : coloring) {
        std::cout << "TOP " << pair.first << " COLOR " << pair.second << std::endl;
    }

    return 0;
}

