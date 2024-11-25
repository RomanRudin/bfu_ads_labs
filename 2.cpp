#include <iostream>
#include <stack>
#include <sstream>
#include <vector>
#include <cctype>
#include <stdexcept>


// Функция для проверки, что скобки стоят верно
bool checkBrackets(const std::string& expr) 
{
    std::stack<char> brackets;
    for (char ch : expr) 
    {
        if (ch == '(') 
        {
            brackets.push(ch);
        }
        else if (ch == ')') 
        {
            if (brackets.empty()) 
            {
                return false;
            }
            brackets.pop();
        }
    }
    return brackets.empty();
}

// Функция для выполнения арифметических операций
double applyOp(double a, double b, char op) 
{
    switch (op) 
    {
    case '+': return a + b;
    case '-': return a - b;
    case '*': return a * b;
    case '/':
        if (b == 0) 
        {
            throw std::runtime_error("Ошибка: Деление на ноль.");
        }
        return a / b;
    }
    return 0;
}

// Функция для получения приоритета операции
int precedence(char op) 
{
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

// Основная функция для вычисления выражения
double evaluate(const std::string& expression) 
{
    std::stack<double> values; 
    std::stack<char> ops;

    for (size_t i = 0; i < expression.length(); i++) 
    {
        if (isspace(expression[i])) continue;
        if (isdigit(expression[i])) 
        {
            double value = 0;
            while (i < expression.length() && isdigit(expression[i])) 
            {
                value = (value * 10) + (expression[i] - '0');
                i++;
            }
            values.push(value);
            i--;
        }
        else if (expression[i] == '(') 
        {
            ops.push(expression[i]);
        }
        else if (expression[i] == ')') {
            while (!ops.empty() && ops.top() != '(') 
            {
                double val2 = values.top();
                values.pop();
                double val1 = values.top();
                values.pop();
                char op = ops.top();
                ops.pop();
                values.push(applyOp(val1, val2, op));
            }
            if (!ops.empty()) ops.pop();
        }
        else if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*' || expression[i] == '/') 
        {
            while (!ops.empty() && precedence(ops.top()) >= precedence(expression[i])) 
            {
                double val2 = values.top();
                values.pop();
                double val1 = values.top();
                values.pop();
                char op = ops.top();
                ops.pop();
                values.push(applyOp(val1, val2, op));
            }
            ops.push(expression[i]);
        }
    }

    while (!ops.empty()) 
    {
        double val2 = values.top();
        values.pop();
        double val1 = values.top();
        values.pop();
        char op = ops.top();
        ops.pop();
        values.push(applyOp(val1, val2, op));
    }

    return values.top();
}

int main() 
{
    setlocale(LC_ALL, "RU");
    std::string input;
    std::cout << "Введите математическое выражение (оканчивающееся на '='): ";
    std::getline(std::cin, input);
    if (!input.empty() && input.back() == '=') 
    {
        input.pop_back();
    }
    else 
    {
        std::cout << "Ошибка: выражение должно заканчиваться символом '='." << std::endl;
        return 1;
    }

    // Проверка на наличие ошибок
    if (!checkBrackets(input)) 
    {
        std::cout << "Ошибка: неверная расстановка скобок." << std::endl;
        return 1;
    }

    try 
    {
        double result = evaluate(input);
        std::cout << "Результат: " << result << std::endl;
    }
    catch (const std::runtime_error& e) 
    {
        std::cout << e.what() << std::endl;
    }

    return 0;
}
