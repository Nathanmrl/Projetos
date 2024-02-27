class Processo:
    def __init__(self, nome, tempo, entrada):
        self.nome = nome
        self.tempo = tempo
        self.entrada = entrada

class Memoria:
    def __init__(self,ordem, tamanho):
        self.ordem = ordem
        self.tamanho = tamanho


if __name__ == '__main__':
    Processo1 = Processo("A", 3, 1)
    Processo2 = Processo("B", 3, 2)
    Processo3 = Processo("C", 1, 3)
    Memoria1 = Memoria(1,4)
    Memoria2 = Memoria(2,2)
    Memoria3 = Memoria(3,10)

    memorias = [Memoria1, Memoria2, Memoria3]

    processos = [Processo1, Processo2, Processo3]


    escolha = int(input("\n1 - Best-Fit\n2 - Worst-Fit\n3 - First-Fit\nEscolha: "))
    if escolha == 1:
            for processo in processos:
                menor_tamanho = float('inf')
                best_fit = None
                for memoria in memorias:
                    if memoria.tamanho >= processo.tempo:
                        if memoria.tamanho < menor_tamanho:
                            menor_tamanho = memoria.tamanho
                            best_fit = memoria
                if best_fit:
                    print(f"Processo {processo.nome} alocado na memória {best_fit.ordem}")
                    best_fit.tamanho -= processo.tempo
                else:
                    print(f"Não foi possível alocar o processo {processo.nome}")
    elif escolha == 2:
            for processo in processos:
                maior_tamanho = 0
                worst_fit = None
                for memoria in memorias:
                    if memoria.tamanho >= processo.tempo:
                        if memoria.tamanho > maior_tamanho:
                            maior_tamanho = memoria.tamanho
                            worst_fit = memoria
                if worst_fit:
                    print(f"Processo {processo.nome} alocado na memória {worst_fit.ordem}")
                    worst_fit.tamanho -= processo.tempo
                else:
                    print(f"Não foi possível alocar o processo {processo.nome}")

    elif escolha == 3:
        for processo in processos:
            first_fit = False
            for memoria in memorias:
                if memoria.tamanho >= processo.tempo:
                  memoria.tamanho -= processo.tempo
                  print(f"Processo {processo.nome} alocado na memória {memoria.ordem}")
                  first_fit = True
                  break
                if not first_fit:
                    print(f"Não foi possível alocar o processo {processo.nome}")