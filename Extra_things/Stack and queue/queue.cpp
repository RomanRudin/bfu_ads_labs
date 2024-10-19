template <typename T>
class queue{
    struct Node{
        T data;
        Node* next;
        Node(T data) : data(data), next(nullptr) {}
    };
    Node* front;
    Node* rear;
public:
    queue() : front(nullptr), rear(nullptr) {}
    ~queue() {
        while (front) {
            Node* temp = front;
            front = front->next;
            delete temp;
        }
    }
    void push(T data) {
        Node* newNode = new Node(data);
        if (!front) {
            front = newNode;
            rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
    }
    T pop() {
        if (!front) throw std::runtime_error("Queue is empty");
        T data = front->data;
        Node* temp = front;
        front = front->next;
        delete temp;
        return data;
    }
    bool empty() const { return !front; }
};