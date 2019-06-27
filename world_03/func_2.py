def soma(*nums):
  total = 0
  for n in nums:
    total += n
  return total


print(soma(1, 2, 10, 20))
