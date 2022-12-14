class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def remove_duplicates(self):
        present = self.head
        while present != None:
            to_check = present.next
            previous = present

            while to_check != None:
                if present.data == to_check.data:
                    if to_check.next == None:
                        previous.next = None
                    else:
                        previous.next = to_check.next
                    to_check = previous.next
                else:
                    previous = to_check
                    to_check = to_check.next

            present = present.next

    def printList(self):
        temp = self.head

        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Driver code
# list = LinkedList()
# list.head = Node(10)
# list.head.next = Node(12)
# list.head.next.next = Node(11)
# list.head.next.next.next = Node(11)
# list.head.next.next.next.next = Node(12)
# list.head.next.next.next.next.next = Node(11)
# list.head.next.next.next.next.next.next = Node(10)

list = LinkedList()
list.head = Node(3)
list.head.next = Node(4)
list.head.next.next = Node(3)
list.head.next.next.next = Node(2)
list.head.next.next.next.next = Node(6)
list.head.next.next.next.next.next = Node(1)
list.head.next.next.next.next.next.next = Node(2)
list.head.next.next.next.next.next.next.next = Node(6)
list.printList()
list.remove_duplicates()
list.printList()
