class MinStack:
    def __init__(self):
        self.stack = []  
        self.min_stack = [] 

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


stack = MinStack()
stack.push(5)
print("Min:", stack.min()) 
stack.push(6)
print("Min:", stack.min())  
stack.push(3)
print("Min:", stack.min())  
stack.push(7)
print("Min:", stack.min())  
stack.pop()
print("Min:", stack.min())  
stack.pop()
print("Min:", stack.min())  
