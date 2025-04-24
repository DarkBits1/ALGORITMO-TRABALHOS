def main():
  try:
   numero1 = float(input('Insira o primeiro número: '))
   numero2 = float(input('Insira o segundo número: '))
   numero3 = float(input('Insira o terceiro número: '))
   identificar_numeros(numero1, numero2, numero3)
  except ValueError:
   print('Insira um número válido.')
   return main()
  except:
   print('Erro inesperado. Tente novamente')
   return main()
  

def identificar_numeros(numero1, numero2, numero3):
  if (numero1 != numero2 and numero1 != numero3 and numero2 != numero3): 
    return print('Nenhum dos números é igual')
  elif numero1 == numero2 and numero1 == numero3: 
    return print('Todos os números são iguais')
  elif numero1 == numero2 or numero1 == numero3:
    return print('Dois números são iguais')
  




main()  
