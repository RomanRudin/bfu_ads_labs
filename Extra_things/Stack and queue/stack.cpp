



//! IN NEED OF TESTING AND REFACTORING



template <typename T>
class stack
{
    struct Node
    {
        T data;
        Node* next;
        Node(T data) : data(data), next(nullptr) {}
    };

    Node* top;
    int size;

public:
    stack() : top(nullptr), size(0) {}

    ~stack()
    {
        while (top)
        {
            Node* temp = top;
            top = top->next;
            delete temp;
        }
    }

    void push(T data)
    {
        Node* newNode = new Node(data);
        newNode->next = top;
        top = newNode;
        size++;
    }

    T pop()
    {
        if (!top) throw std::runtime_error("Stack is empty");
        T data = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        size--;
        return data;
    }

    int getSize() const { return size; }

    bool empty() const { return !top; }
};
