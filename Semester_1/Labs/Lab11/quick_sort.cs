public class Quick
{
    public List<int> sort(List<int> a)
    {
        if (a.Count < 2)
            return a;
        int help = a[0];
        a.RemoveAt(0);
        var Leaft = new List<int>();
        var Right = new List<int>();
        foreach (var i in a)
        {
            if (i<help)
                Leaft.Add(i);
            
            else
                Right.Add(i);
            
        }

        var res = sort(Leaft);
        res.Add(help);
        res.AddRange(sort(Right));
        return res;
    }
}