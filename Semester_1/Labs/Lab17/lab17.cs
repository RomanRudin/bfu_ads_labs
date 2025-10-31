using System.Text;

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
public class lab17
{
        public  Node? Search(Node? root, int key)
        {
            if (root == null) return null;
            if (key == root.Value) return root;
            return key < root.Value
                ? Search(root.Left, key)
                : Search(root.Right, key);
        }
        public Node Insert(Node? root, int key)
        {
            if (root == null) return new Node(key);

            if (key < root.Value)
                root.Left = Insert(root.Left, key);
            else if (key > root.Value)
                root.Right = Insert(root.Right, key);
        

            return root;
        }

    
        public Node? Delete(Node? root, int key)
        {
            if (root == null) return null;

            if (key < root.Value)
                root.Left = Delete(root.Left, key);
            else if (key > root.Value)
                root.Right = Delete(root.Right, key);
            else 
            {
            
                if (root.Left == null) return root.Right;
            
                if (root.Right == null) return root.Left;

            
                Node min = FindMin(root.Right);
                root.Value = min.Value;
                root.Right = Delete(root.Right, min.Value);
            }

            return root;
        }

        private Node FindMin(Node node)
        {
            while (node.Left != null) node = node.Left;
            return node;
        }

    
        public string ToLinearString(Node? node)
        {
            if (node == null) return string.Empty;

            var sb = new StringBuilder();
            sb.Append(node.Value);

            if (node.Left != null || node.Right != null)
            {
                sb.Append('(');
                sb.Append(ToLinearString(node.Left));
                sb.Append(',');
                sb.Append(ToLinearString(node.Right));
                sb.Append(')');
            }

            return sb.ToString();
        }
    }
