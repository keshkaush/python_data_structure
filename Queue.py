import queue


class Queue:
     
    def __init__(self) -> None:
        self.queue = []
    
    def addElement(self, data):
        self.queue.append(data)
    
    def peek(self):
        return self.queue[0]
    
    def pop(self):
        if len(self.queue) <= 0:
            return ("Queue is underflow")
        else:
            return self.queue.pop(0)
        
if __name__ == "__main__":
    example_queue = Queue();
    example_queue.addElement("keshav")
    example_queue.addElement("Nishchal")
    print(example_queue.peek())
    example_queue.pop()
    print(example_queue.peek())