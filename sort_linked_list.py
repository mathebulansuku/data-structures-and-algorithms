from linked_list_ds import LinkedList 

def merge_sort(linked_list):
  """
  Sorts a linked list in ascending order
  -Recursively divide the linked list into sublists containing a single node
  -Repeatedly merge the sublists to produce sorted sublists until one remains

  Returns the sorted linked list
  """
  if linked_list == 1:
    return linked_list
  elif linked_list.head is None:
    return linked_list
  
  left_half,right_half = split(linked_list)

  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left,right)




def split(linked_list):
  
  midpoint = len(linked_list())//2

  left = linked_list[midpoint:]
  right = linked_list[:midpoint]

  return left,right


def merge(left, right):
  
  merged_list = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged_list.append(left[i])
      i += 1
    else:
      merged_list.append(right[j])
      j+= 1

  while i < len(left):
    merged_list.append(left[i])
    i +=1

  while j < len(right):
    merged_list.append(right[j])
    j +=1

  return merged_list

def verify_sorted(linked_list): #This function verifies if the list has been sorted
  n = len(linked_list)

  if n == 0 or n == 1:
    return True
  
  return linked_list[0] < list[1] and verify_sorted(linked_list[1:])

alist = [12,24,43,45,6,67,78,66,56]
l = merge_sort(alist)
print(verify_sorted(alist)) # return False as list is not sorted
print(verify_sorted(l)) #return True as list has been sorted

