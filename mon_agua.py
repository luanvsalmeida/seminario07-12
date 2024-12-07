class Consumo:
    def __init__(self):
        self.__historico = []
        self.__media = 0.0
        self.__alerta = ""

    def registrar_consumo(self, valor):
        if valor < 0:
            return "Erro: Consumo inválido."
        
        self.__historico.append(valor)
        self.calcular_media()
        self.gerar_alerta(valor)
        return {
            "Histórico": self.__historico,
            "Média": self.__media,
            "Alerta": self.__alerta
        }

    def calcular_media(self):
        if self.__historico:
            self.__media = sum(self.__historico) / len(self.__historico)

    def gerar_alerta(self, valor):
        if valor < self.__media:
            self.__alerta = "Consumo abaixo da média."
        elif valor > self.__media:
            self.__alerta = "Consumo acima da média!"
        else:
            self.__alerta = "Consumo dentro da média."

# Testando o sistema
monitoramento = Consumo()

# Testes com as entradas fornecidas
entradas = [50, 60, 100, 0, -20]

for consumo in entradas:
    resultado = monitoramento.registrar_consumo(consumo)
    print(f"Entrada: {consumo}\nSaída: {resultado}\n")
