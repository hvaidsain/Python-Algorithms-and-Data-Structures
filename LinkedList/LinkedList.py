class Node:
    def __init__(self,data):
        #declare object variable or instance variables
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def printList(self):
        if(self.head == None):
            print("List Empty")
            return
        else:
            current = self.head
            while(current != None):
                print(current.data,end=" -> ")
                current = current.next
            print("\r")

        


    def insertInList(self,data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            print("Inserted {} successfully ".format(data))
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = node
            print("Inserted {} successfully ".format(data))

    def insertAtFront(self,data):
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.printList()

    def removeFromFront(self):
        if(self.head == None):
            print("List is empty")
            return
        else:
            current = self.head
            self.head = self.head.next
            current.next = None

            print("{} removed successfully".format(current.data))
            self.printList()

    def removeFromLast(self):
        if(self.head == None):
            self.printList()
        elif(self.head.next == None):
            self.head = None
        else:
            prev = self.head
            ahead = self.head.next
            while(ahead.next!=None):
                ahead = ahead.next
                prev = prev.next

            prev.next = None

        self.printList()





if __name__ == "__main__":
    l1 = LinkedList()
    l1.insertInList(2)
    l1.insertInList(4)
    l1.insertInList(6)
    l1.insertInList(8)
    l1.insertInList(12)
    l1.insertAtFront(20)
    l1.insertAtFront(24)
    l1.removeFromFront()
    l1.removeFromLast()
    l1.removeFromLast()
    l1.removeFromLast()






    

        