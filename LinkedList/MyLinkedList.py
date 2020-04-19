from LinkedList.Node import Node


class MyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        index = self.head
        while index is not None:
            print(index.data)
            index = index.next


llist = MyLinkedList()
llist.head == Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third
llist.printList()
