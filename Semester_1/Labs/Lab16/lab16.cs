
public class Node
{
    public int Value;
    public Node? Left;
    public Node? Right;

    public Node(int value) => Value = value;
}
public class TreeBuilder()
{
    private static int _pos;
    private static string _input = string.Empty;

    public static Node? Build(string input)
    {
        _input = input;
        _pos   = 0;
        SkipSpaces();
        return ParseNode();
    }

    private static void SkipSpaces()
    {
        while (_pos < _input.Length && char.IsWhiteSpace(_input[_pos]))
            _pos++;
    }

    private static int ParseNumber()
    {
        var sb = new StringBuilder();
        if (_input[_pos] == '-')
        {
            sb.Append('-');
            _pos++;
        }

        while (_pos < _input.Length && char.IsDigit(_input[_pos]))
        {
            sb.Append(_input[_pos]);
            _pos++;
        }

        return int.Parse(sb.ToString());
    }

    private static Node? ParseNode()
    {
        SkipSpaces();

        // Пустое поддерево
        if (_pos >= _input.Length ||
            _input[_pos] == ',' ||
            _input[_pos] == ')')
            return null;

        int value = ParseNumber();
        var node = new Node(value);

        SkipSpaces();

        if (_pos < _input.Length && _input[_pos] == '(')
        {
            _pos++;                     // '('
            node.Left = ParseNode();    // левое поддерево

            SkipSpaces();
            if (_pos < _input.Length && _input[_pos] == ',')
                _pos++;                 // ','

            node.Right = ParseNode();   // правое поддерево

            SkipSpaces();
            if (_pos < _input.Length && _input[_pos] == ')')
                _pos++;                 // ')'
        }

        return node;
    }
}
public class lab16
{
    public  string PreOrderIterative(Node? root)
    {
        if (root == null) return string.Empty;

        var stack = new Stack<Node>();
        var result = new List<int>();

        stack.Push(root);

        while (stack.Count > 0)
        {
            Node cur = stack.Pop();
            result.Add(cur.Value);          // обработка узла (root)

            
            if (cur.Right != null) stack.Push(cur.Right);
            if (cur.Left  != null) stack.Push(cur.Left);
        }

        return string.Join(" ", result);
    }
}