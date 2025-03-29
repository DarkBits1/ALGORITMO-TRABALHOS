# Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o numero de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

# Entrada

anos = int(input('A pessoa fuma a quantos anos? ==> '))
cigarros_dia = int(input('Essa pessoa fuma quantos cigarros por dia? ==>'))
carteira_preco = float(input('Qual o preço de uma carteira? ==> '))

# Processamento
anos_para_dias = anos * 365
dinheiro_gasto = (anos_para_dias * cigarros_dia) / 20 * carteira_preco



# Saída

print(f'A pessoa gastou {dinheiro_gasto} reais com cigarro em sua vida.')


