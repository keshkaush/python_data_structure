class Stack:

    def __init__(self) -> None:
        self.stack = []
    
    def addElementAtTop(self, element):
        self.stack.append(element)
    
    def peek(self):
        return self.stack[-1]

    def PopTopElement(self):
        if len(self.stack) == 0:
            return ("stack is undervalued")
        else:
            return self.stack.pop()
    

if __name__ == "__main__":
    example_stack = Stack();
    example_stack.addElementAtTop("keshav")
    example_stack.addElementAtTop("Nishchal")
    print(example_stack.peek())
    example_stack.PopTopElement()
    print(example_stack.peek())