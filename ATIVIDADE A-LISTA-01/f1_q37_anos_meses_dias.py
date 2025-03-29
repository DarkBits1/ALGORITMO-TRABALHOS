# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

# Entrada

dias = int(input('Insira a sua idade em dias: '))

# Processamento

anos = dias // 365

meses = (dias % 365) // 30

dias_final = (dias % 365) % 30

# Saída

print(f'Você possui {anos} ano(s), {meses} mês(meses) e {dias_final} dias de idade')
