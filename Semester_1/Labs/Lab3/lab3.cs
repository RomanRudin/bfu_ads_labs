

internal class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("The answer");
        int x = Convert.ToInt32(Console.ReadLine());
        
        List<int> count_x = new List<int>();
        int help = 0;

        int max_POW = (int)((Math.Log(x)/Math.Log(3))+1);
        
        for (int i = 0; i <= max_POW; i++)
        {
            for (int j = 0; j <= max_POW; j++)
            {
                for (int k = 0; k <= max_POW; k++)
                {
                    help = (int)(Math.Pow(3, i) * Math.Pow(5, j) * Math.Pow(7, k));
                    
                    
                    if (count_x.Contains(help)==false && help <= x && help>0)
                    {
                        count_x.Add(help);
                    }
                }
            }
        }

        help = 0;
        foreach (var VARIABLE in count_x)
        {
            help++;
            if (help<10)
            {
                Console.Write($"{VARIABLE} ");
            }
            else if (help==10)
            {
                Console.Write($"{VARIABLE} ");
                help = 0;
                
            }



        }
        Console.ReadLine();
    }
}