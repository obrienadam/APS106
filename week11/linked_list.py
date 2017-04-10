class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value): # Adds a node onto the end of the list
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.add_node(value)
            self.tail = self.tail.next

    def insert(self, i, value):
        if i == 0:
            self.head = Node(self.head, value)
            return

        last_node = self.head
        curr_node = self.head.next
        idx = 1

        while curr_node is not None:
            if idx == i:
                new_node = Node(curr_node, value)
                last_node.next = new_node
                return

            last_node = curr_node
            curr_node = curr_node.next
            idx += 1

        node = last_node
        for i in range(idx, i):
            node.next = Node(None, None)
            node = node.next

        node.next = Node(None, value)

    def __str__(self):
        nodes = []
        node = self.head

        while node is not None:
            nodes.append(str(node))
            node = node.next

        return str(nodes)

    def __len__(self):
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.next

        return length

    def __getitem__(self, i):
        idx = 0
        node = self.head

        if isinstance(i, int):
            while node is not None:
                if idx == i:
                    return node

                node = node.next
                idx += 1
            return 'Error! Index is out of bounds.'
        elif isinstance(i, slice):
            nodes = LinkedList()

            step = i.step if i.step else 1

            while node is not None:
                if idx >= i.start and idx < i.stop and (idx - i.start)%step == 0:
                    nodes.add_node(node.value)

                idx += 1
                node = node.next

            return nodes
        else:
            return 'Error! Invalid index type.'

class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def add_node(self, value): # Recursive add node
        if self.next is not None:
            return self.next.add_node(value)
        else:
            self.next = Node(value)
            return self

if __name__ == '__main__':
    ll = LinkedList()
    ll.add_node('Node 0')
    ll.add_node('Node 1')
    ll.add_node('Node 2')
    ll.add_node('Node 3')
    ll.add_node('Node 4')

    ll.insert(8, 'Inserted node')

    print(ll)
    print(len(ll))
    print(ll[3])
    print(ll[30])
    print(ll[1:6:2])