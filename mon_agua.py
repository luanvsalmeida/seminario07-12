"""
Projeto: Sistema de Monitoramento de Consumo de Água
Seminário Integrador - Talento Tech
Desenvolvido Por: Silivo Henrique
Caua Moraes
Gabriel Reginato 
Julia Franca
Luan Almeida
Data: 07/12/24
Descrição:
    Este projeto simula um sistema de monitoramento de consumo de água
    O sistema possui funcionalidades como:
    - Registrar o consumo de água.
    - Calcular o consumo médio de água.
    - Alertar o usuário quanto se o consumo está abaixo ou acima da média.
"""
# Classe que representa o sistema de monitoramento de consumo de água
class Consumo:
   
    def __init__(self):
        """
        Inicializa a classe com os seguintes atributos:
        - historico: lista que armazena os valores de consumo.
        - media: valor médio dos consumos registrados.
        - alerta: mensagem de alerta baseada no padrão de consumo.
        """
        self.historico = []  # Lista para armazenar os registros de consumo
        self.media = 0.0     # Média inicial do consumo
        self.alerta = ""     # Mensagem de alerta inicial

    def registrar_consumo(self, valor):
        """
        Registra um valor de consumo, valida o valor, atualiza o histórico,
        recalcula a média e gera um alerta.
       
        Parâmetros:
        - valor (float): o consumo a ser registrado.
       
        Retorno:
        - Dicionário com o histórico, média e alerta ou uma mensagem de erro.
        """
        if valor < 0:
            return "Erro: Consumo inválido."  # Valor negativo não é permitido

        # Adiciona o consumo ao histórico
        self.historico.append(valor)
       
        # Recalcula a média com base no novo valor
        self.calcular_media()
       
        # Gera o alerta com base no valor atual
        self.gerar_alerta(valor)
       
        return {
            "Histórico": self.historico,
            "Média": self.media,
            "Alerta": self.alerta
        }

    def calcular_media(self):
        """
        Calcula a média dos consumos registrados no histórico.
        """
        if self.historico:  # Verifica se há consumos no histórico
            self.media = sum(self.historico) / len(self.historico)  # Calcula a média

    def gerar_alerta(self, valor):
        """
        Gera um alerta com base no valor de consumo informado.
       
        Parâmetros:
        - valor (float): o valor de consumo registrado.
        """
        if valor < self.media:
            self.alerta = "Consumo abaixo da média."  # Quando o consumo é menor que a média
        elif valor > self.media:
            self.alerta = "Consumo acima da média!"  # Quando o consumo é maior que a média
        else:
            self.alerta = "Consumo dentro da média."  # Quando o consumo é igual à média


monitoramento = Consumo()  # Instancia o objeto de controle de consumo

# Testes com as entradas fornecidas
entradas = [50, 60, 100, 0, -20]

print("---------- TESTE DE MESA -----------")
for consumo in entradas:
    resultado = monitoramento.registrar_consumo(consumo)
    print(f"Entrada: {consumo}\nSaída: {resultado}\n")


# Função principal que executa o sistema de forma interativa
def executar_sistema():
    """
    Executa o sistema de forma interativa, exibindo o menu de opções para o usuário.
    """
   
    while True:  # Loop principal do sistema
        print("\n==== Sistema de Monitoramento de Consumo de Água ====")
        print("1 - Adicionar registro de consumo")
        print("2 - Encerrar aplicação")
       
        try:
            opcao = int(input("Escolha uma opção: "))  # Entrada da opção do usuário
           
            if opcao == 1:  # Opção para registrar consumo
                try:
                    valor = float(input("Digite o valor de consumo (número positivo): "))
                    resultado = monitoramento.registrar_consumo(valor)
                   
                    # Verifica se houve erro ou se o consumo foi registrado com sucesso
                    if isinstance(resultado, str):  # Caso seja uma mensagem de erro
                        print(f"\n⚠️ {resultado}")
                    else:  # Exibe o resultado completo
                        print("\n✅ Registro realizado com sucesso!")
                        print(f"Histórico: {resultado['Histórico']}")
                        print(f"Média: {resultado['Média']}")
                        print(f"Alerta: {resultado['Alerta']}")
               
                except ValueError:
                    print("\n⚠️ Erro: Digite um valor numérico válido.")
           
            elif opcao == 2:  # Opção para encerrar o sistema
                print("\nEncerrando a aplicação... Até a próxima!")
                break
           
            else:  # Caso o usuário insira uma opção inválida
                print("\n⚠️ Opção inválida. Escolha 1 ou 2.")
       
        except ValueError:  # Captura erro de entrada não numérica no menu
            print("\n⚠️ Erro: Digite apenas números para a opção.")



# Chama a função principal para executar o sistema
executar_sistema()