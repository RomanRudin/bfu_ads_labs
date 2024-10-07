#include <iostream>
#include <unordered_map>
#include <stack>
#include <string>


bool checkBrackets(std::string input) {
    std::stack<char> stack;

    for (int i = 0; i < input.size(); i++) {
        switch (input[i]) 
        {
        case '{' || '[' || '(':
            stack.push(input[i]);
            break;
        case ')':
            if ((stack.empty()) || (stack.top() != '(')) {
                std::cout << "The answer: false" << std::endl;
                return false;
            }
            else 
                stack.pop();
            break;
        case ']':
            if ((stack.empty()) || (stack.top() != '[')) {
                std::cout << "The answer: false" << std::endl;
                return false;
            }
            else 
                stack.pop();
            break;
        case '}':
            if ((stack.empty()) || (stack.top() != '{')) {
                std::cout << "The answer: false" << std::endl;
                std::cout << "Reason: bracket " << stack.top() << " was never closed" << std::endl;
                return false;
            }
            else 
                stack.pop();
            break;
        default:
            std::cout << "The answer: false" << std::endl;
            std::cout << "Reason: Unknown symbol" << std::endl;
            return false;
        }
    }
    if (stack.empty()) {
        std::cout << "The answer: true" << std::endl;
        return true;
    } else {
        std::cout << "The answer: false" << std::endl;
        std::cout << "Reason: bracket " << stack.top() << " was never closed" << std::endl;
        return false;
    }
}

int main() {
    std::string input;
    std::cout << "Please, enter brackets: " << std::endl;
    std::cin >> input;
    checkBrackets(input);
}