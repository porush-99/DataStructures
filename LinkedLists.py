class node():

    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList():

    def __init__(self, data):
        newNode = node(data)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, data):
        newNode = node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, data):
        newNode = node(data)
        newNode.next = self.head
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
            temp.next = newNode
        self.length += 1

    def removeData(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif index + 1 > self.length:
            print("Index out of range")
        else:
            temp = self.head
            for i in range(1, index):
                temp = temp.next
            delNode = temp.next
            temp.next = delNode.next
            if index + 1 == self.length:
                self.tail = temp
            self.length -= 1

    def printList(self):
        temp = self.head
        while temp.next != None:
            print(temp.val, '--> ', end='')
            temp = temp.next
        print(temp.val)

    def reverseList(self):
        if self.head.next == None:
            pass
        else:
            first = self.head
            self.tail = first
            second = first.next
            while second:
                temp = second.next
                second.next = first
                first = second
                second = temp
            self.head.next = None
            self.head = first

    # def reverseList(self):
    #     if self.head.next == None:
    #       pass
    #     else:
    #       while self.head.next != None:
    #           temp = self.head
    #           while True:
    #               if temp.next.next == None:
    #                   temp.next.next = temp
    #                   temp.next = None
    #                   break
    #               temp = temp.next
    #       temp = self.head
    #       self.head = self.tail
    #       self.tail = temp


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

l.removeData(5)
l.printList()

l.reverseList()
l.printList()

print(l.length)
