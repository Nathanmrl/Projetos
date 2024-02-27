import random


class processo:

  def __init__(self, id, prioridade, tempo):
    self.id = id
    self.prioridade = prioridade
    self.tempo = tempo


if __name__ == '__main__':
  fila = []
  ids = []

  tempolista = 0

  while True:
    escolha = int(input("\n1 - Continuar\n2 - Sair\nEscolha: "))
    tempo = random.randint(1, 5)

    while tempolista == range(0, 10):
      process = processo(chr(random.randint(65, 90)), random.randint(1, 10),
                         tempo)
      fila.append(process)
      ids.append(process.id)
    if escolha == 1:
      tempolista += 1
      print(f'\nTempo: {tempo}\nProcessando: {fila[0].id}\nFila: {ids}')
      continue
    elif escolha == 2:
      break
      print(f'\nTempo: {tempo}\nProcessando: {fila[0].id}\nFila: {ids}')
 # for processo in processos_lista:
    #      print("Prioridade:", processo.prioridade)
    #      print("Tempo:", processo.tempo)
    #      print("Entrada:", processo.entrada)
    #      print("-------------------------")

    # print("Lista:")
    # for i, processo in enumerate(processos):
    #     print(f"Processo {i + 1} - Entrada:{processo.entrada}, Prioridade: {processo.prioridade}, Tempo: {processo.tempo}")
