class Node:
    def __init__(self, value=None):
        self.value = value
        self.l_node = None
        self.r_node = None

    def insert(self, value):
        if value < self.value:
            if self.l_node:
                self.l_node.insert(value)
            else:
                self.l_node = Node(value)
        else:
            if self.r_node:
                self.r_node.insert(value)
            else:
                self.r_node = Node(value)

    def is_in_tree(self, value):
        if value  == self.value: # Found the value!
            return True
        elif value < self.value and self.l_node:
            return self.l_node.is_in_tree(value)
        elif value > self.value and self.r_node:
            return self.r_node.is_in_tree(value)
        else:
            return False # No more nodes, cannot possibly be in the tree :(

    def print_node(self):
        print(self.value)

        if self.l_node:
            self.l_node.print_node()

        if self.r_node:
            self.r_node.print_node()

    def __len__(self):
        n = 1

        if self.r_node:
            n += self.r_node.__len__()

        if self.l_node:
            n += self.l_node.__len__()

        return n

if __name__ == '__main__':
    from random import randint

    tree = Node(50)

    for i in range(99):
        tree.insert(randint(1, 100))

    print(tree.is_in_tree(4))
    print(len(tree))
