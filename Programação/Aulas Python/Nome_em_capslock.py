import pyperclip

while True:
    # Coletar nome do colaborador
    nome = input("Digite o nome do colaborador ('sair' para encerrar): ")

    # Verificar se o usuário deseja sair
    if nome.lower() == 'sair':
        print("Encerrando o programa.")
        break

    # Transformar nome em maiúsculo
    nome_upper = nome.upper()

    # Apresentar nome em maíusculo
    print(nome_upper)

    # Copiar o nome do colaborador
    pyperclip.copy(nome_upper)
