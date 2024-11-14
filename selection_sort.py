# Selection sort

def selection_sort(list):
  sorted_list = []

  for i in range(0, len(list)):
    index_to_move = index_of_min(list)
    sorted_list.append(list.pop(index_to_move))
  return sorted_list

def index_of_min(list):
  min_index = 0

  for i in range(0, len(list)):
    if list[i] < list[min_index]:
      min_index = i
  return min_index
  
alist = [10,2,3,5,6,76,4,3,12]

print(selection_sort(alist))