# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.


# Entrada

idade_anos = int(input('Insira a quantidade de anos: '))

idade_meses = int(input('Insira a quantidade de meses: '))

idade_dias = int(input('Insira a quantidade de dias: '))

# Processamento

dias_final_ano = idade_anos * 365
dias_final_meses = idade_meses * 30
final_idade = dias_final_ano + dias_final_meses + idade_dias
# Saída

print(f'A idade apenas em dias é igual a ==> {final_idade}')
