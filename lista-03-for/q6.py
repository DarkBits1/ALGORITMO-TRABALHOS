
def main():
  tabuada = 0
  for i in range(1, 11, 1):
    print('-----------------------------')
    print(f'Tabuada do {i} até 10:')
    for j in range(1, 11, 1):
      tabuada = i*j
      print(f'{i}*{j}: {tabuada}')
        
main()