def bigger(*nums):
  big = 0
  print('Analisando os valores passados...')
  for n in nums:
    if n > big:
      big = n
    print(n, end = ' ')
  print(f'-> Foram informados {len(nums)} valores ao todo')
  print(f'O maior valor informado foi {big}')
  print('-' * 30)

bigger(10, 2, 3)
bigger(10, 2, 33, 4, 4)
bigger()
