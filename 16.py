# Лабораторная №16 “Не рекурсивный прямой обход” (реализуется с помощью стека).
# В качестве выходных данных формируется строка обхода.
# Например: Бинарное дерево поиска.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def pre_order_iterative(self):
        stack = []
        result = []

        node = self.root

        while node or stack:
            while node:
                result.append(node.value)
                stack.append(node)
                node = node.left

            node = stack.pop()
            node = node.right

        return ' '.join(map(str, result))


if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)

    result = tree.pre_order_iterative()
    print("Результат не рекурсивного прямого обхода:", result)
