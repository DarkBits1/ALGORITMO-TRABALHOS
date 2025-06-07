
def main():
    divida = float(input('Valor inicial da dívida > '))
    taxa = float(input('Taxa de juros mensal (%) > '))
    meses = int(input('Quantos meses? > '))

    taxa /= 100  

    for mes in range(1, meses + 1):
        divida *= (1 + taxa) 
        pagamento = float(input(f'Pagamento no mês {mes} > '))
        divida -= pagamento

        if divida <= 0:
            print(f'Dívida quitada no mês {mes}. Saldo final: R$0,00')
            return
        else:
            print(f'Saldo da dívida após o mês {mes}: R${divida:.2f}')

    print(f'\nDívida não foi quitada. Saldo restante após {meses} meses: R${divida:.2f}')


main()
