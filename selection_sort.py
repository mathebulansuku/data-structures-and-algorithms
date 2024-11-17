# Selection sort is a data algorithm that passes in an unsorted list.
# It then assigns an initial value. traverses the unsorted list while comparing it to the initial value, while assigning a new value if it is less than the previous value
#After completing the list, it then appends the lowest value to the empty sorted list.
# It loops until all the values are moved from the unsorted to the sorted list.

#Big O of selection sort is O(n^2)

def selection_sort(unsorted_list):
  sorted_list = []
  print("%25s %-25s" % (unsorted_list,sorted_list))

  for i in range(0, len(unsorted_list)):
    index_to_move = index_of_min(unsorted_list)
    sorted_list.append(unsorted_list.pop(index_to_move))
    print("%-25s %-25s" % (unsorted_list, sorted_list))
  return sorted_list

def index_of_min(unsorted_list):
  min_index = 0

  for i in range(0, len(unsorted_list)):
    if unsorted_list[i] < unsorted_list[min_index]:
      min_index = i
  return min_index
  
alist = [10,2,3,5,6,76,4,3,12]

print(selection_sort(alist))