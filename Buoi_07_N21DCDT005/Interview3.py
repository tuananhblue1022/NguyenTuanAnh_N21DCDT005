class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_full(self):
        return len(self.items) == self.capacity

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

class SetOfStacks:
    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks = []

    def push(self, item):
        if len(self.stacks) == 0 or self.stacks[-1].is_full():
            new_stack = Stack(self.stack_capacity)
            new_stack.push(item)
            self.stacks.append(new_stack)
        else:
            self.stacks[-1].push(item)

    def pop(self):
        if len(self.stacks) == 0:
            raise Exception("SetOfStacks is empty")
        item = self.stacks[-1].pop()
        if len(self.stacks[-1].items) == 0:
            self.stacks.pop()
        return item

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            raise IndexError("Invalid stack index")

        item = self.stacks[index].pop()

        # Shift items from next stacks to fill the gap
        for i in range(index, len(self.stacks) - 1):
            self.stacks[i].push(self.stacks[i + 1].items[0])
            self.stacks[i + 1].items.pop(0)

        # If the last stack is empty, remove it
        if len(self.stacks[-1].items) == 0:
            self.stacks.pop()

        return item

# Example usage:
set_of_stacks = SetOfStacks(3)
set_of_stacks.push(1)
set_of_stacks.push(2)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(5)
set_of_stacks.push(6)
print(set_of_stacks.popAt(0))  # Output: 3
print(set_of_stacks.popAt(1))  # Output: 6
print(set_of_stacks.pop())    # Output: 5
