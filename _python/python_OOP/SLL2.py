#Creating a Node constructor
#A node is the building block of an SLL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    def __str__(self):
        return str(self.data)


#Creating an SLL constructor
class SLL:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def traverse(self):
        if self.head == None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next
    
    def append(self, data):
        #Create a new node
        newNode = Node(data)

        #if there is no node in the SLL, simply point "Head" to newNode
        if self.head == None:
            self.head = newNode
            self.size+=1
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = newNode
            self.size+=1

    def insert_at_head(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.size+=1
        else:
            newNode.next = self.head
            self.head = newNode
            self.size+=1

    def insert_after(self, x, data):
        n = self.head
        print(n.next)
        while n != None:
            print("N.Data:", n.data)
            print("N.next:", n.next)
            if n.data == x:
                print("Breaking here!!")
                break
            n = n.next
        if n == None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
            self.size+=1
    
    def insert_before(self, x, data):
        if self.head == None:
            print("List has no element")

        if x == self.head.data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        print(n.next)
        while n.next != None:
            if n.next.data == x:
                break
            n = n.next
        if n.next == None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


    def insert_at_index (self, index, data):
            if index == 1:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            i = 1
            n = self.head
            while i < index-1 and n != None:
                n = n.next
                i = i+1
            if n == None:
                print("Index out of bound")
            else: 
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node

    def get_count(self):
        if self.head is None:
            return 0;
        n = self.head
        count = 0;
        while n is not None:
            count = count + 1
            n = n.next
        return count


    def search_item(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.next
        print("item not found")
        return False

    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return 
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def delete_element_by_value(self, x):
        if self.head is None:
            print("The list has no element to delete")
            return

        # Deleting first node 
        if self.head.item == x:
            self.head = self.head.next
            return

        n = self.head
        while n.next is not None:
            if n.next.item == x:
                break
            n = n.next

        if n.next is None:
            print("item not found in the list")
        else:
            n.next = n.next.next

    def reverse_linkedlist(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev











list = SLL()
print(list)
print(hex(id(list)))
print(list.head)
print(list.size)
list.append("Ian")
print(list.size)
list.append("Mario")
list.append("Lizard")
list.append("Cake")
list.append(32)
print(list.size)
list.traverse()
list.insert_at_head("Andrew")
print(list.size)
list.traverse()
list.insert_after("Mario", 19)
list.traverse()
print(list.size)
list.insert_after("Gerald", 33)


