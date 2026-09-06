class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            newnode = Node(value)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.is_empty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.value

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        if self.is_empty():
            return 0
        iternode = self.head
        while iternode != None:
            iternode = iternode.next
            count += 1
        return count
