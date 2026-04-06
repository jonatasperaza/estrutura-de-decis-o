print(
    f"Voce {('podera' if (__import__('datetime').datetime.now().year - (int(input('Insira seu ano de nascimento: ')))) >= 16 else 'não podera')} votar esse ano"
)
