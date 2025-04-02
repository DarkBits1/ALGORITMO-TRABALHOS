# NESSE CENÁRIO HIPOTÉTICO, 1 LITRO DE GASOLINA GARANTE AUTONOMIA DE 15KM E O LITRO DO ALCOOL GARANTE AUTONOMIA DE 12KM



def gasolina(distancia_total, valor_gasolina, eletrico_percentual):
   distancia_menos_eletrico = (distancia_total - (distancia_total * (eletrico_percentual/100)))
   custo_gasolina = distancia_menos_eletrico / 15 * valor_gasolina
   litros_gasolina = distancia_menos_eletrico / 15

   resultado_gasolina = f"""
    
     VALOR QUE SERÁ GASTO COM GASOLINA = R${custo_gasolina:.2f}
     NÚMERO DE LITROS DE GASOLINA QUE SERÃO UTILIZADOS = {litros_gasolina:.2f} litros.
    """

   return resultado_gasolina




def alcool(distancia_total, valor_alcool, eletrico_percentual):
    distancia_menos_eletrico = (distancia_total - (distancia_total * (eletrico_percentual/100)))
    custo_alcool= distancia_menos_eletrico / 12 * valor_alcool
    litros_alcool = distancia_menos_eletrico / 12
    resultado_alcool = f"""
    
     VALOR QUE SERÁ GASTO COM ÁLCOOL = R${custo_alcool:.2f}
     NÚMERO DE LITROS DE ÁLCOOL QUE SERÃO UTILIZADOS = {litros_alcool:.2f} litros.
    """

    return resultado_alcool



usuario = input('Insira o seu nome de usuário: ')
print('=========================================================================\n')
print(f'SEJA BEM VINDO AO CALCULO DE CUSTO DE COMBUSTÍVEL, QUERIDO {usuario}.\n')
print('=========================================================================')
distancia_total = float(input('Insira a distancia total da viagem em quilômetros ==> '))
valor_alcool = float(input('Insira o valor do litro do álcool ==> R$'))
valor_gasolina = float(input('Insira o valor do litro da gasolina ==> R$'))
eletrico_percentual = float(input('Insira o percentual que conseguirá realizar da viagem com o motor elétrico ==> '))
print(gasolina(distancia_total, valor_gasolina, eletrico_percentual))

print(alcool(distancia_total, valor_alcool, eletrico_percentual))

