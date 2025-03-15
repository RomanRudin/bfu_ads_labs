#include <iostream>
#include <vector>

using namespace std;

// Сначала расстояние(step) между элементами максимально, то есть равно размеру массива минус один. 
// Затем, пройдя массив с этим шагом, необходимо поделить шаг на фактор(factor = 1.25) уменьшения и пройти по списку вновь. 
// Так продолжается до тех пор, пока разность индексов не достигнет единицы.

void comb_sort(vector<int> &array)
{

    float factor = 1.25;
    int step = size(array)-1;

    while (step>=1)
    {
        for (int i=step; i<size(array);i++)
        {
            if (array[i-step]>array[i])
            {
                swap(array[i-step],array[i]);
            }
        }
        step /= factor;
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

    comb_sort(arr);

    for(int i = 0; i<size(arr);i++)
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
