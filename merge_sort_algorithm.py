# Merge sort is a sorting algorithm that splits the list into smalleer sublists, sort them, and then merges them back togetheer to form the sorted list. It has a time complexity of O(nlog n).

def merge_sort(list):
  
  """
  STEPS:

  1. Divide: Find the midpoint of the list and divide into sublists
  2. Conquer: Recursively sort the sublists created in previous
  3. Combine: Merge the sorted sublists created in previous step
  """

  if len(list) <= 1:
    return list
  
  left_half, right_half = split(list) #Divide
  left  = merge_sort(left_half) #conquer
  right = merge_sort(right_half)#conquer

  return merge(left,right)

def split(list): #This function divides the unsorted list at midpoint into sublists

  midpoint = len(list)//2
  left = list[:midpoint]
  right = list[midpoint:]

  return left, right 

def merge(left, right): #Function merges 2 lists, sorting them in the process, and returns a new merged list
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]: # This compares the values of the sublists and appends the lesser value to the merge list
        l.append(left[i])
        i += 1 # Increment the value on the left list
      else:
        l.append(right[j])
        j += 1

    while i < len(left):
        l.append(left[i])
        i +=1
      
    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list): #This function verifies if the list has been sorted
  n = len(list)

  if n == 0 or n == 1:
    return True
  
  return list[0] < list[1] and verify_sorted(list[1:])

alist = [12,24,43,45,6,67,78,66,56]
l = merge_sort(alist)
print(verify_sorted(alist)) # return False as list is not sorted
print(verify_sorted(l)) #return True as list has been sorted