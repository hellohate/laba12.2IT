class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


def split_list(dll):
    l1 = DoublyLinkedList()
    l2 = DoublyLinkedList()

    current = dll.head
    while current:
        if current.data > 0:
            l1.append(current.data)
        elif current.data < 0:
            l2.append(current.data)
        current = current.next

    return l1, l2
