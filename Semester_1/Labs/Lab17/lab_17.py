class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def __insert(self, current, key):
        if key < current.key:
            if not current.left:
                current.left = Node(key)
            else:
                self.__insert(current.left, key)
        elif key > current.key:
            if not current.right:
                current.right = Node(key)
            else:
                self.__insert(current.right, key)
        else:
            raise Exception(f"{key} already exist!!")

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.__insert(self.root, key)

    def __search(self, key, parent, current):
        if key == current.key:
            return (parent, current)
        elif key < current.key:
            if not current.left:
                return (None, None)
            return self.__search(key, current, current.left)
        elif key > current.key:
            if not current.right:
                return (None, None)
            return self.__search(key, current, current.right)
        

    def search(self, key):
        if not self.root:
            return (None, None)
        return self.__search(key, parent=self.root, current=self.root)

    def __count_children(self, sub_tree):
        cnt = 0
        if sub_tree.left:
            cnt +=1
        
        if sub_tree.right:
            cnt += 1    
        return cnt

    def __min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
        
    def __remove(self, root, key):
        if not root:
            return None

        if key < root.key:
            root.left = self.__remove(root.left, key)
        elif key > root.key:
            root.right = self.__remove(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp

            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            successor = self.__min_value_node(root.right)
            root.key = successor.key
            root.right = self.__remove(root.right, successor.key)
        return root

    def remove(self, key):
        self.__remove(self.root, key)

    def __traverse_post_order(self, current):
        print(current.key, end=' -- ')
        if current.left:
            self.__traverse_post_order(current.left)
        if current.right:
            self.__traverse_post_order(current.right)

    def traverse_post_order(self):
        self.__traverse_post_order(self.root)
    
    def __traverse_in_order(self, current):
        if current.left:
            self.__traverse_in_order(current.left)
        print(current.key, end=' -- ')
        if current.right:
            self.__traverse_in_order(current.right)

    def traverse_in_order(self):
        self.__traverse_in_order(self.root)

    def __traverse_pre_order(self, current):
        if current.left:
            self.__traverse_pre_order(current.left)
        if current.right:
            self.__traverse_pre_order(current.right)
        print(current.key, end=' -- ')

    def traverse_pre_order(self):
        self.__traverse_pre_order(self.root) 