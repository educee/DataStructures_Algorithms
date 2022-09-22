class SinglyLinkedList():
    
    class _Node():
        
        def __init__(self, element):
            self.element = element
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addNode(self, element):
        newNode = self._Node(element)
        
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
            
    def getSize(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def deleteNodeByReference(self, node):  #Validate wrt ref count and accessing node with address
        
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return
        
        curNode = self.head
        PrevNode = None
        while curNode is not None:
            if curNode == node:
                if curNode == self.head:
                    self.head = self.head.next
                    self.size -= 1
                    break
                elif curNode == self.tail:
                    prevNode.next = None
                    self.size -= 1
                    break
                else:
                    prevNode.next = curNode.next
                    self.size -= 1
                    break
                    
                prevNode = curNode
                curNode = curNode.next
