#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <unordered_map>
#include <stdexcept>

// Function to check if brackets are correct
bool checkBrackets(const std::string& expression, const std::unordered_map<char, char>& bracketMap) {
    std::stack<char> stack;
    for (char c : expression) {
        if (bracketMap.find(c) != bracketMap.end()) {
            if (stack.empty() || stack.top() != bracketMap.at(c)) {
                return false;
            }
            stack.pop();
        }
        else if (c == '(') {
            stack.push(c);
        }
    }
    return stack.empty();
}

// Function to tokenize the input expression
std::vector<std::string> tokenize(const std::string& expression) {
    std::unordered_map<std::string, int> priority = {
        {"start", 0},
        {"(", 1},
        {")", 1},
        {"*", 3},
        {"/", 3},
        {"+", 2},
        {"-", 2}
    };

    std::string expr = expression;
    expr.erase(std::remove(expr.begin(), expr.end(), ' '), expr.end());
    expr.erase(std::remove(expr.begin(), expr.end(), '='), expr.end());

    if (!checkBrackets(expr, { {')', '('} })) {
        throw std::invalid_argument("Invalid brackets");
    }

    for (const auto& sym : priority) {
        size_t pos = 0;
        while ((pos = expr.find(sym.first, pos)) != std::string::npos) {
            expr.insert(pos, " ");
            expr.insert(pos + sym.first.size() + 1, " ");
            pos += sym.first.size() + 2;
        }
    }

    std::vector<std::string> tokens;
    size_t pos = 0;
    while ((pos = expr.find(" ")) != std::string::npos) {
        tokens.push_back(expr.substr(0, pos));
        expr.erase(0, pos + 1);
    }
    tokens.push_back(expr);

    return tokens;
}


// Function to get the priority of an operator
int getPriority(const std::string& op) {
    std::unordered_map<std::string, int> priority = {
        {"start", 0},
        {"(", 1},
        {")", 1},
        {"*", 3},
        {"/", 3},
        {"+", 2},
        {"-", 2}
    };

    return priority[op];
}


// Function to convert infix notation to RPN
// Function to convert infix notation to RPN
std::vector<std::string> convert(const std::vector<std::string>& tokens) {
    std::vector<std::string> result;
    std::stack<std::string> tempStack;

    for (const auto& token : tokens) {
        if (std::isdigit(token[0])) {
            result.push_back(token);
            continue;
        }

        if (token == "(") {
            tempStack.push(token);
        }
        else if (token == ")") {
            while (!tempStack.empty() && tempStack.top() != "(") {
                result.push_back(tempStack.top());
                tempStack.pop();
            }
            if (!tempStack.empty() && tempStack.top() == "(") {
                tempStack.pop();
            }
            else {
                throw std::invalid_argument("Unbalanced parentheses");
            }
        }
        else {
            while (!tempStack.empty() && tempStack.top() != "(" && getPriority(tempStack.top()) > getPriority(token)) {
                result.push_back(tempStack.top());
                tempStack.pop();
            }
            tempStack.push(token);
        }
    }

    while (!tempStack.empty()) {
        if (tempStack.top() == "(") {
            throw std::invalid_argument("Unbalanced parentheses");
        }
        result.push_back(tempStack.top());
        tempStack.pop();
    }

    return result;
}

// Function to evaluate the RPN expression
double evaluate(const std::vector<std::string>& tokens) {
    std::stack<double> stack;
    for (const auto& token : tokens) {
        if (std::isdigit(token[0])) {
            stack.push(std::stod(token));
        }
        else {
            double right = stack.top();
            stack.pop();
            double left = stack.top();
            stack.pop();

            if (token == "+") {
                stack.push(left + right);
            }
            else if (token == "-") {
                stack.push(left - right);
            }
            else if (token == "*") {
                stack.push(left * right);
            }
            else if (token == "/") {
                if (right == 0) {
                    throw std::invalid_argument("Division by zero");
                }
                stack.push(left / right);
            }
        }
    }

    return stack.top();
}

int main() {
    std::string expression;
    std::cout << "Enter an expression: ";
    std::getline(std::cin, expression);

    try {
        std::vector<std::string> tokens = tokenize(expression);
        std::vector<std::string> rpn = convert(tokens); //! ERROR OCCURES while inputting (2 + 3) * 4: clling back() on empty dequ. In need of fixing
        double result = evaluate(rpn);

        std::cout << "Result: " << result << std::endl;
    }
    catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}