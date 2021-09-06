nota1 = float(input('diga sua primeira nota: '))
nota2 = float(input('diga sua segunda nota: '))

soma = nota1 + nota2

media = soma/2

print(f'Sua média foi de {media:.2f}')

if media >= 6:
    print('Você passou!')
else:
    print('Você não passou!')