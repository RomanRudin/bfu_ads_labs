/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№6 Посредством выбора
*/


#include <iostream>
#include <vector>


void choice(std::vector<int>& mas)
{
    int n = mas.size();
    for (int i = 0; i < n - 1; i++) 
    {
        int min = i;
        for (int j = i + 1; j < n; j++) 
        {
            if (mas[j] < mas[min]) 
            {
                min = j;
            }
        }
        std::swap(mas[min], mas[i]);
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

    choice(numbers);

    std::cout << "Отсортированная последовательность: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
