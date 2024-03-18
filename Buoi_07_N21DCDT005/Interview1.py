class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack_list = [None] * (3 * stack_size)
        self.pointers = [0, stack_size, 2 * stack_size]

    def push(self, stack_num, value):
        if self.pointers[stack_num] < (stack_num + 1) * self.stack_size:
            self.stack_list[self.pointers[stack_num]] = value
            self.pointers[stack_num] += 1
        else:
            print(f"Stack {stack_num+1} is full. Cannot push more elements.")

    def pop(self, stack_num):
        if self.pointers[stack_num] > stack_num * self.stack_size:
            self.pointers[stack_num] -= 1
            value = self.stack_list[self.pointers[stack_num]]
            self.stack_list[self.pointers[stack_num]] = None
            return value
        else:
            print(f"Stack {stack_num+1} is empty. Cannot pop from an empty stack.")
            return None

    def peek(self, stack_num):
        if self.pointers[stack_num] > stack_num * self.stack_size:
            return self.stack_list[self.pointers[stack_num] - 1]
        else:
            print(f"Stack {stack_num+1} is empty. Cannot peek from an empty stack.")
            return None

# Example usage:
stacks = ThreeStacks(3)

stacks.push(0, 10)
stacks.push(0, 20)
stacks.push(0, 30)
stacks.push(1, 40)
stacks.push(1, 50)
stacks.push(1, 60)
stacks.push(2, 70)
stacks.push(2, 80)
stacks.push(2, 90)

print(stacks.stack_list)  
print(stacks.peek(0)) 
print(stacks.peek(1))  
print(stacks.peek(2))  

print(stacks.pop(0))  
print(stacks.pop(1))  
print(stacks.pop(2))  

print(stacks.stack_list)  

