def calcular_fatura(valor_fatura, pagamento, meses_sem_pagar):
    juros_rotativo = 0.12  
    multa_atraso = 0.02  
    juros_mora = 0.01  
    
    saldo_devedor = valor_fatura - pagamento
    if pagamento < valor_fatura * 0.15:  # 15% = valor mínimo
        print('Pagamento é menor que o valor mínimo. Seu cartão foi bloqueado.')
    
    saldo_devedor *= (1 + multa_atraso) * ((1 + juros_rotativo + juros_mora) ** meses_sem_pagar)
    
    crescimento = ((saldo_devedor - (valor_fatura - pagamento)) / (valor_fatura - pagamento)) * 100
    
    return saldo_devedor, crescimento


valor_fatura = float(input('Insira o valor total da fatura: '))
pagamento1 = float(input('Insira o valor do primeiro pagamento (P1): '))
pagamento2 = float(input('Insira o valor do segundo pagamento (P2): '))
meses_sem_pagar = int(input('Insira por quantos meses a dívida ficou sem pagamento: '))


fatura_p1, crescimento_p1 = calcular_fatura(valor_fatura, pagamento1, meses_sem_pagar)
fatura_p2, crescimento_p2 = calcular_fatura(valor_fatura, pagamento2, meses_sem_pagar)


print('=======================')
print('Resumo da Simulação:')
print('=======================')
print(f'Cenário P1 - Valor Inicial: R${valor_fatura:.2f}, Valor Final: R${fatura_p1:.2f}, Crescimento: {crescimento_p1:.2f}%')
print(f'Cenário P2 - Valor Inicial: R${valor_fatura:.2f}, Valor Final: R${fatura_p2:.2f}, Crescimento: {crescimento_p2:.2f}%')
