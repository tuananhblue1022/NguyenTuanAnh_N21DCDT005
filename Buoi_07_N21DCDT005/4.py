class Queue:
  def __init__(self):
    self.items = []

  def __str__(self):
    values = [str(x) for x in self.items]
    return ', '.join(values)  # Join elements with commas for better output

  def isEmpty(self):
    return self.items == []  # More concise way to check emptiness

  def enqueue(self, value):
    self.items.append(value)
    return "Element inserted at the end of queue"  # Consistent capitalization

  def peek(self):
    if self.isEmpty():
      return "The queue is empty"  # Clearer message
    else:
      return self.items[0]

  def dequeue(self):  # Renamed for clarity (standard queue operation)
    if self.isEmpty():
      return "The queue is empty"  # Consistent error handling
    else:
      return self.items.pop(0)  # Remove and return the first element

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)

print(customQueue.peek())  # Output: 1
print(customQueue.dequeue())  # Output: 1
print(customQueue.peek())  # Output: 2
