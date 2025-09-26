public class Merge
{
    public  void Sort(int[] array, IComparer<int> comparer = null)
    {
        if (array == null) throw new ArgumentNullException(nameof(array));
        int n = array.Length;
        if (n < 2) return;

        comparer = Comparer<int>.Default;
        int[] aux = new int[n];
        SortImpl(array, aux, 0, n - 1, comparer);
    }

    

    private  void SortImpl(int[] a, int[] aux, int left, int right, IComparer<int> comp)
    {
        if (right - left + 1 <= a.Length)
        {
            InsertionSort(a, left, right, comp);
            return;
        }

        int mid = left + (right - left) / 2;
        SortImpl(a, aux, left, mid, comp);
        SortImpl(a, aux, mid + 1, right, comp);

        
        if (comp.Compare(a[mid], a[mid + 1]) <= 0) return;

        merge(a, aux, left, mid, right, comp);
    }

    private  void merge(int[] a, int[] aux, int left, int mid, int right, IComparer<int> comp)
    {
        int i = left, j = mid + 1, k = left;

        for (int t = left; t <= right; t++) aux[t] = a[t];

        while (i <= mid && j <= right)
        {
            if (comp.Compare(aux[i], aux[j]) <= 0)
                a[k++] = aux[i++];
            else
                a[k++] = aux[j++];
        }

        while (i <= mid) a[k++] = aux[i++]; 
        while (j <= right) a[k++] = aux[j++];
    }

    private  void InsertionSort(int[] a, int left, int right, IComparer<int> comp)
    {
        for (int i = left + 1; i <= right; i++)
        {
            int key = a[i];
            int j = i - 1;
            while (j >= left && comp.Compare(a[j], key) > 0)
            {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = key;
        }
    }
}
