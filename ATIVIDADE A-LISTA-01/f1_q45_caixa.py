# Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.

# No meu exemplo, a máquina só dispôe de notas de 50, 10, 5 e 1 reais

# Entrada

valor_total = int(input('Qual a quantia que deseja retirar? : '))

# Processamento

nota_50 = valor_total // 50
nota_10 = (valor_total % 50) // 10
nota_5 = ((valor_total % 50) % 10) // 5
nota_1 = valor_total % 5


# Saída

print(f'Você receberá {nota_50} nota(s) de 50R$, {nota_10} nota(s) de 10R$, {nota_5} nota(s) de 5 e {nota_1} nota(s) de 1R$')



