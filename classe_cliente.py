from classe_loja import Loja


class Cliente(Loja):

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saldo_bikes(self):
        saldo = Loja
        print(f'O saldo de Bikes disponível é: {saldo.mostrar_saldo_bikes}')

    def opcao_de_locacao(self):
        print('Você pode: \nAlugar bicicletas por hora (R$5/hora); \nAlugar bicicletas por dia (R$25/dia); \nAlugar bicicletas por semana (R$100/semana)')
        print('Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquer tipo), \ncom 30 por cento de desconto no valor total.')
        tipo_locacao = input('Digite H para Hora, \nD para dia, \nS para semana')

        while tipo_locacao != 'H' or tipo_locacao != 'D' or tipo_locacao != 'S':
            print('Opção errada')
            tipo_locacao = input('Digite H para Hora, \nD para dia, \nS para semana')

        aux = int(input('Informe a quantidade de Bikes que irá alugar: '))

        return (aux, tipo_locacao)
        




    