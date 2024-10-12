#include <iostream>
#include <vector>

int int_log(int base, int argument) // логарифм, возвращающий целое число
{
	if (base < 1)
		throw std::exception("Wrong base");
	if (argument <= 0)
		throw std::exception("Wrong argument");
	
	int counter = 0;
	float tmp = argument;
	while (tmp >= base){
		tmp /= base;
		counter++;
	}
	return counter;
}

int pow(int base, int exponent) // возведение в степень
{
	if (exponent == 0)
		return 1;
	int tmp = base;
	for (int i = 0; i < exponent-1; i++)
		tmp *= base;
	return tmp;
}

void comb_sort(std::vector<int>& data)//сортировка расчёской
{
	int step = data.size() / 1.247;

	while (step > 0)
	{
		for (int i = 0; i < data.size() - step; i++)
			if (data[i] > data[i + step])
				std::swap(data[i], data[i + step]);

		step = step / 1.247;
	}
}

int main()
{
	setlocale(LC_ALL,"russian");

	int x;

	std::cout << "Введите число: " << std::endl;
	std::cin >> x;
	while (x < 1)
	{
		std::cout << "Число не принято, введите новое: " << std::endl;
		std::cin >> x;
	}
	std::cout << "Число принято." << std::endl;

	std::vector<int> result;

	for(int K = 0; K <= int_log(3,x); K++)
		for (int L = 0; L <= int_log(5, x); L++)
			for (int M = 0; M <= int_log(7, x); M++){
				int tmp = pow(3, K) * pow(5, L) * pow(7, M);
				if (tmp <= x && tmp > 0)
					result.push_back(tmp);
			}

	comb_sort(result);

	for (int i : result)
		std::cout << i << std::endl;

	return 0;
}