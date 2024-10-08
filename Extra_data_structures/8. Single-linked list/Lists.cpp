#include <iostream>
#include <cmath>

struct Node {
    int val;
    Node* next;
};

struct intList {
    Node* first;
    Node* last;


    Node* getElementByIndex(int index) {
        if (isEmpty()) throw;
        if (length() <= index) throw;
        if (index < 0) index += length();
        Node* current = first;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        return current;
    }


    int elem(int index) {
        return getElementByIndex(index)->val;
    }


    void print() {
        if (isEmpty()) return;
        Node* current = first;
        while (current) {
            std::cout << current->val << "\t";
            current = current->next;
        }
        std::cout << std::endl;
    }


    int length() {
        if (isEmpty()) return 0;
        int counter = 1;
        Node* current = first;
        while (current != last) {
            counter++;
            current = current->next;
        }
        return counter;
    }


    bool isEmpty() {
        return first == nullptr;
    }


    void append(int value) {
        Node* elem = new Node();
        elem->val = value;
        if (isEmpty()) {
            first = elem;
            last = elem;
            return;
        }
        last->next = elem;
        last = elem;
    }


    void pop(int index) {
        if (index == 0) {
            first = getElementByIndex(1);
            return;
        }
        if (index == length() - 1) {
            last = getElementByIndex(index - 1);
            return;
        }
        getElementByIndex(index - 1)->next = getElementByIndex(index + 1);
        return;
    }


    void duplicate(int index) {
        Node* elem = getElementByIndex(index);
        Node* duplicated = new Node();
        duplicated->val = elem->val;
        duplicated->next = elem->next;
        elem->next = duplicated;
    }


    void swap(int index1, int index2) {
        if (index1 < 0) throw;
        if (index2 < 0) throw;
        if (index1 == index2) return;
        if (index2 < index1) {
            int swap = index2;
            index2 = index1;
            index1 = swap;
        }

        int len = length() - 1;
        Node* swap1 = getElementByIndex(index1);
        Node* swap2 = getElementByIndex(index2);

        int temp = swap1->val;
        swap1->val = swap2->val;
        swap2->val = temp;
    }
};

bool contains(int num, int contains1, int contains2) {
    bool containsTOrN = false;
    while (num > 0) {
        if ((num % 10 == 3) || (num % 10 == 9)) {
            containsTOrN = true;
            break;
        }
        num /= 10;
    }
    return containsTOrN;
}

bool isPrimary(int num) {
    if (num == 2) return true;
    bool isPrimary = true;
    for (int i = std::sqrt(num) + 1; i > 1; i--) {
        if (num % i == 0) {
            isPrimary = false;
            break;
        }
    }
    return isPrimary;
}

int getFirstDigit(int num) {
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
    for (int i = 0; i < length; i++) {
        int input;
        std::cin >> input;
        list->append(input);
    }
    std::cout << "The answer is:" << std::endl;

    bool sortedByFirst = true;
    bool sortedByLast = true;
    for (int i = 0; i < length - 1; i++) {
        if (list->elem(i + 1) % 10 < list->elem(i) % 10) {
            sortedByFirst = false;
        }
        if (getFirstDigit(list->elem(i + 1)) < getFirstDigit(list->elem(i))) {
            sortedByLast = false;
        }
        if (!sortedByFirst && !sortedByLast) break;
    }

    if (sortedByFirst || sortedByLast) {
        int len = list->length();
        int counter = 0;
        while (counter < len) {
            std::cout << counter << "\t" << list->elem(counter) << std::endl;;
            if (!isPrimary(list->elem(counter))) {
                list->pop(counter);
                len--;
                counter--;
            }
            else if (contains(list->elem(counter))) {
                list->duplicate(counter);
                len++;
                counter++;
            }
            counter++;
        }
        list->print();
        return 1;
    }

    for (int i = 0; i < length - 1; i++) {
        for (int j = i + 1; j < length; j++) {
            std::cout << i << " " << list->elem(i) << "\t" << j << " " << list->elem(j) << std::endl;
            if (list->elem(i) > list->elem(j)) {
                std::cout << "Here!" << std::endl;
                list->swap(j, i);
            }
        }
    }
    list->print();
    return 1;
}
