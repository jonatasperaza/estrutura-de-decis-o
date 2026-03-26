print(
    f"O valor inserido é {(valor := 'Positivo' if (n := int(input('Informe um valor: '))) > 0 else 'Negativo' if n < 0 else 'Zero')}"
)
