#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

bool isNumber(char a)
{
    return (a >= '0' && a <= '9');
}

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

string minusCheck(string str)
{
    if (str[0]=='-')
    {
        int i = 1;
        while (isNumber(str[i]))
        {
            i++;
        }
        str = str.insert(i, ")");
        str = "(0" + str;

    }
    return str;
}

bool check1 (string str)
{
    stack<char> stack;
    for (int i = 0; i < str.size(); i++)
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
    else return 0;
}

bool check2 (string str)
{
    for (int i = 0; i < str.size()-1; i++)
    {
        if ((str[i] == '+' || str[i] == '-' || str[i] == '*' || str[i] == '/') &&
        (str[i + 1] == '+' || str[i + 1] == '-' || str[i + 1] == '*' || str[i + 1] == '/' || i==0))
        {
            return 0;
        }
    }
    return 1;
}

int Priority(char i)
{
    if (i == '*' or i == '/') return 3;
    else if (i == '-' or i == '+') return 2;
    return 0;
}

string toRPN(string str)
{
    stack<char> steck;
    string output;

    if (str[0]=='-')
    {
        int i = 1;
        while (isNumber(str[i]))
        {
            i++;
        }
        str = str.insert(i, ")");
        str = "(0" + str;

    }

    for (int i = 0; i < str.size(); i++)
    {
        if (isNumber(str[i]))
        {
            while (i < str.size() && isNumber(str[i]))
            {
            output += str[i];
            i++;
            }
            output += ' ';
            i--;
        }
        else if (str[i]=='(') steck.push(str[i]);
        else if (str[i] == ')')
        {
            while (!steck.empty() && steck.top()!='(')
            {
                output += steck.top();
                output += ' ';
                steck.pop();
            }
            if (!steck.empty()) steck.pop();
        }
        else
        {
            while (!steck.empty() && Priority(steck.top())>=Priority(str[i]))
            {
                output += steck.top();
                output += ' ';
                steck.pop();
            }
            steck.push(str[i]);
        }
    }

    while (!steck.empty()) {
        output += steck.top();
        output += ' ';
        steck.pop();
    }
    return output;
}

int operation(int a,int b,char sign)
{
    switch (sign) {
        case '+':
            return a+b;
        case '-':
            return a-b;
        case '*':
            return a*b;
        case '/':
            return a/b;
        default:
            return sign;
    }
}

string calculate(string str)
{
    stack<int> steck;
    for (int i = 0; i < str.size(); i++)
    {
        if (isNumber(str[i]))
        {
            string temp = "";
            while (i < str.size() && isNumber(str[i]))
            {
            temp += str[i];
            i++;
            }
            steck.push(stoi(temp));
            i--;
        }
        else if (!steck.empty() && str[i]!=' ')
        {
            int b = steck.top();
            steck.pop();
            int a = steck.top();
            steck.pop();
            if (b==0 && str[i]=='/') return "Ошибка, деление на ноль";
            steck.push(operation(a,b,str[i]));
        }
    }
    return to_string(steck.top());
}

int main()
{
    string inpt;
    setlocale(LC_ALL,"rus");

    cout << "Введите выражение" << endl;
    cin >> inpt;
    inpt = minusCheck(inpt);

    if (check1(inpt)==0){
        cout << "Выражение с ошибкой" << endl;
        return -1;
    }
    if (check2(inpt)==0){
        cout << "Выражение с ошибкой" << endl;
        return -2;
    }
    std::cout << calculate(toRPN(inpt)) << endl;
    
    return 0;
}