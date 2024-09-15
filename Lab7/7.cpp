#include <iostream>

void shellSort(int a[]) {
    int length = sizeof(a) / sizeof(a[0]);
    int step = length / 2;
    while (step > 0) {
        for (int i = step; i < length; i++) {
            int j = i;
            int difference = j - step;
            while ((difference >= 0) && (a[difference] > a[j])) {
                std::swap(a[difference], a[j]);
                j = difference;
                difference = j - step;
            }
        }
        step /= 2;
    }
}