print(
    f"{(nascimento := input('Insira seu ano de nascimento: ')) and ''}{(f'Sua idade é de {__import__("datetime").datetime.now().year - int(nascimento)}' if (nascimento.isdigit()) else 'Insira um valor válido')}"
)
