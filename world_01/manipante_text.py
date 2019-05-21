frase = 'Curso em video Python'
name = '   Pedro Henrique Lopes  '

print(len(frase))
print(frase[9::3]) # pulando de 3 em 3
print(frase.count('o')) # procura ocorrencia da letra 'o'
print(frase.count('o', 0, 13)) # com fatiamento
print(frase.find('deo')) # encontra a ocorrencia e existe a posição incial
print(frase.replace('Python', 'Android'))
frase = frase.split() # divide uma string em uma lista
print('-'.join(frase)) # junta todos os elementos

print(name.strip()) # remover espaços no começo e no fim

