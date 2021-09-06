#minha idéia é criar uma simulação de caixa de super-mercado
#ela deve perguntar o valor de um produto e trazer 5% de desconto
#sabendo que para calcular porcentagem é necessário dividir nesse caso, vamos lá.

import sys
class loja:
    def __init__(self, produtos):
        self.produtos = type(produtos)
    def wellcome():
        print('Olá seja bem-vindo(a) ao super-mercado, oque você gostaria de fazer? \n')
        print('1 - produtos ')
        print('2 - preços ')
        print('3 - pagar ')
        print('4 - sair\n')
        opcao = input('Digite sua escolha: ')
        op = opcao
        if op == 1 or op == '1':
            produto = input('\nDigite qual o produto desejado!')
            print(f'Seu produto desejado é: {produto}, deseja muda-lo?\n')
            print('1 - sim')
            print('2 - não\n')
            opcao2 = input('digite sua resposta: ')
            if opcao2 == 1 or opcao2 == '1' or opcao2 == 'sim':
                return produto
            elif opcao2 == 2 or opcao2 == '2' or opcao2 == 'nao' or opcao2 == 'não':
                return opcao