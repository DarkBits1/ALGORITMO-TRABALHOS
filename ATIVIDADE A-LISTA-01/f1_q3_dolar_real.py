# Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

# Entrada

quant_dolar = float(input('Insira quantidade em dólar: '))
cotacao_dolar = float(input('Insira a cotação do dólar: '))

#Processamento

real = quant_dolar * cotacao_dolar

#Saída

print(f'O valor equivalente em reais é ==> R${real:.2f}')
