# quicksort - 


def quick_sort(list):
  if len(list) <=1: #base case 
    return list
  
sorted_list = quick_sort(list)
print(sorted_list)
