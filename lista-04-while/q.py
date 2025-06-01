def calcular_pontuacao():
    pontos_por_colocacao = {1: 9, 2: 6, 3: 4, 4: 3}
    total_clube_a = 0
    total_clube_b = 0

    while True:
        numero_prova = int(input("Número da prova: "))
        qtd_nadadores = int(input("Quantidade de nadadores: "))

        if numero_prova == 0 and qtd_nadadores == 0:
            break

        for _ in range(qtd_nadadores):
            nome = input("Nome do nadador: ")
            classificacao = int(input("Classificação (1 a 4): "))
            tempo = float(input("Tempo: "))
            clube = input("Clube (a ou b): ").lower()

            pontos = pontos_por_colocacao.get(classificacao, 0)

            if clube == 'a':
                total_clube_a += pontos
            elif clube == 'b':
                total_clube_b += pontos

    print(f"\nTotal de pontos do Clube A: {total_clube_a}")
    print(f"Total de pontos do Clube B: {total_clube_b}")

    if total_clube_a > total_clube_b:
        print("Clube A é o vencedor!")
    elif total_clube_b > total_clube_a:
        print("Clube B é o vencedor!")
    else:
        print("Empate!")

# Executa o programa
calcular_pontuacao()
