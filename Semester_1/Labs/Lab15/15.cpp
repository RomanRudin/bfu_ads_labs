#include <string>
#include <iostream>

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

        void traversePreOrder() {
            std::cout << this->value << ' ';
            if (this->left)
                this->left->traversePreOrder();
            if (this->right)
                this->right->traversePreOrder();
        }

        void traverseInOrder() {
            if (this->left)
                this->left->traverseInOrder();
            std::cout << this->value << ' ';
            if (this->right)
                this->right->traverseInOrder();
        }

        void traversePostOrder() {
            if (this->left)
                this->left->traversePostOrder();
            if (this->right)
                this->right->traversePostOrder();
            std::cout << this->value << ' ';
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
    std::cout << "Traverse In-Order: " << std::endl;
    tree->traverseInOrder();
    std::cout << std::endl;
    std::cout << "Traverse Post-Order: " << std::endl;
    tree->traversePostOrder();
    std::cout << std::endl;
    std::cout << "Traverse Pre-Order: " << std::endl;
    tree->traversePreOrder();
};
