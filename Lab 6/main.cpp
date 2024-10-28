#include <iostream>
#include <vector>

using namespace std;

void choice_sort(vector<int> &array)
{
    for(int i=0;i<size(array);i++)
    {
        int min = i;
        for(int j=i;j<size(array);j++)
        {
            if (array[j]<array[min])
            {
                min = j;
            }
        }
        swap(array[i],array[min]);
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

    choice_sort(arr);

    for(int i = 0; i<size(arr);i++)
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
