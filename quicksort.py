# quicksort - A highly efficient and widely used sorting algorithm that works by partitioning a list into smaller sublists, sorting them independently, and combining the results.

# Big O of quicksort is: best case = O(n log n) and worst case = O(n^2)


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
  return quick_sort(pivot_less) + [pivot] + quick_sort(pivot_plus)

  

alist = [12,45,6,7,8,99,3,2,4,335,655,7]
sorted_list = quick_sort(alist)
print(sorted_list)
