/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№4 Сортировка методом прочесывания
*/


#include <iostream>
#include <vector>


void SortHairbrush(std::vector<int>& mas) 
{
    int n = mas.size();
    int step = n;
    bool swapped = true;

    while (step > 1 || swapped) 
    {
        step = (step * 10) / 13;
        if (step < 1) 
        {
            step = 1;
        }
        swapped = false;

        for (int i = 0; i < n - step; i++) 
        {
            if (mas[i] > mas[i + step])
            {
                std::swap(mas[i], mas[i + step]);
                swapped = true;
            }
        }
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

    SortHairbrush(numbers);

    std::cout << "Отсортированные числа: ";
    for (int i = 0; i < numbers.size(); i++) 
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
