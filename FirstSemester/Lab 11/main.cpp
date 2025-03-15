#include <iostream>
#include <vector>

using namespace std;

int partition ( vector<int> &arr , int low, int high )
{
    int pivot = arr[ ( low + high ) / 2 ];
    int i = low;
    int j = high;

    while(true)
    {
        while( arr[i] < pivot ) i++;
        while( arr[j] > pivot ) j--;

        if ( i >= j ) return j;

        swap ( arr[i], arr[j] );
        i++;
        j--;
    }
}
void quick_sort ( vector<int> &arr, int low, int high )
{
    if ( low < high )
    {
        int p = partition( arr, low, high );

        quick_sort( arr, low, p );
        quick_sort( arr, p + 1, high );
    }
}

int main()
{
    setlocale( LC_ALL, "rus" );
    vector<int> arr = {1,3,5,7,2,4,6,8};
    //{4,9,7,1,3,8,2,5,6}

     cout <<"Неотсортированный массив: "<< endl;
    for( int i = 0; i < size( arr ); i++ )
    {
        cout << arr[i] << ' ';
    }
    cout << endl << "Отсортированный массив: " << endl;

    quick_sort( arr, 0, size( arr ) - 1);

    for( int i = 0; i < size( arr ); i++ )
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
