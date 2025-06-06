def analisar_consumo_calorico():
    dias = int(input("Informe a quantidade de dias para análise: "))
    limite_calorias = float(input("Informe o limite calórico diário: "))

    consumos_totais = []
    for i in range(1, dias + 1):
        print(f"\nDia {i}:")
        cafe = float(input("  Calorias no café da manhã: "))
        almoco = float(input("  Calorias no almoço: "))
        jantar = float(input("  Calorias no jantar: "))
        lanches = float(input("  Calorias nos lanches: "))

        total_dia = cafe + almoco + jantar + lanches
        consumos_totais.append(total_dia)

  
    media_diaria = sum(consumos_totais) / dias
    dia_menor = consumos_totais.index(min(consumos_totais)) + 1
    dia_maior = consumos_totais.index(max(consumos_totais)) + 1

    print("\n=== Relatório Nutricional ===")
    print(f"Média calórica diária: {media_diaria:.2f} calorias")
    print(f"Dia com menor consumo: Dia {dia_menor} ({min(consumos_totais):.2f} calorias)")
    print(f"Dia com maior consumo: Dia {dia_maior} ({max(consumos_totais):.2f} calorias)")
    
    if media_diaria > limite_calorias:
        print("A média diária EXCEDEU o limite calórico informado.")
    else:
        print("A média diária NÃO excedeu o limite calórico informado.")

analisar_consumo_calorico()
