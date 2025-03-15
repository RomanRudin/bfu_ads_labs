#include <iostream>
#include <vector>

using namespace std;

int maxl(vector<int> arr) //нахождение максимального элемента
{
    int max = arr[0];
    for (int i=1; i<size(arr);i++)
        if (arr[i]>max)
            max = arr[i];

    return max;
}

void countSort(vector<int> &arr, int ei) //сортировка подсчётом
{
    vector<int> out_arr(size(arr));
    vector<int> c_arr(10,0);

    for (int i = 0 ;i < size(arr); i++)
    {
        c_arr[(arr[i]/ei)%10]++;  //подсчитываем кол-ва вхождения цифр в отдельный массив
    }

    for (int i = 1; i < 10;i++)
    {
        c_arr[i] += c_arr[i - 1]; //преобразовывам для того чтобы 
                                  //отображалось корректное местоположение
    }

    for (int i = size(arr) - 1; i >= 0; i--)
    {
        out_arr[c_arr[(arr[i]/ei)%10] - 1] = arr[i];  //составляем выходной массив
        c_arr[(arr[i]/ei)%10]--;
    }

    for (int i = 0; i < size(arr); i++)
        arr[i] = out_arr[i];
}

void radix_sort(vector<int> &arr)
{
    int max = maxl(arr);

        for(int i = 1; max/i>0 ; i*=10)
            countSort(arr,i);
}

int main()
{
    setlocale(LC_ALL,"rus");
    vector<int> arr = {90,4,774,777,33,0,8,2,1337,6};

     cout <<"Неотсортированный массив: "<< endl;
    for(int i = 0; i<size(arr);i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl << "Отсортированный массив: " << endl;

    radix_sort(arr);

    for(int i = 0; i<size(arr);i++)
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
