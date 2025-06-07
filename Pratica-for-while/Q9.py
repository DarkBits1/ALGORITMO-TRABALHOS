
valor_imovel = float(input("Valor do imóvel: R$ "))
entrada = float(input("Valor da entrada: R$ "))
taxa_juros = float(input("Taxa de juros mensal (%): ")) / 100
parcelas = int(input("Número de parcelas: "))

saldo = valor_imovel - entrada

print("Simulação de Financiamento:")
for i in range(1, parcelas + 1):
    juros = saldo * taxa_juros
    amortizacao = saldo / (parcelas - i + 1)
    valor_parcela = amortizacao + juros
    saldo -= amortizacao
    print(f"Parcela {i}: R$ {valor_parcela:.2f} (Juros: R$ {juros:.2f}) | Saldo devedor: R$ {saldo:.2f}")
