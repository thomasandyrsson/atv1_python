lista_tarefas = []

for n in range(10):
    tarefa = input(f">> INSIRA A TAREFA {n+1}: ")
    lista_tarefas.append(tarefa)

for n in range(10):
    print(f"{n+1} {lista_tarefas[n]}")