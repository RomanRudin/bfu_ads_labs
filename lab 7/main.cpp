#include <iostream>
#include <vector>

using namespace std;

void shell_sort(vector<int> &array)
{
    for(int d=size(array)/2;d>0;d/=2)
    {
        for(int i=d;i<size(array);i++)
        {
            for(int j=i;j>0 && array[j-d]>array[j];j-d)
            {
                swap(array[j-d], array[j]);
            }

        }
    }
}

int main()
{
    setlocale(LC_ALL,"rus");
    vector<int> arr = {9,4,7,1,3,0,8,2,5,6};

     cout <<"Неотсортированный массив: "<< endl;
    for(int i = 0; i<size(arr);i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl << "Отсортированный массив: " << endl;

    shell_sort(arr);

    for(int i = 0; i<size(arr);i++)
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
