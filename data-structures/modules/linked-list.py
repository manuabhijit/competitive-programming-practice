from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value, currentNode=None):
        if self.head is None:
            self.head = Node(value)
            return self
        elif currentNode is None:
            currentNode = self.head

        if currentNode.nextNode is None:
            currentNode.nextNode = Node(value)
        else:
            self.insert(value, currentNode.nextNode)
        return self

    def printList(self, currentNode=None):
        if self.head is None:
            print("No nodes in the list")
            return self
        elif currentNode is None:
            currentNode = self.head

        print("Node(", currentNode.value, ")", end="")

        if currentNode.nextNode is not None:
            print(" -> ", end="")
            self.printList(currentNode.nextNode)
        else:
            print("")
        return self


LinkedList().insert(1).insert(2).insert(3).insert(4).printList()
