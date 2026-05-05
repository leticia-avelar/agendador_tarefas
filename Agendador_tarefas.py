#1-Criar uma lista vazia chamada tarefas.
#2- Mostrar um menu para o usuário.
#3-Solicitar ao usuário  opçãoes Menu.

#3.1 opçã 1:
#pedir nome da tarefa;
#pedir prioridade;
#pedir tempo estimado;
#salvar como tarefa não concluída.

#3.2 opção 2:
#mostrar todas as tarefas cadastradas.

#3.3 opção 3:
#pedir o número da tarefa;
#status concluída.
#validação

#3.4 opção 4:
#somar o tempo estimado de todas as tarefas;
#mostrar o total.

#3.5 opção 5:
#encerrar o programa.

#4- restringir opções
#5- Mostrar ao usuário

tarefas = []

while True:

    print("Bem-vindo ao Agendador de Tarefas!")
    print("Escolha uma Opção do Menu:")
    print("\nMENU")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Calcular tempo total das tarefas")
    print("5. Sair")

    opcao = input("Escolha a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        tempo = float(input("Digite o tempo (em horas): "))
        concluida = False

        tarefa = [nome, tempo, concluida]
        tarefas.append(tarefa)

        print("Tarefa adicionada!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            numero = 0
            for tarefa in tarefas:
                print(numero, "-", tarefa)
                numero = numero + 1

    elif opcao == "3":
        indice = int(input("Digite o número da tarefa: "))

        if indice >= 0 and indice < len(tarefas):
            tarefas[indice][2] = True
            print("Tarefa concluída!")
        else:
            print("Número inválido!")

    elif opcao == "4":
        total = 0

        for tarefa in tarefas:
            total = total + tarefa[1]

        print("Tempo total:", total, "horas")

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
    
    
