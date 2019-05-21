a = str(input('Informe uma frase: ')).strip().lower()

print('Ocorrencias da letra A: {}'.format(a.count('a')))
print('Primeira ocorrencia: {}'.format(a.find('a') + 1))
print('Ultima posição: {}'.format(a.rfind('a') + 1))