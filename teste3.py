import random

if __name__ == '__main__':

    escalonador = []

    tempo = 0

    while True:

        escolha = int(input("\n1 - Adicionar Processo\n2 - Continuar\n3 - Sair\nEscolha: "))

        if escolha == 1:
            escalonador.append([random.randint(0, 10), chr(
                random.randint(65, 90)), random.randint(1, 5)])
            processo = sorted(escalonador)
            prioridade, id, tempos = zip(*processo)
            id = list(id)
        elif escolha == 2:
            tempo += 1
            if len(escalonador) == 0:
                print('\nEscalonador Vazio')
                continue
            if len(processo) == 0:
                print('\nEscalonador Vazio')
                continue
            if processo[0][2] > 0:
                processo[0][2] -= 1
        elif escolha == 3:
            break

        print(f'Tempo: {tempo}')
        print(
            f'\nProcessando: \nId: {processo[0][1]}\nPrioridade: {processo[0][0]}\nTempo Restante: {processo[0][2]}\n')
        print(f"Fila: {id[1:]}")

        if processo[0][2] == 0:
            processo.pop(0)
            id.pop(0)
            escalonador.pop(0)