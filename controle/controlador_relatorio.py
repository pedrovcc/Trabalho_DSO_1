from limite.tela_relatorio import TelaRelatorio
from controle.controlador_projeto import ControladorProjeto
from datetime import datetime


class ControladorRelatorio:
    def __init__(self, controlador_principal):
        self.__controlador = controlador_principal
        self.__tela_relatorio = TelaRelatorio(self)
        self.__exibindo_tela = True

    def visualizar_relatorio(self):
        relatorio = self.__controlador.controlador_projeto.busca_projeto_pelo_codigo()

    def gerar_relatorio(self):
        a = self.__controlador.controlador_projeto.projetos()
        logFilePathParser = "C:/Users/pedro/OneDrive/Área de Trabalho/Trabalho_dso/Gerenciador_Projeto/logs/Logs_Gerenciador_Projetos.txt"
        logParser = open(logFilePathParser,'w')
        logParserArray = []
        logParserArray.append("----------ARQUIVO DE LOG GERENCIADOR DE PROJETOS----------\n")
        logParserArray.append('DATA DA CRIACAO: '+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        logParserArray.append("\nPROJETOS EXISTENTES:\n")
        logParserArray.append(str(a))
        logParserArray.append("\n")
        logParser.writelines(logParserArray)
        logParser.close()
        aviso = self.__tela_relatorio.dados_relatorio_texto()

    def voltar(self):
        self.__exibindo_tela = False

    def abre_tela(self):
        lista_opcoes = {1: self.visualizar_relatorio,
                        2: self.gerar_relatorio,
                        0: self.voltar}

        while self.__exibindo_tela:
            opcao_escolhida = self.__tela_relatorio.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
