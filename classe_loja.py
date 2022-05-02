import funcoes

class Loja:
    def __init__(self, nome, bikes):
        self.nome = nome
        self.bikes = bikes

    def mostrar_saldo_bikes(self):
        print(f'O total de Bikes disponíveis: {self.bikes}')
    
    def atualiza_saldo(self):
        operacao = int(input('Informe o tipo de operação, sendo: \nS para realizar locação de bike \nE para o recebeimento de bike \n:'))
        while operacao != 'S' or operacao != 'E':
            if operacao == 'S':
                aux = int(input('Informe a quantidade de Bikes que deseja alugar: '))
                if self.bikes >= aux:
                    print('OK, total disponível para a locação')
                    self.bikes -= aux
                else:
                    print(f'Infelizmente o saldo de Bikes disponével é de: {self.bikes}')
            elif operacao == 'E':
                aux = int(input('Informe a quantidade de Bikes que vais devolver: '))
                self.bikes += aux
            else:
                print('Opção errada')
                
            operacao = int(input('Informe o tipo de operação, sendo: \nS para realizar locação de bike \nE para o recebeimento de bike \n:')) 
        return self.bikes

    def valor_receber(self):
        funcoes.calc_periodo_locado
        tipo_locacao = input(f'Informe o tipo de locação: \nH para Hora \nD para dia \nS para semana \n: ')
        aux = int(input('Informe o total de Bikes locadas: '))
        if tipo_locacao == 'H':
            if aux >= 3:
                valor = (funcoes.tempo_em_hora * 5) * 0,7
                print(f'O valor a pagar pela locação é de: R${valor:.2f}')
            else:
                valor = funcoes.tempo_em_hora * 5
                print(f'O valor a pagar pela locação é de: R${valor:.2f}')
        elif tipo_locacao == 'D':
            if aux >= 3:
                valor = (funcoes.tempo_em_dias * 25) * 0,7
                print(f'O valor a pagar pela locação é de: R${valor:.2f}')
            else:
                valor = funcoes.tempo_em_dias * 25
                print(f'O valor a pagar pela locação é de: R${valor:.2f}')
         
        else:
            if aux >= 3:
                valor = (funcoes.tempo_em_semanas * 100) * 0,7
                print(f'O valor a pagar pela locação é de: R${valor:.2f}')
            else:
                valor = funcoes.tempo_em_semanas * 100
                print(f'O valor a pagar pela locação é de: R${valor:.2f}')

    




    
