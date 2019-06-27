def message(text = 'Mensagem padrão'):
  print('-' * len(text))
  print(text)
  print('-' * len(text))

def soma(*num):
  total = 0
  for n in num:
    total += n
  return print(total)

def duble(lst):
  for i in range(len(lst)):
    lst[i] *= 2
  return print(lst)

message('Funções Python')
message()

soma(10, 11, 20, 10)

duble([10, 20, 30])


