/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№5 Вставками
*/


#include <iostream>
#include <vector>


void inserts(std::vector<int>& mas) 
{
    int n = mas.size();
    for (int i = 1; i < n; i++) 
    {
        int digit = mas[i];
        int j = i - 1;
        while (j >= 0 && mas[j] > digit) 
        {
            mas[j + 1] = mas[j];
            j--;
        }
        mas[j + 1] = digit;
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


    std::cout << "Исходная последовательность: ";
    for (int i = 0; i < numbers.size(); i++) 
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    inserts(numbers);

    std::cout << "Отсортированная последовательность: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
