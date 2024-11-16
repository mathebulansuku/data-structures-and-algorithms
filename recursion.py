# Recursion is the ability of a function to call itself

def sum(numbers):
  if not numbers:
    return 0
  remaining_sum = sum(numbers[1:])
  return numbers[0] + remaining_sum

print(sum([1,2,7,9]))