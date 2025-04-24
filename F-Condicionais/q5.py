#Leia 3 (três) números e escreva-os em ordem crescente.

def main():
  try:
   num1 = float(input('Insira primeiro número:'))
   num2 = float(input('Insira segundo número:'))
   num3 = float(input('Insira terceiro número:'))
   ordem_num(num1, num2, num3)
  except:
    print('Erro. Insira um valor válido.')
    main() 

def ordem_num(num1, num2, num3):
  if(num1 > num2 and num1 > num3 and num3 > num2):
    print({num2})
    print({num3})
    print({num1})
  elif(num2 > num1 and num2 > num3 and num3 > num1):
    print({num1})
    print({num3})
    print({num2})    
  elif(num1 > num2 and num2 > num3):
    print({num3})
    print({num2})
    print({num1})  
  elif(num2 > num3 and num2 > num1 and num1 > num3):
    print({num1})
    print({num3})
    print({num2})  
  elif(num3 == num2 and num3 == num1):
    print('Todos os números são iguais.')
  elif(num3 > num2 and num3 > num1 and num2 > num1):
    print({num1})
    print({num2})
    print({num3})
  elif(num3 == num2 and num3 != num1):
    print({num1})
    print({num2})
    print({num3})
  elif(num1 > num2 and num1 > num3 and num3 > num2):
    print({num2})
    print({num3})
    print({num1})  
  elif (num1 == num2 and num1 != num3 and num3 > num1):
    print({num1})
    print({num2})
    print({num3})
  elif(num1 == num3 and num1 < num2):
    print({num1})
    print({num3})
    print({num2})  
  elif(num1 == num2 and num1 > num3):
    print({num3})
    print({num1})
    print({num2})  
  elif(num3 > num1 and num3 > num2 and num1 > num2):
    print({num2})
    print({num1})
    print({num3})  
  else:
    print({num2})
    print({num3})
    print({num1})  


main()  
