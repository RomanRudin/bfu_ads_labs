from queue import LifoQueue

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # Traverse preorder
    # Прямой рекурсивный обход
    def traversePreOrder(self) -> None:
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    # центральный рекурсивный обход
    def traverseInOrder(self) -> None:
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    # обратный рекурсивный обход
    def traversePostOrder(self) -> None:
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

def create_tree(string: str) -> BinaryTree:
    string = string.strip()
    stack = LifoQueue()
    index, root_number = 0, ''

    while string[index] in '0123456789':
        index += 1
        root_number += string[index]
    root = Node(int(root_number))
    last_node = root
    bt = BinaryTree(root)

    while index < len(string):
        if string[index] == ' ': continue

        if string[index] in '0123456789':
            number = string[index]
            while string[index + 1] in '0123456789':
                index += 1
                number += string[index]
            node = Node(int(number))
            last_node.

        if string[index] == '(':
            pass

        if string[index] == ')':
            

        if string[index] == ',':
            pass

        index += 1
    return bt

if __name__ == "__main__":
    bt = create_tree(input("Please, enter the linear-bracket string: "))