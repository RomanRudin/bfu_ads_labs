public class comb_sort
{
    public void sort(int[] a)
    {
        
        int n = a.Length;
        while (n > 1)
        {
            int newN = 0;
            for (int i = 0; i < n - 1; i++)
            {
                if (a[i].CompareTo(a[i + 1]) > 0)
                {
                    (a[i], a[i + 1]) = (a[i + 1], a[i]);
                    newN = i + 1;
                }
            }

            n = newN;
        }
      
    }
}