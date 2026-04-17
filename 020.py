print(f"{(num1 := float(input('Insira o primeiro valor: '))) and ''}{(num2 := float(input('Insira o segundo valor: '))) and ''}{(num3 := float(input('Insira o terceiro valor: '))) and ''}{(f'O maior valor é {num1}.' if num1 > num2 and num1 > num3 else (f'O maior valor é {num2}.' if num2 > num1 and num2 > num3 else f'O maior valor é {num3}.'))}")


