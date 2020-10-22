from linkedlist import LinkedList
from node import Node

def main():
    llist = LinkedList()
    first_node = Node("a")
    llist.head = first_node
    print(repr(llist))

if __name__ == "__main__":
    main()