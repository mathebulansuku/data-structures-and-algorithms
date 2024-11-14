from linked_list_ds import LinkedList 

def merge_sort(linked_list):
  """
  Sorts a linked list in ascending order
  -Recursively divide the linked list into sublists containing a single node
  -Repeatedly merge the sublists to produce sorted sublists until one remains

  Returns the sorted linked list

  Runs on O(kn log n)
  """
  if linked_list.size() == 1:
    return linked_list
  elif linked_list.head is None:
    return linked_list
  
  left_half,right_half = split(linked_list) # This splits the linked_list in left and right

  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left,right)




def split(linked_list):

  """
  Divide the unsorted list at midpoint into sublists
  Takes O(k log n) time
  """
  
  if linked_list == None or linked_list.head == None:
    left = linked_list
    right = None

    return left, right
  else:
    size = linked_list.size()
    midpoint = size//2

    mid_node = linked_list.node_at_index(midpoint - 1)

    left_half = linked_list
    right_half = LinkedList()
    right_half.head = mid_node.next_node
    mid_node.next_node = None

    return left_half, right_half

def merge(left, right):
    """
    The function merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    Runs in O(n) time
    """
    # Create a new linked list that contains nodes from left and right lists
    merged_list = LinkedList()

    # Add a fake head that is discarded later
    merged_list.add(0)

    # Set current to the head of the linked list
    current = merged_list.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head 

    # Iterate over the left and right lists until we reach the tail node
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            break  # Exit loop since remaining nodes are from right list
        elif right_head is None:
            current.next_node = left_head
            break  # Exit loop since remaining nodes are from left list
        else:
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        
        current = current.next_node  # Advance the current pointer

    # Discard fake head and set first merged node as head
    merged_list.head = merged_list.head.next_node

    return merged_list

#Test code 

l = LinkedList()
l.add(12)
l.add(32)
l.add(43)
l.add(45)
l.add(76)
l.add(36)

print("unsorted linked list:", l)
sorted_linked_list = merge_sort(l)
print("Sorted linked list:", sorted_linked_list)