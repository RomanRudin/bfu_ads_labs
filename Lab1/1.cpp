#include <iostream>
#include <unordered_map>
#include <stack>
#include <string>

int main() {
    std::unordered_map<char , char> brackets = {{')', '()'}, {']', '[]'}, {'}', '{}'}};
    std::stack<char> stack;

    std::string input;
    std::cout << "Please, enter brackets: " << std::endl;
    std::cin >> input;

    for (int i = 0; i < input.size(); i++) {
        // TODO
        // if (brackets.find(input[i]) != brackets.end()) {
        //     if (!stack.empty()) {
        //         if (stack.top() == brackets[input[i]]) {
        //             stack.pop();
        //         } else {
        //             std::cout << "The answer: false" << std::endl;
        //             return 0;
        //         }
        //     } else {
        //         std::cout << "The answer: false" << std::endl;
        //         return 0;
        //     }
        // } else {
        //     stack.push(input[i]);
        // }
    }
    if (stack.empty()) {
        std::cout << "The answer: true" << std::endl;
    } else {
        std::cout << "The answer: false" << std::endl;
    }
    return 0;
}