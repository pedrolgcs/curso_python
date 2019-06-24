data = [[], [], []]
total = three = bigger = 0

for l in range(0, 3):
  for c in range(0, 3):
    data[l].append(int(input(f'Informe um valor para posição [{l}, {c}]: ')))
    # números pares
    if data[l][c] % 2 == 0:
      total += data[l][c]
    # soma da terceira coluna
    if c == 2:
      three += data[l][c]
    # maior valor da segunda linha
    # if l == 1:
    #   if bigger < data[l][c]:
        # bigger = data[l][c]

bigger = max(data[1])

for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{data[l][c]:^5}]', end = '')
  print()
print('=-=' * 10)

print(f'A soma dos números pares é: {total}')
print(f'A soma dos valores da terceira coluna é: {three}')
print(f'O maior número da segunda linha é: {bigger}')
