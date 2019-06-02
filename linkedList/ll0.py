class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None



def printLL(head):
    if head != None:
        print(head.data)
        printLL(head.next)



def printRev(head):
    if head != None:
        printRev(head.next)
        print(head.data)


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
printLL(head)
printRev(head)
