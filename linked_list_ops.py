from http.client import LineTooLong
from subprocess import list2cmdline


class Node: #Creating node class
    def __init__(self, data) -> None:
        self.data = data;
        self.next = None;

class LinkedList:# Creating Linked List class whose object will be the Linked List.
    def __init__(self) -> None:
        self.head = None;
    
    def PrintNodes(self): # For printing Nodes
        temp = self.head;
        while(temp): # while temp return None we will keep traversing through the linked list.
            print(f"Data {temp.data} is at {temp.next}")
            temp = temp.next


    def AtBeginning(self, new_element):
        new_Node = Node(new_element)
        new_Node.next = self.head;
        self.head = new_Node;

    
    def AtEnd(self, new_element): # Be sure to check last element points to None
        newNode = Node(new_element)
        #if list is empty:
        if self.head is None:
            self.head = newNode
            return
        temp = self.head;
        while(temp.next):
            temp = temp.next
        temp.next = newNode
    

    def InBetween(self, new_element):
        temp = self.head;
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        temp2 = self.head
        for _ in range(2, count//2 + 1):
            temp2 = temp2.next
        newNode = Node(new_element)
        newNode.next = temp2.next
        temp2.next = newNode

    def SearchNode(self, element):
        temp = self.head;
        count = 0
        while(temp):
            count += 1;
            if( temp.data == element ):
                print(f"Searched data {temp.data} is at {temp.next} on Node {count}");
            temp = temp.next
    

    def RemoveNode(self, the_element):
        HeadNode = self.head;
        if HeadNode is not None:
            if HeadNode.data == the_element:
                self.head = HeadNode.next
                HeadNode = None
                return
        while(HeadNode):
            if(HeadNode.data == the_element):
                break
            prevNode = HeadNode
            HeadNode = HeadNode.next
        
        if(HeadNode):
            return "Item is not there"
        
        prevNode.next = HeadNode.next
        HeadNode = None

if __name__ == "__main__":
    list1 = LinkedList(); # Created list1 object of LinkedList Class.
    list1.head = Node("Keshav"); # Making head node a object of Node class to create a node while passing data.
    second = Node("Aniket")
    first = Node("Nishchal")
    third = Node("Divyanshu")

    list1.head.next = second
    second.next = first
    first.next = third

    list1.AtBeginning("Narayan")
    list1.AtEnd("Me")
    list1.InBetween("minx");
    list1.PrintNodes(); # calling the function PrintNodes P.S don't forget the parenthesis. if you write a function without () it means you are passing it not calling it.
    list1.RemoveNode("Keshav")
    list1.PrintNodes();
    list1.SearchNode("Nishchal")

