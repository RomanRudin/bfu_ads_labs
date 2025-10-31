
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
public class lab15
{
    
    
        public void PreOrder(Node? node, List<int> result)
        {
            if (node == null) return;
            result.Add(node.Value);          // Root
            PreOrder(node.Left, result);     // Left
            PreOrder(node.Right, result);    // Right
        }

        public void InOrder(Node? node, List<int> result)
        {
            if (node == null) return;
            InOrder(node.Left, result);      // Left
            result.Add(node.Value);          // Root
            InOrder(node.Right, result);     // Right
        }

        public void PostOrder(Node? node, List<int> result)
        {
            if (node == null) return;
            PostOrder(node.Left, result);    // Left
            PostOrder(node.Right, result);   // Right
            result.Add(node.Value);          // Root
        }

        
}