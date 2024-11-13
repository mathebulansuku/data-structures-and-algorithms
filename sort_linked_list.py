from linked_list_ds import LinkedList 

def merge_sort(linked_list):
  """
  Sorts a linked list in ascending order
  -Recursively divide the linked list into sublists containing a single node
  -Repeatedly merge the sublists to produce sorted sublists until one remains

  Returns the sorted linked list
  """
  if linked_list.size() == 0 or linked_list.size() == 1:
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

