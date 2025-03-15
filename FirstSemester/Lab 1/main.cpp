#include <iostream>
#include <string>
#include <stack>
using namespace std;

char flipBracket(char bracket) //свитч для разворота скобок
{
    switch (bracket) {
        case '(':
            return ')';
        case ')':
            return '(';
        case '{':
            return '}';
        case '}':
            return '{';
        case '[':
            return ']';
        case ']':
            return '[';
        default:
            return bracket;
    }
}

bool check (string str) //функция проверки скобок
{
    stack<char> stack;
    for (int i; i < str.size(); i++)
    {
        if ((str[i] == '(') || (str[i] == '{') || (str[i] == '[')) //засовываем открывающие в стек
        {
            stack.push(str[i]);
        }
        else if ((str[i] == ')') || (str[i] == '}') || (str[i] == ']'))
        {
            if (stack.empty()) 
            {
                return 0;
            }
            else
            {
                if (flipBracket(stack.top()) == str[i]) //если стек не пустой то ставим в соответствие каждой открывающей скобке закрывающую, и убираем из из стека
                {
                    stack.pop();
                }
                else
                {
                    return 0;
                }
            }
        }
    }
    if (stack.empty())  //если в конце стек не пустой, то значит скобки расставленны неверно
    {
        return 1;
    }
    else{return 0;}
}

int main()
{
    string inpt;
    setlocale(LC_ALL,"rus");

    cout << "Введите строку" << endl;
    cin >> inpt;
    if (check(inpt)==1){
        cout << "Строка верная" << endl;
    }
    else 
    {
        cout << "Строка неверна" << endl;
    }
    return 0;
}