public class selection_sort
{
    public void sort(int[] a)
    {
        for (int i = 0; i < a.Length; i++)
        {
            var minIndex = i;
            for (int j = i; j < a.Length; j++)
            {
                if (a[minIndex]>a[j])
                {
                    minIndex = j;
                }
                
            }

            if (minIndex!=i)
            {
                (a[i], a[minIndex]) = (a[minIndex], a[i]);
            }
        }
    }
}