public class skobki
{
    
    public bool IsValid(string s)
    { 
        List<char> satk = new List<char>();

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i]==')')
            {
                if (satk.Count > 0 && satk[satk.Count - 1] == '(')
                    satk.RemoveAt(satk.Count - 1);
                else
                    return false;
            }
            else if (s[i]=='}')
            {
                if (satk.Count > 0 && satk[satk.Count - 1] == '{')
                    satk.RemoveAt(satk.Count - 1);
                else
                    return false;
            }
            else if (s[i]==']')
            {
                if (satk.Count > 0 && satk[satk.Count - 1] == '[')
                    satk.RemoveAt(satk.Count - 1);
                else
                    return false;
            }
            else if(s[i]=='('|| s[i]=='{'||s[i]=='[') 
                satk.Add(s[i]);
        }
        

        if (satk.Count>0)
        {
            return false;
        }

        return true;
    }
}
internal class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("enter string");
        var str = Console.ReadLine();
        var info = new skobki();
        Console.WriteLine(info.IsValid(str));
    }
}