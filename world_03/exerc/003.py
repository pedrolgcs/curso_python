from random import randint, sample

# l = tuple(sample(range(10), 5))

sort = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: { sort }')
print(f'O maior valor foi: { max(sort) }')
print(f'O menor valor foi: { min(sort) }')