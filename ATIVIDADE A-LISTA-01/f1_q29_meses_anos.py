# Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

# Entrada

valor_meses = int(input('Insira o numero de meses: '))

# Processamento

valor_anos = valor_meses // 12
resto_meses = valor_meses % 12

# Saída

print(f'O valor traduz para {valor_anos} ano(s) e {resto_meses} mês(s)')
