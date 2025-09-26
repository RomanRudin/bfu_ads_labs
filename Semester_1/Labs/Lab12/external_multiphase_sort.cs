using static System.Diagnostics.Stopwatch;

public class external_multiphase_sort
{
     
    // Максимальный размер блока, который помещается в память (в байтах)
    private const long MaxChunkSize = unchecked(10 * 1024 * 1024); // 100 МБ

    
    private readonly string _inputPath;
    
    private readonly string _outputPath;
   
    private readonly string _tempDir = Path.Combine(Path.GetTempPath(), "ExternalSortRuns");

    public ouut(string inputPath, string outputPath)
    {
        _inputPath = inputPath;
        _outputPath = outputPath;
        Directory.CreateDirectory(_tempDir);
    }

    public void Sort()
    {
        var runFiles = CreateSortedRuns();
        MergeRuns(runFiles);
    }

   
    private List<string> CreateSortedRuns()
    {
        var runFiles = new List<string>();
        using var reader = new StreamReader(_inputPath);
        long currentChunkSize = 0;
        var numbers = new List<long>();

        while (!reader.EndOfStream)
        {
            string? line = reader.ReadLine()?.Trim();
            if (string.IsNullOrEmpty(line)) continue;          

            if (long.TryParse(line, out long value))
                numbers.Add(value);
            else
                throw new FormatException($"Не удалось разобрать число: \"{line}\"");

            currentChunkSize += System.Text.Encoding.UTF8.GetByteCount(line) + Environment.NewLine.Length;

            if (currentChunkSize >= MaxChunkSize)
            {
                runFiles.Add(WriteRun(numbers));
                numbers.Clear();
                currentChunkSize = 0;
            }
        }

        if (numbers.Count > 0)
            runFiles.Add(WriteRun(numbers));

        return runFiles;
    }

    private string WriteRun(List<long> numbers)
    {
        numbers.Sort();                     // сортировка по возрастанию
        string runPath = Path.Combine(_tempDir, $"run_{Guid.NewGuid()}.txt");
        File.WriteAllLines(runPath, numbers.Select(n => n.ToString()));
        return runPath;
    }
    
    private void MergeRuns(List<string> runFiles)
    {
        var readers = runFiles.Select(p => new StreamReader(p)).ToList();

        
        var pq = new SortedSet<QueueItem>(Comparer<QueueItem>.Create((a, b) =>
        {
            int cmp = a.Value.CompareTo(b.Value);
            if (cmp != 0) return cmp;
            
            return a.ReaderIndex.CompareTo(b.ReaderIndex);
        }));

        
        for (int i = 0; i < readers.Count; i++)
        {
            if (!readers[i].EndOfStream)
            {
                var line = readers[i].ReadLine()?.Trim();
                if (long.TryParse(line, out long val))
                    pq.Add(new QueueItem { Value = val, ReaderIndex = i });
            }
        }

        using var writer = new StreamWriter(_outputPath);
        while (pq.Count > 0)
        {
            var smallest = pq.Min;
            pq.Remove(smallest);
            writer.WriteLine(smallest.Value);

            var srcReader = readers[smallest.ReaderIndex];
            if (!srcReader.EndOfStream)
            {
                var line = srcReader.ReadLine()?.Trim();
                if (long.TryParse(line, out long val))
                    pq.Add(new QueueItem { Value = val, ReaderIndex = smallest.ReaderIndex });
            }
        }

        foreach (var r in readers) r.Dispose();
    }

    
    

    private class QueueItem
    {
        public long Value { get; set; }
        public int ReaderIndex { get; set; }
    }
    

        

    

//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK
//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK
//! REWRITTEN FROM PYTHON USING AI, IN NEED OF TESTING AND PROBABLY WON'T WORK
}