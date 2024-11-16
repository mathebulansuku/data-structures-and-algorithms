# quicksort - 


def quick_sort(list):
  if len(list) <=1: #base case 
    return list
  pivot = list[0]
  pivot_less = []
  pivot_plus = []

  for item in list[1:]: #We loop through every item in list excluding the pivot value list[0]
    if item <= pivot: #This adds items to the specific lists(pivot_less and pivot_plus)
      pivot_less.append(item) 
    else:
      pivot_plus.append(item)

  
sorted_list = quick_sort(list)
print(sorted_list)
