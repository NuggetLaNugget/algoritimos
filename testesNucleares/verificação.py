algo = input('digite algo: ')

print(f'{algo} é numérico? ')
print(algo.isnumeric())

print(f'{algo} é uma string? ')
print(algo.isalpha())

print(f'{algo} é alfanumérico?')
print(algo.isalnum())