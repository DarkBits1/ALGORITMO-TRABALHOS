

alimentos = {
    "arroz": {"calorias": 130, "proteinas": 2.7},
    "feijao": {"calorias": 95, "proteinas": 6.6},
    "frango": {"calorias": 165, "proteinas": 31},
    "carne": {"calorias": 250, "proteinas": 26},
    "ovo": {"calorias": 143, "proteinas": 13},
    "leite": {"calorias": 61, "proteinas": 3.2},
    "banana": {"calorias": 89, "proteinas": 1.1},
    "maçã": {"calorias": 52, "proteinas": 0.3},
    "pão": {"calorias": 265, "proteinas": 9},
    "batata": {"calorias": 77, "proteinas": 2}
}


dados_pessoas = []
def main():
  qtd_pessoas = int(input("Digite a quantidade de pessoas: "))

  for i in range(qtd_pessoas):
    print(f"\nPessoa {i+1}:")
    qtd_alimentos = int(input("Quantidade de alimentos consumidos: "))
    total_calorias = 0
    total_proteinas = 0
    
    for j in range(qtd_alimentos):
        while True:
            nome = input(f"Nome do alimento #{j+1}: ").strip().lower()
            if nome in alimentos:
                break
            else:
                print("Alimento inválido. Tente novamente.")
        
        gramas = float(input(f"Quantidade (g) de {nome}: "))
        calorias = alimentos[nome]["calorias"] * gramas / 100
        proteinas = alimentos[nome]["proteinas"] * gramas / 100
        total_calorias += calorias
        total_proteinas += proteinas

    dados_pessoas.append({
        "pessoa": i+1,
        "calorias": total_calorias,
        "proteinas": total_proteinas
    })


  print("\nResumo nutricional por pessoa:")
  for dados in dados_pessoas:
    print(f"Pessoa {dados['pessoa']}: {dados['calorias']:.2f} calorias, {dados['proteinas']:.2f}g de proteínas")

  mais_calorias = dados_pessoas[0]
  menos_calorias = dados_pessoas[0]

  for pessoa in dados_pessoas[1:]:
    if pessoa["calorias"] > mais_calorias["calorias"]:
        mais_calorias = pessoa
    if pessoa["calorias"] < menos_calorias["calorias"]:
        menos_calorias = pessoa

  print(f"\nPessoa com MAIOR consumo calórico: Pessoa {mais_calorias['pessoa']} ({mais_calorias['calorias']:.2f} cal)")
  print(f"Pessoa com MENOR consumo calórico: Pessoa {menos_calorias['pessoa']} ({menos_calorias['calorias']:.2f} cal)")


main()
