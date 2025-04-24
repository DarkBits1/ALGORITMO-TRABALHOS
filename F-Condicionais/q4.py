#Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade



def main():
  try:
   num = int(input('Insira o número: '))
   calc_num(num)
  except:
    print('Erro. Insira um valor válido de 2 dígitos.')
    return main()
  
def calc_num(num):
  dezena = num // 10
  unidade = num % 10
  if(dezena == unidade):
    print('O algarismo da dezena e da unidade são iguais')
  else:
    print('O algarismo da dezena e da unidade são diferentes.')  



main()
