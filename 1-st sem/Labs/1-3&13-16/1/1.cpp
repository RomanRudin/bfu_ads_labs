#include <iostream>
#include <string>

#include <ctime>
#include <vector>


bool check_string(std::string str)
{
	for (char i : str)
		if (i != '(' && i != ')' && i != '[' && i != ']' && i != '{' && i != '}')
		{
			std::cout << "В строке присутствуют лишние символы" << std::endl;
			return false;
		}

	int current_level = 0;
	bool is_correctly = true;
	
	int levels_size = str.size() / 2 +1;
	int** brace_levels = new int* [levels_size];
	for (int i = 0; i < levels_size; i++)
	{
		brace_levels[i] = new int[3];
		brace_levels[i][0] = brace_levels[i][1] = brace_levels[i][2] = 0;
	}

	for (char i : str)
	{
		/*/debug
		std::cout << "\nУровень: " << current_level << " Эл-т: " << i << std::endl;
		for (int lev = 0; lev < levels_size; lev++)
		{
			std::cout << lev << ' ';
			for (int br = 0; br < 3; br++)
				std::cout << brace_levels[lev][br] << ' ';
			std::cout << std::endl;
		}
		//debug*/

		switch (i)
		{
		case '(':
			if (current_level + 1 < levels_size)
			{
				brace_levels[current_level][0]++;
				current_level += 1;
			}
			else
				is_correctly = false;
				
			break;
		case '{':
			if (current_level + 1 < levels_size)
			{
				brace_levels[current_level][1]++;
				current_level += 1;
			}
			else
				is_correctly = false;

			break;
		case '[':
			if (current_level + 1 < levels_size)
			{
				brace_levels[current_level][2]++;
				current_level += 1;
			}
			else
				is_correctly = false;

			break;
		case ')':
			if (current_level == 0)
			{
				is_correctly = false;
				break;
			}

			if (brace_levels[current_level-1][0] == 1)
			{
				for(int j = current_level-1; j < levels_size; j++)
					if(brace_levels[j][1] != 0 || brace_levels[j][2] != 0)
					{
						is_correctly = false; 
						break;
					}
				
				current_level--;
				brace_levels[current_level][0] -= 1;
			}
			else
				is_correctly = false;
			break;
		case '}':
			if (current_level == 0)
			{
				is_correctly = false;
				break;
			}

			if (brace_levels[current_level - 1][1] == 1)
			{
				for (int j = current_level - 1; j < levels_size; j++)
					if (brace_levels[j][0] != 0 || brace_levels[j][2] != 0)
					{
						is_correctly = false;
						break;
					}

				current_level--;
				brace_levels[current_level][1] -= 1;
			}
			else
				is_correctly = false;
			break;

		case ']':
			if (current_level == 0)
			{
				is_correctly = false;
				break;
			}

			if (brace_levels[current_level - 1][2] == 1)
			{
				for (int j = current_level - 1; j < levels_size; j++)
					if (brace_levels[j][1] != 0 || brace_levels[j][0] != 0)
					{
						is_correctly = false;
						break;
					}

				current_level--;
				brace_levels[current_level][2] -= 1;
			}
			else
				is_correctly = false;
			break;

		default:
			break;
		}

		if (!is_correctly)
			break;
	}

	for (int i = 0; i < str.size() / 2; i++)
	{
		if (is_correctly)
		{
			for (int j = 0; j < 3; j++)
				if (brace_levels[i][j] != 0)
					is_correctly = false;
		}

		delete[] brace_levels[i];
	}
	delete[] brace_levels;

	if (is_correctly)
	{
		std::cout << "Скобки в строке расставленны верно" << std::endl;
		return true;
	}
	else
	{
		std::cout << "Скобки в строке расставленны неверно" << std::endl;
		return false;
	}
}

int main()
{
	setlocale(LC_ALL, "russian");
	
	std::string input_string;

	std::cout << "Введите строку: " << std::endl;
	std::cin >> input_string;

	check_string(input_string);
	

	/*srand(time(NULL));
	std::vector<std::string> true_str;
	std::vector<std::string> false_str;

	std::string use = "({[]})";

	for (int i = 0; i < 10000; i++)
	{
		std::string tmp;

		for (int i = 0; i < 6; i++)
			tmp.push_back(use[rand() % 6]);

		if (check_string(tmp))
			true_str.push_back(tmp);
		else
			false_str.push_back(tmp);
	}

	std::cout << "False strings:" << std::endl;
	for (int i = 0; i < false_str.size(); i++)
		std::cout << false_str[i] << std::endl;
	std::cout << "True strings:" << std::endl;
	for (int i = 0; i < true_str.size(); i++)
		std::cout << true_str[i] << std::endl;
		*/
	return 0;
}