#include <string>
#include <iostream>
#include <stack>

namespace bt {
    template <class T>
    class Node {
    public:
        T value;
        Node* left = nullptr;
        Node* right = nullptr;

        ~Node() {
            if (this->left) delete this->left;
            if (this->right) delete this->right;
        }

        void traverseNonRecursive() {
            std::stack<Node<T>*> nodes_for_later;
            nodes_for_later.push(this);
            while (!nodes_for_later.empty()) {
                Node<T>* current = nodes_for_later.top();
                nodes_for_later.pop();
                while (current)
                {
                    std::cout << current->value << "\t";
                    if (current->left)
                        nodes_for_later.push(current->left);
                    current = current->right;
                }
            }
        }
    };



    int find_right_subtree(const std::string& str, int start, int end) {
        int bracket_counter = -1;
        while (true) {
            if (start >= end) return -1;
            if ((str[start] == ',') && (bracket_counter == 0)) return start + 1;
            if (str[start] == '(') bracket_counter += 1;
            if (str[start] == ')') bracket_counter -= 1;
            start += 1;
        };
    };


    template <class T>
    Node<T>* create_subtree(const std::string& str, int start, int end) {
        while ((str[start] == ' ') || (str[start] == '(')) start += 1;
        if (start >= end) return nullptr;

        int number = 0;
        while (((int)(str[start]) >= 48) && ((int)(str[start]) <= 57)) {
            number *= 10;
            number += (int)(str[start]) - 48;
            start += 1;
            if (start >= end) break;
        }
        Node<T>* node = new Node<T>;
        node->value = number;
        if (start >= end) return node;

        int right_subtree_index = find_right_subtree(str, start, end) - 1;
        node->left = create_subtree<T>(str, start + 1, right_subtree_index);
        node->right = create_subtree<T>(str, right_subtree_index + 1, end - 1);
        return node;
    };


    template <class T>
    Node<T>* create_tree(std::string str) {
        return create_subtree<T>(str, 0, str.length());
    };
};

int main() {
    std::string input;
    std::cout << "Please, input the bracket notation: \t";
    std::getline(std::cin, input);

    bt::Node<int>* tree = new bt::Node<int>;
    tree = bt::create_tree<int>(input);

    std::cout << std::endl;
    std::cout << "Traverse without recursion: " << std::endl;
    tree->traverseNonRecursive();
};
