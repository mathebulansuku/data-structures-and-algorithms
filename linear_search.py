def linear_search(list, target):
  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None