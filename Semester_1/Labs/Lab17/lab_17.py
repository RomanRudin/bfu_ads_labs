from typing import Any, LiteralString


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.children = [self.left, self.right]




class BST:
    def __init__(self):
        self.root = None


    def __insert(self, current, value) -> None:
        if value < current.value:
            if not current.left:
                current.left = Node(value)
            else:
                self.__insert(current.left, value)
        elif value > current.value:
            if not current.right:
                current.right = Node(value)
            else:
                self.__insert(current.right, value)
        else:
            raise Exception(f"{value} already exist!!")

    def insert(self, value) -> None:
        if not self.root:
            self.root = Node(value)
        else:
            self.__insert(self.root, value)


    def __search(self, value, parent, current) -> tuple | tuple[None, None] | Any | None:
        if value == current.value:
            return (parent, current)
        elif value < current.value:
            if not current.left:
                return (None, None)
            return self.__search(value, current, current.left)
        elif value > current.value:
            if not current.right:
                return (None, None)
            return self.__search(value, current, current.right)
        

    def search(self, value) -> tuple[None, None] | tuple | Any | None:
        if not self.root:
            return (None, None)
        return self.__search(value, parent=self.root, current=self.root)

    def __minValueNode(self, node) -> Any:
        current = node
        while current.left:
            current = current.left
        return current
    
        
    def __remove(self, root, value) -> Any | None:
        if not root:
            return None

        if value < root.value:
            root.left = self.__remove(root.left, value)
        elif value > root.value:
            root.right = self.__remove(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp

            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            successor = self.__minValueNode(root.right)
            root.value = successor.value
            root.right = self.__remove(root.right, successor.value)
        return root

    def remove(self, value) -> None:
        was_removed = self.__remove(self.root, value)


    def __traversePostOrder(self, current) -> None:
        print(current.value, end=' -- ')
        if current.left:
            self.__traversePostOrder(current.left)
        if current.right:
            self.__traversePostOrder(current.right)

    def traversePostOrder(self) -> None:
        self.__traversePostOrder(self.root)

    
    def __traverseInOrder(self, current) -> None:
        if current.left:
            self.__traverseInOrder(current.left)
        print(current.value, end=' -- ')
        if current.right:
            self.__traverseInOrder(current.right)

    def traverseInOrder(self) -> None:
        self.__traverseInOrder(self.root)


    def __traversePreOrder(self, current) -> None:
        if current.left:
            self.__traversePreOrder(current.left)
        if current.right:
            self.__traversePreOrder(current.right)
        print(current.value, end=' -- ')


    def traversePreOrder(self) -> None:
        self.__traversePreOrder(self.root) 

        
    def traverseNonRecursive(self) -> None:
        from queue import LifoQueue
        stack = LifoQueue()
        stack.put(self.root)
        while not stack.empty():
            current = stack.get()
            while current:
                print(current.value, end=' -- ')
                if current.left:
                    stack.put(current.left)
                current = current.right


    def draw(self) -> None:
        self.root.display()


    def inputBracketNotation(self, string: str) -> None:
        def find_right_subtree(string: str, start: int, end: int):
            bracket_counter = -1
            while True:
                if (start >= end): return -1
                if ((string[start] == ',') and (bracket_counter == 0)): return start + 1
                if string[start] == '(': bracket_counter += 1
                if string[start] == ')': bracket_counter -= 1
                start += 1

        def create_subtree(string: str, start: int, end: int) -> Node:
            while string[start] == ' ' or string[start] == '(': start += 1
            if (start >= end): return

            number = ''
            while string[start] in '1234567890':
                number += string[start]
                start += 1
                if start >= end: return Node(int(number))
            node = Node(int(number))

            right_subtree_index = find_right_subtree(string, start, end) - 1

            if right_subtree_index == -1:
                raise Exception("Wrong bracket notation string!")

            if right_subtree_index :
                node.left = create_subtree(string, start+1, right_subtree_index)
                node.right = create_subtree(string, right_subtree_index+1, end - 1)
            return node

        self.root = create_subtree(string, 0, len(string))




if __name__ == "__main__":
    bst = BST()
    while True:
        print(''' Enter the number of command you want to execute:
    1) insert the vertexes by values
    2) search the vertexes by values
    3) remove the vertexes by values
    4) traverse Pre-Order
    5) traverse In-Order
    6) traverse Post-Order
    7) traverse Non-Recursive
    8) Enter tree through bracket notation (changes the root element and doesn't assert, that the string is going to be BST)
    0) Exit''')
        command = input()
        match command:
            case '1':
                values = list(map(int, input('Please, enter the values you want to inswrt: ').strip().replace(',', ' ').split()))
                for value in values:
                    bst.insert(value)
            case '2':
                values = list(map(int, input('Please, enter the values of the vertex you are searching: ').strip().replace(',', ' ').split()))
                for value in values:
                    parent, current = bst.search(value); 
                    print(f'Parent value is {parent.value}, searched value is {current.value}')
            case '3':
                values = list(map(int, input('Please, enter the value of the vertex you are searching: ').strip().replace(',', ' ').split()))
                for value in values:
                    bst.remove(value)
            case '4':
                bst.traversePreOrder()
                print()
            case '5':
                bst.traverseInOrder()
                print()
            case '6':
                bst.traversePostOrder()
                print()
            case '7':
                bst.traverseNonRecursive()
                print()
            case '8':
                bst.inputBracketNotation(input('Please, enter the bracket notation string: '))
            case '0':
                break
            case _:
                continue
    bst.traverseInOrder()
    
        