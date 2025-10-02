#implementation of stack using lists?

class Stack:

    def __init__(self):
        self.list_stack=[]
        self.top=0
        
    def push(self,data):
        self.list_stack.append(data)
        self.top=self.top+1
        
    def pop(self):
        if len(self.list_stack)==0:
            print("Stack empty")
        else:
            print(self.list_stack[self.top-1])
            self.top=self.top-1
    
    def peek(self):
        print("This is what is on the stack")
        for i in range(self.top-1,-1,-1):
            print(self.list_stack[i])
    
s=Stack()
s.push(3)
s.push(4)
s.push(5)
s.push(123)
s.push(203)
s.push(999)
s.pop()
s.pop()
s.peek()

        
