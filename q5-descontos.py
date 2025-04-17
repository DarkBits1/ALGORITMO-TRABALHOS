def desconto_normal(valor):
    if valor > 500:
        return valor * 0.85
    elif valor >= 200:
        return valor * 0.90
    elif valor >= 100:
        return valor * 0.95
    else:
        return valor  


def aniversario():
    resposta = input('Você completa aniversário hoje? (sim ou nao): ').strip().lower()
    if resposta == 'sim':
        return 0.97 
    elif resposta == 'nao':
        return 1 
    else:
        print('INSIRA UMA RESPOSTA VÁLIDA.')
        return aniversario()


def vip():
    resposta = input('Você é VIP? (sim ou nao): ').strip().lower()
    if resposta == 'sim':
        return 0.95
    elif resposta == 'nao':
        return 1
    else:
        print('INSIRA UMA RESPOSTA VÁLIDA.')
        return vip()


def desconto_final():
    valor = float(input('Insira o valor do produto: R$ '))
    valor_com_desconto = desconto_normal(valor)
    fator_vip = vip()
    fator_niver = aniversario()
    valor_final = valor_com_desconto * fator_vip * fator_niver
    print(f'VOCÊ IRÁ PAGAR: R$ {valor_final:.2f}')



desconto_final()
