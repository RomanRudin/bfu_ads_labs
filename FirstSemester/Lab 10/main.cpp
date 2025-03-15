#include <iostream>
#include <vector>

using namespace std;

void merge( vector<int> &arr, int l, int r, int mid )                    
{
    int n1 = mid - l + 1;
    int n2 = r - mid;
    vector<int> L_arr(n1);
    vector<int> R_arr(n2);

    for ( int i = 0; i < n1; i++ )
    {
        L_arr[i] = arr[l+i];
    }

    for ( int j = 0; j < n2; j++ )
    {
        R_arr[j] = arr[mid + 1 + j];
    }

    int i = 0, j = 0, k = l;
    while ( i < n1 && j < n2 )
    {
        if ( L_arr[i] <= R_arr[j] )
        {
            arr[k] = L_arr[i];
            i++;
        }
        else
        {
            arr[k] = R_arr[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L_arr[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R_arr[j];
        j++;
        k++;
    }
}

void merge_sort ( vector<int> &arr, int l, int r )
{
    if (l<r)
    {
        int mid = ( l + r ) / 2;
        merge_sort ( arr, l, mid );
        merge_sort ( arr, mid + 1, r );
        merge ( arr, l, r, mid );

    }
        
}

int main()
{
    setlocale( LC_ALL, "rus" );
    vector<int> arr = {1,3,5,7,2,4,6,8};
    //{4,9,7,1,3,8,2,5,6}

     cout <<"Неотсортированный массив: "<< endl;
    for( int i = 0; i<size(arr);i++ )
    {
        cout << arr[i] << ' ';
    }
    cout << endl << "Отсортированный массив: " << endl;

    merge_sort( arr, 0, size( arr ) - 1);

    for( int i = 0; i < size( arr ); i++ )
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
