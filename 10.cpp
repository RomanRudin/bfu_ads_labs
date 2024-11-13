/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№10 Слиянием
*/

#include <iostream>
#include <vector>

void merge(std::vector<int>& numbers, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++) {
        L[i] = numbers[left + i];
    }
    for (int j = 0; j < n2; j++) {
        R[j] = numbers[mid + 1 + j];
    }

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            numbers[k] = L[i];
            i++;
        }
        else {
            numbers[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        numbers[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        numbers[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& numbers, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(numbers, left, mid);
        mergeSort(numbers, mid + 1, right);
        merge(numbers, left, mid, right);
    }
}

void Sort(std::vector<int>& numbers) {
    mergeSort(numbers, 0, numbers.size() - 1);
}

int main() 
{
    setlocale(LC_ALL, "RUS");
    std::vector<int> numbers;
    int num;
    std::cout << "Введите числа (0 - окончание ввода): ";
    while (true) 
    {
        std::cin >> num;
        if (num == 0) 
        {
            break;
        }
        numbers.push_back(num);
    }

    std::cout << "Ваш ввод: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    Sort(numbers);

    std::cout << "Отсортированные числа: ";
    for (int i = 0; i < numbers.size(); i++) 
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
