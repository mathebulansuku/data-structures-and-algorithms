# Recursion is the ability of a function to call itself

def sum(numbers):
  total = 0

  for number in numbers:
    total += number # total = total + number
  return total


print(sum([1,2,7,9]))