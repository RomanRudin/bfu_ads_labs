#include <iostream>

void selectionSort(int a[]){
    int length = sizeof(a) / sizeof(a[0]);
    for (int i = 0; i < length - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < length; j++) {
            if (a[j] < a[minIndex])
                minIndex = j;
        std::swap(a[i], a[minIndex]);
        }
    }
}