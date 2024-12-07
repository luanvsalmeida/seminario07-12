"""
Projeto: Sistema de Monitoramento de Alunos e Evasão Escolar
Disciplina: Seminário Integrador -Talento Tech
Desenvolvido Por:
Data 07/12/2024
Descrição:
    Este projeto simula um sistema de monitoramento de alunos para informar a situação do aluno nas disciplinas matriculadas
    O sistema possui funcionalidades como:
    - Calcula a média das notas do aluno.
    - Retorna 

"""

class Aluno:
    def __init__(self, frequencia, notas):
        """Inicializa o aluno com frequência e notas."""
        self.frequencia = frequencia
        self.notas = notas
        self.historico = []

    def calcular_media(self):
        """Calcula a média das notas do aluno."""
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_evasao(self):
        """Verifica se o aluno está em risco de evasão."""
        # Se a frequência for abaixo de 75% ou a média das notas for inferior a 7
        if self.frequencia < 75 or self.calcular_media() < 7:
            return True
        return False

    def atualizar_historico(self):
        """Atualiza o histórico do aluno com as novas notas."""
        self.historico.extend(self.notas)

    def exibir_resultado(self):
        """Exibe o histórico, média e o estado de evasão do aluno."""
        self.atualizar_historico()
        media = self.calcular_media()
        evasao = self.verificar_evasao()
        print(f"Histórico: {self.historico}, Média: {media:.2f}, Evasão: {evasao}")


class SistemaMonitoramento:
    def __init__(self):
        """Inicializa o sistema sem alunos inicialmente."""
        self.alunos = []

    def adicionar_aluno(self, frequencia, notas):
        """Adiciona um novo aluno ao sistema."""
        aluno = Aluno(frequencia, notas)
        self.alunos.append(aluno)

    def exibir_resultados(self):
        """Exibe o resultado de todos os alunos do sistema."""
        for aluno in self.alunos:
            aluno.exibir_resultado()


# Testes de entrada e saída
entradas = [
    (70, [80]),
    (70, [80, 90]),
    (85, [80, 90, 70]),
    (90, [80, 90, 70, 85]),
    (60, [80, 90, 70, 85])
]

# Criando o sistema e adicionando alunos
sistema = SistemaMonitoramento()

for frequencia, notas in entradas:
    sistema.adicionar_aluno(frequencia, notas)

# Exibindo os resultados para todos os alunos
sistema.exibir_resultados()
