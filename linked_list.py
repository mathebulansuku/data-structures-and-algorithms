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
  

  def add (self,data): #This method adds a new node to the list
    new_node = Node(data)
