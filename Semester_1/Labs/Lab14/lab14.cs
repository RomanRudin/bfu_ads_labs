using System.Text;
using System.Text.Unicode;
public class Lab14
{
    public void BuildFromFile(string inputPath)
    {
        
        string text = File.ReadAllText(inputPath, Encoding.UTF8);

        
        var words = text.Split(
            new[] { ' ', '\t', '\r', '\n' },
            StringSplitOptions.RemoveEmptyEntries);

        foreach (var w in words)
            Add(w);
        
    }
    
    
    protected static int _bucketCount = 223;
    
    private readonly List<string>?[] _buckets = new List<string>?[_bucketCount];

  
    public void WriteToFile(string outputPath)
    {
        using var writer = new StreamWriter(outputPath, false, Encoding.UTF8);
        for (int i = 0; i < _bucketCount; i++)
        {
            var list = _buckets[i];
            if (list == null || list.Count == 0) continue;
            
            var sb = new StringBuilder();
            sb.Append("Index ").Append(i).Append(": [");

            for (int j = 0; j < list.Count; j++)
            {
                sb.Append('\'').Append(list[j].Replace("'", "\\'")).Append('\'');
                if (j < list.Count - 1) sb.Append(", ");
            }

            sb.Append("]");
            writer.WriteLine(sb.ToString());
        }
    }

    
    protected void Add(string word)
    {
       
        byte[] bytes = Encoding.UTF8.GetBytes(word);
        uint hash = Fnv1a32(bytes);
        int index = (int)(hash % (uint)_bucketCount);
        
        if (_buckets[index] == null)
            _buckets[index] = new List<string>();

        _buckets[index]!.Add(word);
    }

    public uint Fnv1a32(byte[] data)
        {
            const uint fnvPrime = 16777619;
            const uint offset   = 2166136261;
            uint hash = offset;
    
            foreach (byte b in data)
            {
                hash ^= b;
                hash *= fnvPrime;
            }
            return hash;
        }
}

internal class Program()
{
    static void Main()
    {
        
        var builder = new Lab14();
        builder.BuildFromFile("input.txt");
        builder.WriteToFile("outt.txt");
    }
}