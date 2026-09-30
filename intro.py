class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def add_last(self,data):
        NewNode = Node(data)
        
        if self.head is None:
            self.head = NewNode
            return
        
        curr = self.head
        

        while curr.next:
            curr = curr.next
        curr.next = NewNode
    def add_at_begining(self,data):
        NewNode = Node(data)
        
        if self.head is None:
            self.head = NewNode
            return
        
        NewNode.next = self.head
        self.head = NewNode

    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end=" -> ")
            self.size += 1
            curr = curr.next
        print("None")
ll = LinkedList()
ll.add_last(20)
ll.add_last(30)
ll.add_last(40)
ll.add_at_begining(10)
ll.display()
print(len(ll))
        
        