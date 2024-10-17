from queue import LifoQueue

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def traverseNonRecursive(self) -> None:
        stack = LifoQueue()
        stack.put(self)
        while not stack.empty():
            current = stack.get()
            while current:
                print(current.val, end=' ')
                if current.left:
                    stack.put(current.left)
                current = current.right



def create_tree(string: str) -> Node:
    return create_subtree(string, 0, len(string))

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



if __name__ == "__main__":
    bt = create_tree(input("Please, enter the linear-bracket string: ").strip())
    print('traverseNonRecursive: ')
    bt.traverseNonRecursive()