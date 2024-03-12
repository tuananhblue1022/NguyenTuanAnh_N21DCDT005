class Node:
  def __init__(self, data):
      self.data = data
      self.next = None


class LinkedList:
  def __init__(self, value):
      self.head = Node(value)
      self.tail = self.head
      self.length = 1

  def append(self, value):
      new_node = Node(value)
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1

  def prepend(self, value):
      new_node = Node(value)
      new_node.next = self.head
      self.head = new_node
      self.length += 1

  def insert(self, index, value):
      if index < 0 or index > self.length:
          raise IndexError("Index out of bounds")

      if index == 0:
          self.prepend(value)
      elif index == self.length:
          self.append(value)
      else:
          new_node = Node(value)
          current_node = self.head
          for _ in range(index - 1):
              current_node = current_node.next
          new_node.next = current_node.next
          current_node.next = new_node
          self.length += 1

  def remove(self, index):
      if index < 0 or index >= self.length:
          raise IndexError("Index out of bounds")

      if index == 0:
          self.head = self.head.next
      elif index == self.length - 1:
          self.tail = self.tail.next
      else:
          current_node = self.head
          for _ in range(index - 1):
              current_node = current_node.next
          current_node.next = current_node.next.next
          self.length -= 1

  def __getitem__(self, index):
      if index < 0 or index >= self.length:
          raise IndexError("Index out of bounds")

      current_node = self.head
      for _ in range(index):
          current_node = current_node.next
      return current_node.data

  def __setitem__(self, index, value):
      if index < 0 or index >= self.length:
          raise IndexError("Index out of bounds")

      current_node = self.head
      for _ in range(index):
          current_node = current_node.next
      current_node.data = value

  def __len__(self):
      return self.length

  def __str__(self):
      values = []
      current_node = self.head
      while current_node is not None:
          values.append(current_node.data)
          current_node = current_node.next
      return " ".join(str(x) for x in values)


# Ví dụ sử dụng

my_list = LinkedList(10)
my_list.append(20)
my_list.append(30)
my_list.prepend(5)
my_list.insert(2, 15)

print(my_list)  # In ra: 5 10 15 20 30

print(my_list[2])  # In ra: 15

my_list[2] = 25

print(my_list)  # In ra: 5 10 25 20 30

my_list.remove(2)

print(my_list)  # In ra: 5 10 20 30

print(len(my_list))  # In ra: 4
