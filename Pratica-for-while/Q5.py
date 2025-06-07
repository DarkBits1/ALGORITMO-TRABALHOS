


def main():
  qtd_horas = int(input('Horas > '))
  contagem = 0
  maior_temp = 0
  menor_umidade = 0
  limite = float(input('Insira o limite de temperatura > '))

  for i in range(qtd_horas):
    temp = float(input('Insira a temperatura em graus celsius > '))
    umidade = float(input('Insira umidade em % > '))
    if temp > limite:
      contagem += 1
    if temp > maior_temp:
      maior_temp = temp
    if umidade < menor_umidade or i == 0:
      menor_umidade = umidade
    
  print (resultado(maior_temp, menor_umidade, contagem))



def resultado (maior_temp, menor_umidade, contagem):

  return print(f"""
-----------------
               
  MENOR UMIDADE > {menor_umidade}%
  MAIOR TEMP > {maior_temp}°C
  VEZES Q ULTRAPASSOU > {contagem}

------------------------

""")
main()
