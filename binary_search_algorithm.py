#Binary search is a searching algorithm used to find an item from a sorted list of items. 
#It works by first comparing the middle value of the list, and comparing it to the target value.
#If that is False, it continues by checking if the value is less or greater than the middle value.
#If the middle value is less, it works with the right half of the list by starting again at the middle value of the right list, continuing the pattern until it finds the value and then returns the index of that value.

def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    midpoint = (first + last) // 2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None

def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")
  

numbers = [1,2,3,4,5,6,7,8,9,10] 

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)