#include <iostream>
#include <vector>
#include <ctime>

void shell_sort(std::vector<int>& data)//сортировка шелла
{
	for (int step = data.size() / 2; step > 0; step /= 2)
		for (int i = step; i < data.size(); i++)
			for (int j = i; j > step - 1 && data[j - step] > data[j]; j -= step)
				std::swap(data[j], data[j - step]);
}

int main()
{
	srand(time(NULL));

	std::vector<int> data;
	int num = 1500;

	for (int i = 0; i < num; i++)
		data.push_back(rand());

	shell_sort(data);

	bool check = true;
	std::cout << data[0] << std::endl;
	for (int i = 1; i < num; i++)
	{
		if (data[i] < data[i - 1])
			check = false;
		std::cout << data[i] << std::endl;
	}

	if (check)
		std::cout << "sorted correctly" << std::endl;
	else
		std::cout << "sorted not correctly" << std::endl;


	return 0;
}