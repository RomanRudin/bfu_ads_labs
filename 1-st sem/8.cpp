/*
Дана последовательность чисел. Отсортировать и вывести последовательность чисел, определённым методом.
№8 Поразрядная
*/


#include <iostream>
#include <vector>

void quite_a_bit_Sort(std::vector<int>& arr)
{
    // Находим максимальное число в массиве
    int max = arr[0];
    for (int i = 1; i < arr.size(); i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }

    // Сортируем по разрядам
    for (int exp = 1; max / exp > 0; exp *= 10)
    {
        std::vector<int> output(arr.size());
        std::vector<int> count(10, 0);

        // Подсчет количества элементов для каждого разряда
        for (int i = 0; i < arr.size(); i++)
        {
            count[(arr[i] / exp) % 10]++;
        }

        // Обновление count для кумулятивного подсчета
        for (int i = 1; i < 10; i++) 
        {
            count[i] += count[i - 1];
        }

        // Распределение элементов в output
        for (int i = arr.size() - 1; i >= 0; i--) 
        {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }

        // Копирование отсортированных элементов в arr
        for (int i = 0; i < arr.size(); i++) 
        {
            arr[i] = output[i];
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

    quite_a_bit_Sort(numbers);

    std::cout << "Отсортированные числа: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
