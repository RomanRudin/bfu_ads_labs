public class Heap
{
    public void HeapSort(int [] a)
    {
        
        
            int n = a.Length;
            if (n < 2) return;

            for (int i = Parent(n - 1); i >= 0; i--)
                SiftDown(a, i, n);

            for (int end = n - 1; end > 0; end--)
            {
                Swap(a, 0, end);        
                SiftDown(a, 0, end);    
            }
    }

        static void SiftDown<T>(T[] a, int i, int n) where T : IComparable<T>
        {
            while (true)
            {
                int left = 2 * i + 1;
                if (left >= n) break;

                int right = left + 1;
                int largest = left;
                if (right < n && a[right].CompareTo(a[left]) > 0)
                    largest = right;

                if (a[largest].CompareTo(a[i]) <= 0) break;

                Swap(a, i, largest);
                i = largest;
            }
        }

        static int Parent(int i) => (i - 1) / 2;

        static void Swap<T>(T[] a, int i, int j)
        {
            (a[i], a[j]) = (a[j], a[i]);
        }
    
}