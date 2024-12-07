class Consumo:
    def __init__(self):
        self.historico = []
        self.media = 0.0
        self.alerta = ""

    def registrar_consumo(self, valor):
        if valor < 0:
            return "Erro: Consumo inválido."
        
        self.historico.append(valor)
        self.calcular_media()
        self.gerar_alerta(valor)
        return {
            "Histórico": self.historico,
            "Média": self.media,
            "Alerta": self.alerta
        }

    def calcular_media(self):
        if self.historico:
            self.media = sum(self.historico) / len(self.historico)

    def gerar_alerta(self, valor):
        if valor < self.media:
            self.alerta = "Consumo abaixo da média."
        elif valor > self.media:
            self.alerta = "Consumo acima da média!"
        else:
            self.alerta = "Consumo dentro da média."

# Testando o sistema
monitoramento = Consumo()

# Testes com as entradas fornecidas
entradas = [50, 60, 100, 0, -20]

for consumo in entradas:
    resultado = monitoramento.registrar_consumo(consumo)
    print(f"Entrada: {consumo}\nSaída: {resultado}\n")
