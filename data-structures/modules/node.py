class Node:
    value = None
    nextNode = None
    previousNode = None
    leftNode = None
    rightNode = None

    def __init__(self, value):
        self.value = value

    def update(self, value):
        self.value = value
        return self

    def setNext(self, nextNode):
        self.nextNode = nextNode
        return self

    def show(self, log=False):
        if log is True:
            print("Node =>", self.value)
        return self.value
