#include <iostream>

void insertionSort(int a[]){
    int length = sizeof(a) / sizeof(a[0]);
    for (int i = 1; i < length; i++) {
        int j = i;
        while (j > 0 && a[j] < a[j - 1]) {
            std::swap(a[j], a[j - 1]);
            j -= 1;
        }
    }
}