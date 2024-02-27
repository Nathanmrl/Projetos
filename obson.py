class Memoria:
    def __init__(self, tamanho):
        self.espacos = [None] * tamanho

    def enviar_mensagem(self, mensagem, endereco):
        if self.espacos[endereco] is None:
            self.espacos[endereco] = mensagem
            print(f"Processo atual: Mensagem '{mensagem}' enviada para endereço {endereco}.")
        else:
            print(f"Processo atual: O endereço {endereco} já está ocupado com '{self.espacos[endereco]}'.")

    def receber_mensagem(self, endereco):
        if self.espacos[endereco] is not None:
            mensagem = self.espacos[endereco]
            print(f"Processo atual: Mensagem '{mensagem}' recebida do endereço {endereco}.")
            self.espacos[endereco] = None
        else:
            print(f"Processo atual: O endereço {endereco} está vazio.")

class Processo:
    def __init__(self, nome):
        self.nome = nome

def criar_processo():
    nome = input("Digite o nome do processo: ")
    return Processo(nome)

def menu():
    print("Selecione uma ação:")
    print("1. Adicionar processo")
    print("2. Enviar mensagem")
    print("3. Receber mensagem")
    print("4. Sair")

if __name__ == "__main__":
    tamanho_memoria = 10
    memoria_computador = Memoria(tamanho_memoria)
    processos = []

    while True:
        menu()
        escolha = input("Escolha uma ação (1/2/3/4): ")

        if escolha == "1":
            processo = criar_processo()
            processos.append(processo)
            print(f"Processo '{processo.nome}' criado.")
        elif escolha == "2":
            if not processos:
                print("Nenhum processo criado ainda.")
                continue

            endereco = int(input("Digite o endereço de destino: "))
            mensagem = input("Digite a mensagem a ser enviada: ")
            memoria_computador.enviar_mensagem(mensagem, endereco)
        elif escolha == "3":
            if not processos:
                print("Nenhum processo criado ainda.")
                continue

            endereco = int(input("Digite o endereço de origem: "))
            memoria_computador.receber_mensagem(endereco)
        elif escolha == "4":
            break
        else:
            print("Escolha inválida. Tente novamente.")
