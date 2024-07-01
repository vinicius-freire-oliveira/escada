class Escada:
    # Método inicializador da classe Escada
    def __init__(self, altura_espelho=None, largura_degrau=None):
        self.altura_espelho = altura_espelho  # Altura do espelho do degrau (opcional)
        self.largura_degrau = largura_degrau  # Largura do degrau (opcional)
    
    # Método para calcular a altura do espelho baseado na largura do degrau
    def calcular_altura_espelho(self):
        if self.largura_degrau is not None:
            # Fórmula para calcular a altura do espelho
            return (0.64 - self.largura_degrau) / 2
        else:
            # Lança um erro se a largura do degrau não estiver definida
            raise ValueError("A largura do degrau deve ser definida para calcular a altura do espelho.")

    # Método para calcular a largura do degrau baseado na altura do espelho
    def calcular_largura_degrau(self):
        if self.altura_espelho is not None:
            # Fórmula para calcular a largura do degrau
            return 0.64 - 2 * self.altura_espelho
        else:
            # Lança um erro se a altura do espelho não estiver definida
            raise ValueError("A altura do espelho deve ser definida para calcular a largura do degrau.")
    
    # Método para calcular o número de degraus necessários para vencer um desnível
    def calcular_numero_degraus(self, desnivel):
        if self.altura_espelho is None:
            # Calcula a altura do espelho se não estiver definida
            self.altura_espelho = self.calcular_altura_espelho()
        # Calcula e arredonda o número de degraus baseado no desnível e altura do espelho
        numero_degraus = round(desnivel / self.altura_espelho)
        return numero_degraus

# Exibe apresentação
print("\n####### Cálculo de escada #######\n")
# Pergunta ao usuário se ele quer calcular a altura do espelho (h) ou a largura do degrau (p)
escolha = input("Digite 'h' para calcular a altura do espelho ou 'p' para calcular a largura do degrau: ")
escada = Escada()

if escolha == 'h':
    # Se o usuário escolheu 'h', solicita a largura do degrau
    largura_degrau = float(input("Digite a largura do degrau (em metros): "))
    escada.largura_degrau = largura_degrau  # Define a largura do degrau na instância da classe Escada
    # Calcula a altura do espelho com base na largura do degrau fornecida
    altura_espelho = escada.calcular_altura_espelho()
    print("A altura do espelho é:", altura_espelho, "metros")
elif escolha == 'p':
    # Se o usuário escolheu 'p', solicita a altura do espelho
    altura_espelho = float(input("Digite a altura do espelho (em metros): "))
    escada.altura_espelho = altura_espelho  # Define a altura do espelho na instância da classe Escada
    # Calcula a largura do degrau com base na altura do espelho fornecida
    largura_degrau = escada.calcular_largura_degrau()
    print("A largura do degrau é:", largura_degrau, "metros")

# Solicita ao usuário o desnível a ser vencido
desnivel = float(input("Digite o desnível a ser vencido (em metros): "))

# Calcula o número de degraus necessários para vencer o desnível
numero_degraus = escada.calcular_numero_degraus(desnivel)
print("Número de espelhos:", numero_degraus)

# Calcula a largura total da escada (projeção horizontal) se a largura do degrau estiver definida
if escada.largura_degrau is not None:
    largura_total = (numero_degraus - 1) * escada.largura_degrau
    print("A projeção horizontal total da escada é:", largura_total, "metros")

