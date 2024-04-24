valor1 = int(input('Digite o primeiro valor: ' ))
valor2 = int(input('Digite o segundo valor: ' ))

if valor1 == valor2:
    print(f'Os valores "{valor1}" e "{valor2}" são iguais!')
elif valor1 > valor2:
    print(f'O valor "{valor1}" é maior que "{valor2}"')
elif valor1 < valor2:
    print(f'O valor "{valor1}" é menor que "{valor2}"')