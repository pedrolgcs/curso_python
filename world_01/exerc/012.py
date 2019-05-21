name = str(input('Informe seu nome: ')).strip()

print('Mutio prazer {}'.format(name))
print('Primeiro nome: {}'.format(name.split()[0]))
print('Ultima nome: {}'.format(name.split()[len(name.split()) - 1]))