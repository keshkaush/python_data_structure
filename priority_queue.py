class PriorityQueue:

    def __init__(self) -> None:
        self.priority_queue = []
    
    def addElement(self, data):
        self.priority_queue.append(data)
    
    def dispalyQueue(self):
        return ' '.join(self.priority_queue)
    
    def pop(self):
        max = 0
        for i in range(len(self.priority_queue)):
            if self.priority_queue[i] > self.priority_queue[max]:
                max = i
        max_element = self.priority_queue[max]
        del self.priority_queue[max]
        return max_element

if __name__ == "__main__":
    example_queue = PriorityQueue();
    example_queue.addElement(34)
    example_queue.addElement(92)
    example_queue.addElement(1)
    print(example_queue.dispalyQueue)
    print(example_queue.pop())
