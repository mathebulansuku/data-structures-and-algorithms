class Node(): 
  """
  An object for storing a single node of a linked list.
  Models two attributes - data and the link to the next node in the list
  """

  data = None
  next_node = None

  def __init__(self, data):
    self.data = data
    

  def __repr__(self):
    return "<Node data: %s>" % self.data
  

class LinkedList():

  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None #This method check if the head Node is empty
  
  def size(self): #Returns the number of nodes in the list. Takes 0(n) linear time
    current = self.head
    count = 0

    while current != None:
      count += 1
      current = current.next_node
    return count
  

  def add (self,data): #This method adds a new node to the head of the list
    new_node = Node(data)
    new_node.next_node = self.head # This node sets the new node added to the list to be the head
    self.head = new_node #This is a O(n) time operation that reassing the head of the list to the new node

  def search(self,key_value): #This method searches through each node in the list until it finds the node == to the key_value
    current = self.head

    while current != None:
      if current.data == key_value:
        return current
      else:
        current = current.next_node
      
    return None
  
  def insert(self, data,index):
    """
    Inserts a new Node containing data at index position
    Insertion takes O(1) time but finding the node at the insertion point 
    takes O(n) time.
    """

    if index == 0:
      self.add(data) # class the add method to insert node at the head of the list

    if index > 0:
      new = Node(data)

      position = index
      current = self.head

    while position > 1:
      current = current.next_node
      position -= 1

    prev_node = current 
    next_node = current.next_node

    prev_node.next_node = new
    new.next_node = next_node

  def remove(self, key):

    """
    Removes Node containing data that matches the key
    Returns the node or None if the key doesn't exist
    Takes O(n) time
    """
    current = self.head #Tail node
    previous = None #This refers to the previous node
    found = False #Key value is still not found

    while current and not found:
      if current.data == key and current == self.head:
        found = True
        self.head = current.next_node
      elif current.data ==key:
        found = True
        previous.next_node = current.next_node
      else:
        previous = current
        current = current.next_node

    return current
  
  def node_at_index(self,index): #Method return node at a given index
    if index == 0:
      return self.head
    else:
      current = self.head
      position = 0

      while position < index:
        current = current.next_node
        position += 1

      return current


        
  def __repr__(self):
    node = []
    current = self.head

    while current != None:
      if current is self.head:
        node.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        node.append("[Tail: %s]" % current.data)
      else:
        node.append("[%s]" % current.data)

      current = current.next_node
    
    return '->'.join(node)
  