from node import Node
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.tail = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def append(self,node=None):
        if node is not None:
            self.tail.next = node
            self.tail = node
            
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    