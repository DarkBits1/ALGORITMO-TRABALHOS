def main():
  tentativa_atual = 0
  tentativa_anterior = 0
  n = int(input('N > '))
  for i in range(1, 30000000, 1):
    if tentativa_atual + tentativa_anterior == n:
      print('Pronto.')
      break
    tentativa_anterior = tentativa_atual
    tentativa_atual = int(input('tenta aí > '))




main()