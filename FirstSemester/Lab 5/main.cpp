#include <iostream>
#include <vector>

using namespace std;

//На каждом шаге алгоритма выбирается один из элементов входных данных и помещается на нужную позицию 
//в уже отсортированной последовательности до тех пор, пока набор входных данных не будет исчерпан.


void insert_sort(vector<int> &array)
{
    for(int i=1;i<size(array);i++)
    {
        for(int j=i;j>0;j--)
        {
            if(array[j-1]>array[j])
            {
                swap(array[j-1],array[j]);
            }
        }
    }
}

int main()
{
    setlocale(LC_ALL,"rus");
    vector<int> arr = {9,4,7,1,3,8,2,5,6};

     cout <<"Неотсортированный массив: "<< endl;
    for(int i = 0; i<size(arr);i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl << "Отсортированный массив: " << endl;

    insert_sort(arr);

    for(int i = 0; i<size(arr);i++)
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
