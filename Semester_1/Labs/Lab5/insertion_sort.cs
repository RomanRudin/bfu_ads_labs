public class InsertionSort
{
    public void insertionSort(int [] a)
    {
        int length = a.Length;
        
        for (int i = 1; i < length; i++)
        {
            var j = i  ;
            while (j > 0 && a[j-1]>a[j])
            {
                (a[j], a[j - 1]) = (a[j - 1], a[j]);
                j--;
                
            }
            
        }
    }
}