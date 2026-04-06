print(f"{(idade := int(input("Insira sua idade: "))) and ''}{("Maior que 65" if idade >= 65 else "Maior de idade" if idade >= 18 else "Menor de idade")}")
