#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

char flipBracket(char bracket) 
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

bool check (string str)
{
    stack<char> stack;
    for (int i; i < str.size(); i++)
    {
        if ((str[i] == '(') || (str[i] == '{') || (str[i] == '['))
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
                if (flipBracket(stack.top()) == str[i])
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
    if (stack.empty())
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