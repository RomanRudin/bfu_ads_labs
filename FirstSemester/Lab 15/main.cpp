#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Node // узел дерева
{
    int Value;
    Node* Left;
    Node* Right;

    Node(int val) : Value(val), Left(nullptr), Right(nullptr) {}
};


string no_spaces(const string& str) 
{
    string out;
    for (char ch : str) 
    {
        if (ch != ' ') 
        {
            out += ch;
        }
    }
    return out;
}

// Число из строки
int to_number(const string& str, size_t& pos) 
{
    int num = 0;
    while (pos < str.size() && isdigit(str[pos])) 
    {
        num = num * 10 + (str[pos] - '0');
        pos++;
    }
    return num;
}

// Парсер строки для построения дерева
Node* tree_parse(const string& input, size_t& pos) 
{

    if (pos >= input.size() || input[pos] == ')') 
        return nullptr;

    // Значение текущего узла
    if (!isdigit(input[pos])) 
        return nullptr;

    int value = to_number(input, pos);
    Node* node = new Node(value);

    if (pos < input.size() && input[pos] == '(') 
    {
        pos++;
        node->Left = tree_parse(input, pos); // Парсим левое поддерево
        if (pos < input.size() && input[pos] == ',') 
        {
            pos++; 
            node->Right = tree_parse(input, pos); // Парсим правое поддерево
        }
        if (pos < input.size() && input[pos] == ')') 
        {
            pos++;
        }
    }
    return node;
}


Node* parse(const string& input) 
{
    size_t pos = 0;
    return tree_parse(no_spaces(input), pos);
}

// Прямой 
void PreorderTraversal(Node* node, string& result) 
{
    if (!node) return;
    result += to_string(node->Value) + " "; // Обработка текущего узла
    PreorderTraversal(node->Left, result);   // Рекурсивный обход левого поддерева
    PreorderTraversal(node->Right, result);  // Рекурсивный обход правого поддерева
}

// Центральный 
void InorderTraversal(Node* node, string& result) 
{
    if (!node) return;
    InorderTraversal(node->Left, result);    // Рекурсивный обход левого поддерева
    result += to_string(node->Value) + " "; // Обработка текущего узла
    InorderTraversal(node->Right, result);   // Рекурсивный обход правого поддерева
}

// Концевой
void PostorderTraversal(Node* node, string& result) 
{
    if (!node) return;
    PostorderTraversal(node->Left, result);  // Рекурсивный обход левого поддерева
    PostorderTraversal(node->Right, result); // Рекурсивный обход правого поддерева
    result += to_string(node->Value) + " "; // Обработка текущего узла
}

int main() 
{
    string input = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13,)))";

    string NoSpc_input = no_spaces(input);

    Node* Root = parse(NoSpc_input);

    if (Root) 
    {
        string preorderResult, inorderResult, postorderResult;


        PreorderTraversal(Root, preorderResult);
        cout << "Прямой обход: " << preorderResult << endl;

        InorderTraversal(Root, inorderResult);
        cout << "Центральный обход: " << inorderResult << endl;


        PostorderTraversal(Root, postorderResult);
        cout << "Концевой обход: " << postorderResult << endl;
    }

    return 0;
}
