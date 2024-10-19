#include <iostream>
#include <queue>
#include <string>

class Node {
public:
    int value;
    Node* left;
    Node* right;

    Node(int value) : value(value), left(nullptr), right(nullptr) {}
};

class BST {
private:
    Node* root;

    void __insert(Node*& current, int value) {
        if (value < current->value) {
            if (!current->left) {
                current->left = new Node(value);
            } else {
                __insert(current->left, value);
            }
        } else if (value > current->value) {
            if (!current->right) {
                current->right = new Node(value);
            } else {
                __insert(current->right, value);
            }
        } else {
            throw std::runtime_error("Value already exists!");
        }
    }

    std::pair<Node*, Node*> __search(int value, Node* parent, Node* current) {
        if (value == current->value) {
            return {parent, current};
        } else if (value < current->value) {
            if (!current->left) {
                return {nullptr, nullptr};
            }
            return __search(value, current, current->left);
        } else {
            if (!current->right) {
                return {nullptr, nullptr};
            }
            return __search(value, current, current->right);
        }
    }

    Node* __minValueNode(Node* node) {
        Node* current = node;
        while (current->left) {
            current = current->left;
        }
        return current;
    }

    Node* __remove(Node* root, int value) {
        if (!root) {
            return nullptr;
        }

        if (value < root->value) {
            root->left = __remove(root->left, value);
        } else if (value > root->value) {
            root->right = __remove(root->right, value);
        } else {
            if (!root->left) {
                Node* temp = root->right;
                delete root;
                return temp;
            } else if (!root->right) {
                Node* temp = root->left;
                delete root;
                return temp;
            }

            Node* successor = __minValueNode(root->right);
            root->value = successor->value;
            root->right = __remove(root->right, successor->value);
        }
        return root;
    }

public:
    BST() : root(nullptr) {}

    void insert(int value) {
        if (!root) {
            root = new Node(value);
        } else {
            __insert(root, value);
        }
    }

    std::pair<Node*, Node*> search(int value) {
        if (!root) {
            return {nullptr, nullptr};
        }
        return __search(value, root, root);
    }

    void remove(int value) {
        root = __remove(root, value);
    }

    void traverseNonRecursive() {
        std::queue<Node*> queue;
        queue.push(root);
        while (!queue.empty()) {
            Node* current = queue.front();
            queue.pop();
            while (current) {
                std::cout << current->value << " -- ";
                if (current->left) {
                    queue.push(current->left);
                }
                current = current->right;
            }
        }
    }
};

int main() {
    BST bst;
    while (true) {
        std::cout << "Enter the number of command you want to execute:\n"
                  << "1) Insert the vertexes by values\n"
                  << "2) Search the vertexes by values\n"
                  << "3) Remove the vertexes by values\n"
                  << "4) Traverse (using non-recursive method)\n"
                  << "0) Exit\n";
        int command;
        std::cin >> command;

        switch (command) {
            case 1:
                int value;
                std::cout << "Please, enter the values you want to insert: ";
                std::cin >> value;
                bst.insert(value);
                break;
            case 2:
                std::cout << "Please, enter the values of the vertex you are searching: ";
                std::cin >> value;
                auto result = bst.search(value);
                if (result.first && result.second) {
                    std::cout << "Found: " << result.second->value << std::endl;
                } else {
                    std::cout << "Not found!" << std::endl;
                }
                break;
            case 3:
                std::cout << "Please, enter the value of the vertex you are searching: ";
                std::cin >> value;
                bst.remove(value);
                break;
            case 4:
                bst.traverseNonRecursive();
                break;
            case 0:
                return 0;
            default: 
                continue;
        }
    }
}