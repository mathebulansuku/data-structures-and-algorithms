# quicksort - 


def quick_sort(list):
  if len(list) <=1: #base case 
    return list
  pivot = list[0]
  pivot_less = []
  pivot_plus = []
  
sorted_list = quick_sort(list)
print(sorted_list)
