#include <iostream>

void combSort(int a[])
{
    float shrink = 1.247;
    int length = sizeof(a) / sizeof(a[0]);
    float gapFactor = length / shrink;
    int gap;
 
    while (gapFactor > 1) {
        gap = (int)gapFactor;
        for (int i = 0; i < length - gap; i++) {
            if (a[i] > a[i + gap]) {
                std::swap(a[i], a[i + gap]);
            }
        }
        gapFactor /= shrink;
    }
}