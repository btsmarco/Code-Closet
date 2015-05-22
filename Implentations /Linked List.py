# Linked Lists
# Marco Botros

class Node:
    def __init__(self,initValue):
        self.value = initValue
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,newValue):
        self.value = newValue

    def setNext(self,nextNode):
        self.next = nextNode

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        result = True if self.head == None else False
        return result

    def add(self, newNodeValue):
        newNode = Node(newNodeValue)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        counter = 0
        node = self.head
        while node != None:
            counter += 1
            node = node.getNext()

        # The for loop is great too but dependent on another method
        # in the class ( __iter__ ) which is not save
        #for node1 in self:
        #    counter += 1

        return counter

    def remove(self,value):
        node = self.head
        prev = None
        while node != None:
            if (node.getValue() == value):
                break
            prev = node
            node = node.getNext()

        if (node != None):
            if (prev == None):
                self.head = None
            else:
                prev.setNext(node.getNext())
            del node

    def search(self,value):
        node = self.head

        while node != None:

            if (node.getValue() == value):
                return True

            node = node.getNext()
        return False



    def __iter__(self):
        node = self.head
        while True:
            yield node.getValue()
            if (node.getNext() == None):
                break
            else:
                node = node.getNext()


linkedList1 = UnorderedList()
print(linkedList1.isEmpty())

linkedList1.add(5)
linkedList1.add(7)
linkedList1.add(3)
linkedList1.add(4)
linkedList1.add(4)
linkedList1.add(9)
linkedList1.add(12)
linkedList1.remove(3)

bulb = linkedList1.search(12)
print("12 is found?",bulb)
bulb = linkedList1.search(11)
print("11 is found?",bulb)

print(linkedList1.isEmpty())
for n in linkedList1:
    print(n)

for n in linkedList1:
    linkedList1.remove(n)

print("after deleting all: ")
print(linkedList1.isEmpty())
