class Node:

  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = self.head
    self.length = 1

  def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
    if self.length == 0:
      self.tail = new_node
    self.length += 1
    
  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

linked_list = LinkedList("Nguyễn Tuấn Anh")
linked_list.append("N21DCDT005")
print(linked_list.head.value)  
print(linked_list.tail.value)  
print(linked_list.length)  