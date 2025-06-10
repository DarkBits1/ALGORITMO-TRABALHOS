import math

def eval_loop():
  entrada = ''
  while True:
   entrada = input('Coloque a a entrada: ')

   if entrada == 'done':
     break
   else:
    resultado = eval(entrada)
    print(resultado)
   
 



eval_loop()