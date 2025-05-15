/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№9 Пирамидальная (heap sort)
*/

#include <iostream>
#include <vector>


void heapify(std::vector<int>& numbers, int n, int i) 
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && numbers[left] > numbers[largest]) 
    {
        largest = left;
    }
    if (right < n && numbers[right] > numbers[largest]) 
    {
        largest = right;
    }

    if (largest != i) 
    {
        std::swap(numbers[i], numbers[largest]);
        heapify(numbers, n, largest);
    }
}

void heapSort(std::vector<int>& numbers) 
{
    int n = numbers.size();

    //Строим максимальную кучу
    for (int i = n / 2 - 1; i >= 0; i--) 
    {
        heapify(numbers, n, i);
    }

    //Извлекаем элементы из кучи
    for (int i = n - 1; i >= 0; i--) 
    {
        std::swap(numbers[0], numbers[i]);
        heapify(numbers, i, 0);
    }
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

    heapSort(numbers);

    std::cout << "Отсортированные числа: ";
    for (int i = 0; i < numbers.size(); i++) 
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
