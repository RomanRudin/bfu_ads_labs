#include <iostream>

using namespace std;

bool check(int xi)
{
    int out = xi;
    while (xi!=1)
    {
        if (xi%3==0)
        {
            xi /= 3;
        }
        else if (xi%5==0)
        {
            xi /= 5;
        }
        else if (xi%7==0)
        {
            xi /= 7;
        }
        else
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int x;

    setlocale(LC_ALL,"rus");

    cout << "Введите число x: ";
    cin >> x;

    cout << "Условию удовлетворяют: " << endl;
    for (int i=1; i<=x; i++)
    {
        if(check(i))
        {
            cout << i << endl;
        }
    }

    
}