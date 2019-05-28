total = 0
count_number = 0
for i in range(1, 501, 2):
  if i % 3 == 0:
    count_number += 1
    total += i

print('A soma dos {} valores solicitados é: {}'.format(count_number, total))