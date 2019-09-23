class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

# 3 -> 2 -> 1
  def reverse_list(self):
    if self.head == None:
      return
    prev_node = None
    curr_node = self.head # 3
    while curr_node.next_node:
      next_node = curr_node.next_node # 2 -> 1 : 1 -> None
      curr_node.next_node = prev_node # 3 -> None : 2 -> 3
      prev_node = curr_node # 3 -> None : 2 -> 3
      curr_node = next_node # 2 -> 1 : 1 -> None
    curr_node.next_node = prev_node # 1 -> 2
    self.head = curr_node # 1 -> 2

if __name__ == '__main__':
  list = LinkedList()
  list.add_to_head(1)
  list.reverse_list()
