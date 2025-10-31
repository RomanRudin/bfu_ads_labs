class Radix
{
    public  void RadixSort(int[] a)
    {
        if (a == null || a.Length < 2) return;

        int[] aux = new int[a.Length];
        const int B = 256;
        int[] count = new int[B];


        for (int byteIndex = 0; byteIndex < 4; byteIndex++)
        {
            Array.Clear(count, 0, B);


            for (int i = 0; i < a.Length; i++)
            {
                int key = (a[i] >> (byteIndex * 8)) & 0xFF;
                count[key]++;
            }

            
            for (int i = 1; i < B; i++) count[i] += count[i - 1];

            
            for (int i = a.Length - 1; i >= 0; i--)
            {
                int key = (a[i] >> (byteIndex * 8)) & 0xFF;
                aux[--count[key]] = a[i];
            }

            
            Array.Copy(aux, a, a.Length);
        }

        int firstPositive = 0;
        while (firstPositive < a.Length && (a[firstPositive] < 0)) firstPositive++;
        int idx = 0;
        while (idx < a.Length && a[idx] >= 0) idx++;
        
        if (idx > 0 && idx < a.Length)
        {
            Reverse(a, 0, idx - 1);
            Reverse(a, idx, a.Length - 1);
            Reverse(a, 0, a.Length - 1);
        }
    }

     void Reverse(int[] a, int i, int j)
    {
        while (i < j)
        {
            (a[i], a[j]) = (a[j], a[i]);
            i++;
            j--;
        }
    }
}