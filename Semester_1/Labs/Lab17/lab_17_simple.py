from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




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



if __name__ == "__main__":
    bst = BST()
    while True:
        print(''' Enter the number of command you want to execute:
    1) insert the vertexes by values
    2) search the vertexes by values
    3) remove the vertexes by values
    4) traverse (using non-recursive method)
    0) Exit''')
        command = input()
        match command:
            case '1':
                bst.insert(int(input('Please, enter the values you want to inswrt: ')))
            case '2':
                parent, current = bst.search(int(input('Please, enter the values of the vertex you are searching: '))); 
                print(f'Parent value is {parent.value}, searched value is {current.value}')
            case '3':
                bst.remove(int(input('Please, enter the value of the vertex you are searching: ')))
            case '4':
                bst.traverseNonRecursive()
            case '0':
                break
            case _:
                continue
    bst.traverseNonRecursive()