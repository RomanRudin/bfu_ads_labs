#include <iostream>
#include <vector>

using namespace std;

void heapify(vector<int> &arr, int n,int i)                    
{
    int max = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    if (left < n && arr[left]>arr[max])
        max = left;

    if (right < n && arr[right]>arr[max])
        max = right;

    if (max!=i)
    {
        swap(arr[i],arr[max]);
        heapify(arr,n,max);
    }

}

void heap_sort(vector<int> &arr)
{
    int n = size(arr);
    for (int i = n/2 - 1; i>=0;i--)
        heapify(arr,n,i);
    
    for (int i=n-1;i>=0;i--)
    {
        swap(arr[0],arr[i]);
        heapify(arr,i,0);
    }
}

int main()
{
    setlocale(LC_ALL,"rus");
    vector<int> arr = {4,9,7,1,3,8,2,5,6};

     cout <<"Неотсортированный массив: "<< endl;
    for(int i = 0; i<size(arr);i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl << "Отсортированный массив: " << endl;

    heap_sort(arr);

    for(int i = 0; i<size(arr);i++)
    {
        cout <<arr[i] << ' ';
    }


    return 0;
}
