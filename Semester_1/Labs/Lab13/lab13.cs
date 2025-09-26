using System;
using System.IO;
using System.Text;
public class Lab13
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
    
    private class Node
    {
        public string Word { get; }
        public uint   Hash { get; }
        public Node?  Next { get; set; }

        public Node(string word, uint hash)
        {
            Word = word;
            Hash = hash;
        }
    }

    private static int _bucketCount = 1171;//простое число
   
    private readonly Node?[] _buckets = new Node?[_bucketCount];
    
    public void WriteToFile(string outputPath)
    {
        using var writer = new StreamWriter(outputPath, false, Encoding.UTF8);
        for (int i = 0; i < _bucketCount; i++)
        {
            if (_buckets[i] == null) continue;

            writer.WriteLine($"Bucket {i}:");
            
                writer.WriteLine($"  [{_buckets[i]!.Hash:X8}] {_buckets[i]?.Word}");
            
        }
    }
  protected void Add(string word)
    {
        // получаем байтовое представление слова (UTF‑8)
        byte[] bytes = Encoding.UTF8.GetBytes(word);
        uint hash = Fnv1a32(bytes);

        int index = (int)(hash % (uint)_bucketCount);

        // вставка в начало цепочки
        var node = new Node(word, hash) { Next = _buckets[index] };
        _buckets[index] = node;
    }

    // 32‑битный FNV‑1a – простая, быстрая хеш‑функция
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
        var builder = new Lab13();
        var builder4 = new Lab14();
        builder.BuildFromFile("input.txt");
        builder.WriteToFile("outt.txt");
    }
}
