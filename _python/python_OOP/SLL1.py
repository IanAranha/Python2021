# Creating the builing blocks of a Single linked list - aka a Node

# Node constructor
class Node:
	#function to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)



#SingleListConstructor
class LinkedList:

    #Start with a function to initialize a list 
    def __init__(self):
        self.head = None
        self.size = 0

    
    #A Method to print all items in the list.
    def printList(self):
        runner = self.head
        while runner != None:
            print(runner.data)
            runner = runner.next





#Creating some Nodes

node1 = Node(1)
node2 = Node("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
node3 = Node([1,2,3])

print(node1)
print(hex(id(node1)))
print(node2)
print(hex(id(node1)))
print(node3)
print(hex(id(node1)))
print(node1.data)
print(node2.data)
print(node3.data)

#The output should be "NONE" as the nodes are independent objects and are not linked.
print("Printing object.next:")
print("Node objects are not connected. Hence object.next = None")
print(node1.next)
print(node2.next)
print(node3.next)

# #Connecting the nodes to make a Single Linked List
print("Connecting N1.next to N2 and N2.next to N3")
node1.next = node2
node2.next = node3

print("\nNode 1")
print(node1)
print(node1.next)
print(hex(id(node1.next)))

print("\nNode 2")
print(node2.next)
print(hex(id(node2.next)))

print("\nNode 3")
print(node3.next)
print(hex(id(node3.next)))




llist = LinkedList()
print(llist)
print(hex(id(llist)))

#The list has been created but is not connected to anything. Check by printing the head.
print("Link list before connection:")
print(llist.head)

#Connecting the head to first node.

llist.head = node1

print("Link list after connection:")
print(llist.head)

#Connecting the prepared nodes from earlier
node1.next = node2
node2.next = node3

#printing the whole list.
print(llist.head)
print(llist.head.next)
print(llist.head.next.next)
print(llist.head.next.next.next)

# ##Printing all the values
llist.printList()
