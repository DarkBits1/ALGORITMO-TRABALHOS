# Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

def main():
  try:
   numero1 = float(input('Insira o primeiro número: '))
   numero2 = float(input('Insira o segundo número: '))
   numero3 = float(input('Insira o terceiro número: '))
   maior_numero(numero1, numero2, numero3)
  except ValueError:
    print('Valor inválido. Tente novamente.')
    return main()
  except:
    print('Erro inesperado. Tente novamente.')
    return main()


def maior_numero(num1, num2, num3):
  if (num1 > num2 and num1 > num3):
    return print(f'O maior número é o número {num1}')
  elif (num2 > num3):
    return print(f'O maior número é o número {num2}')  
  elif (num1 == num2 and num1 == num3):
    return print('Todos os valores são iguais.')
  else:
    return print(f'O maior número é o número {num3}')




main()
