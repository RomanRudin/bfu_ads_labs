#include <iostream>
#include <cmath>

struct Node {
    int val;
    Node* next;
    Node* previous;
};

struct intList {
    Node* root;


    void print() { //Ready
        if (isEmpty()) return;
        Node* current = root->next;
        while (current != root) {
            std::cout << current->val << "\t";
            current = current->next;
        }
        std::cout << std::endl;
        return;
    }


    int length() { //Ready
        if (isEmpty()) return 0;
        int counter = 0;
        Node* current = root->next;
        while (current != root) {
            counter++;
            current = current->next;
        }
        return counter;
    }


    bool isEmpty() { //Ready
        return root->next == nullptr;
    }


    void appendLeft(int value) { //Ready
        Node* elem = new Node();
        elem->val = value;
        if (isEmpty()) {
            elem->next = root;
            elem->previous = root;
            root->next = elem;
            root->previous = elem;
            return;
        }
        elem->previous = root;
        elem->next = root->next;
        root->next->previous = elem;
        root->next = elem;
        return;
    }


    void appendRight(int value) { //Ready
        Node* elem = new Node();
        elem->val = value;
        if (isEmpty()) {
            elem->next = root;
            elem->previous = root;
            root->next = elem;
            root->previous = elem;
            return;
        }
        elem->previous = root->previous;
        elem->next = root;
        root->previous->next = elem;
        root->previous = elem;
        return;
    }


    void pop(Node* elem) { //Ready
        if ((elem->next == root) || (elem->previous == root)) {
            elem->previous->next = root;
            elem->next->previous = root;
            return;
        }
        elem->previous->next = elem->next;
        elem->next->previous = elem->previous;
        return;
    }


    void duplicate(Node* element) { //Ready
        Node* duplicated = new Node();
        duplicated->val = element->val;
        duplicated->previous = element;
        duplicated->next = element->next;
        element->next->previous = duplicated;
        element->next = duplicated;
        return;
    }


    void swap(Node* elem1, Node* elem2) {
        int temp = elem1->val;
        elem1->val = elem2->val;
        elem2->val = temp;
        return;
    }
};

bool isPrimary(int num) {
    if (num == 2) return true;
    for (int i = std::sqrt(num) + 1; i > 1; i--) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int getFirstDigit(int value){
    int num = value;
    while (num > 9) {
        num /= 10;
    }
    return num;
}

int main()
{
    int length;
    std::cout << "Please, input the length of the sequence:" << std::endl;
    std::cin >> length;

    std::cout << "Please, input elements of the sequence:" << std::endl;
    intList* list = new intList();
    Node* root = new Node();
    root->next = nullptr;
    root->val = -1;
    root->previous = nullptr;
    list->root = root;
    for (int i = 0; i < length; i++) {
        int input;
        std::cin >> input;
        list->appendRight(input);
    }
    std::cout << "The answer is:" << std::endl;

    bool startsWithThree = false;
    Node* checker = root->next;
    while (checker != root)
    {
        if (getFirstDigit(checker->val) == 3) {
            startsWithThree = true;
            break;
        }
        checker = checker->next;
    } 


    if (!startsWithThree) {
        Node* first = root->next;
        while (first != root->previous)
        {
            Node* second = first->next;
            while (second != root)
            {
                if (first->val % 10 < second->val % 10) {
                    list->swap(first, second);
                }
                second = second->next;
            }
            first = first->next;
        }
        list->print();
        return 1;
    }

    Node* current = root->next;

    int test = 0;
    while (current != root) {
        if ((current->val % 2 == 0) && (current->val != 2)) {
            list->pop(current);
            current = current->previous;
        }
        else if (isPrimary(current->val)) {
            list->duplicate(current);
            current = current->next;
        }
        current = current->next;
    }
    list->print();
    return 1;
}
