
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

if __name__ == "__main__":
    list1 = LinkedList();
    list1.head = Node("Keshav");
    second = Node("Aniket")
    first = Node("Nishchal")

    list1.head.next = second
    second.next = first