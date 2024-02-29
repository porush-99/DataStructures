class node():

    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None


class LinkedList():

    def __init__(self, data):
        newNode = node(data)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, data):
        newNode = node(data)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length += 1

    def prepend(self, data):
        newNode = node(data)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def insertData(self, index, data):
        if index == 0:
            self.prepend(data)
        elif index > self.length:
            self.append(data)
        else:
            newNode = node(data)
            temp = self.head
            for i in range(1, index):
                temp = temp.next

            newNode.next = temp.next
            temp.next.prev = newNode
            temp.next = newNode
            newNode.prev = temp
        self.length += 1

    def removeData(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        elif index + 1 > self.length:
            print("Index out of range")
        else:
            temp = self.head
            for i in range(1, index):
                temp = temp.next
            delNode = temp.next
            temp.next = delNode.next
            delNode.next.prev = temp
            if index + 1 == self.length:
                self.tail = temp
            self.length -= 1

    def printList(self):
        temp = self.head
        while temp.next != None:
            print(temp.val, '--> ', end='')
            temp = temp.next
        print(temp.val)

        # print("Reverse order")
        # temp = self.tail
        # while temp.prev != None:
        #     print(temp.val, '<-- ', end='')
        #     temp = temp.prev
        # print(temp.val)
        # print("---------------")


l = LinkedList(1)
l.printList()

l.append(10)
l.printList()

l.append(5)
l.printList()

l.append(6)
l.printList()

l.prepend(2)
l.printList()

l.insertData(1, 4)
l.printList()

l.removeData(4)
l.printList()

print(l.length)
