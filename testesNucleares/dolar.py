import sys

print('eita bixo! parece que temos uma boa grana aqui, que tal nós por motivo nem um comprarmos dólar?\n')

print('seguinte, eu vou te dar o quanto c pedir, use com sabedoria\n')

dinheiro = float(input('digite seu valor: '))

troca = dinheiro//3,27

troco = dinheiro%3,27

print(f'\nsaldo = {dinheiro}')

print('iai? bó comprar dinheirin?\n')

print('1 - sim')
print('2 - não\n')

escolha = input('faça sua escolha: ')

if escolha == '1' or escolha == 'sim':
    print('\nbeleza então, se liga: US$1,00 = R$3,27\n\npresta atenção nisso aí eim!')

    print(f'dá pra você comprar {troca}, vai comprar mesmo?\n')
    print('1 - sim')
    print('2 - não\n')
    escolha2 = input('digite sua opção: ')
    if escolha2 == '1' or escolha2 == 'sim':
        print('\nCompra realizada com sucesso!')
        print(f'\nAgora você tem US${troca}, aqui está seu troco!')
        print(f'\n**Você recebeu {troco} de troco!**')
    elif escolha2 == '2' or escolha2 == 'não':
        print('tá bão então._.')
        sys.exit()
elif escolha == '2' or escolha == 'não':
    print('\noxe, tão tá bão\n')
    print('metendo o pé...\n')
    sys.exit()