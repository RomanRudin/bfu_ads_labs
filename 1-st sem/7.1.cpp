/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№7 Шелла
*/


#include <iostream>
#include <vector>


void ShellSort(std::vector<int>& mas) 
{
    int n = mas.size();
    int start = n / 2;

    while (start > 0) 
    {
        for (int i = start; i < n; i++) 
        {
            int temp = mas[i];
            int j;
            for (j = i; j >= start && mas[j - start] > temp; j -= start) 
            {
                mas[j] = mas[j - start];
            }
            mas[j] = temp;
        }
        start /= 2;
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

    ShellSort(numbers);

    std::cout << "Отсортированные числа: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
