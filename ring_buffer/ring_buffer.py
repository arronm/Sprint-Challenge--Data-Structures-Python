class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity


  def append(self, item):
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1
      return
    
    # current % capacity to replace
    self.storage[self.current % self.capacity] = item
    self.current += 1


  def get(self):
    return [i for i in self.storage if i is not None]


if __name__ == '__main__':
  buffer = RingBuffer(5)
  buffer.append('a')
  buffer.append('b')
  buffer.append('c')
  buffer.append('d')
  print(buffer.storage, buffer.get() == ['a', 'b', 'c', 'd'])