/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№11 Быстрая
*/


#include <iostream>
#include <vector>

int partition(std::vector<int>& mas, int low, int high) 
{
    int foothold = mas[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) 
    {
        if (mas[j] <= foothold) 
        {
            i++;
            std::swap(mas[i], mas[j]);
        }
    }
    std::swap(mas[i + 1], mas[high]);
    return (i + 1);
}

void fastSort(std::vector<int>& mas, int low, int high) {
    if (low < high) 
    {
        int pi = partition(mas, low, high);
        fastSort(mas, low, pi - 1);
        fastSort(mas, pi + 1, high);
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

    fastSort(numbers, 0, numbers.size() - 1);

    std::cout << "Отсортированные числа: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
