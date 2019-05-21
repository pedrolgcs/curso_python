name = input('Informe seu nome: ').strip()

print('nome maiúscula: {}'.format(name.upper()))
print('nome minúsculo: {}'.format(name.lower()))
print('quantdiades de caractres: {}'.format(len(name) - name.count(' ')))
first_name = name.split()
print('Seu primeiro nome tem {} letras'.format(len(first_name[0])))
