public class Shell_sort
{
    public void shell_sort(int[] a)
    {
        
        
        var step = (a.Length / 2);
        var maksL = a.Length;
        var help = 0;

        while (step>0)
        {
            for (int i = step; i < maksL; i++)
            {
                var j = i;
                help = j - step;
                while (help>=0 && a[help]>a[j])
                {
                    (a[j], a[help]) = (a[help], a[j]);
                    j = help;
                    help = j - step;
                }
            }

            step /= 2;
        }

       
    }
}