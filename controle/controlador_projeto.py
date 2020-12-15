from limite.tela_projeto import TelaProjeto
from entidade.projeto import Projeto


class ControladorProjeto:
    def __init__(self, controlador_principal):
        self.__controlador = controlador_principal
        self.__tela_projeto = TelaProjeto(self)
        self.__exibindo_tela = True
        self.__projetos = []
        self.__tarefas = []

    def adicionar_projeto(self):
        dados_projeto = self.__tela_projeto.solicita_dados_projeto()
        novo_projeto = Projeto(dados_projeto["titulo"],
                               dados_projeto["codigo"],
                               dados_projeto["descricao"],
                               dados_projeto["custo"])
        self.__projetos.append(novo_projeto)

    def remover_projeto(self):
        info_projeto = self.__tela_projeto.qual_projeto_remover()
        outro_projeto = info_projeto["codigo"]
        for projeto in self.__projetos:
            if projeto.codigo == outro_projeto:
                self.__projetos.remove(projeto)
                self.__tela_projeto.mensagem_sucesso()
            elif projeto.codigo != outro_projeto:
                self.__tela_projeto.mensagem_erro()

    def busca_projeto_pelo_codigo(self):
        info_tela_projeto = self.__tela_projeto.buscar_projeto()
        info_projeto_tela = info_tela_projeto["codigo"]
        for i in self.__projetos:
            if i.codigo == info_projeto_tela:
                self.__tela_projeto.projeto_especifico(i.titulo, i.codigo, i.descricao, i.custo)
            elif i.codigo != info_projeto_tela:
                self.__tela_projeto.mensagem_erro()

    def projetos(self):
        for i in self.__projetos:
            return i

    def verifica_projeto(self):
        for projeto in self.__projetos:
            self.__tela_projeto.mostra_dados_projeto(projeto.titulo, projeto.codigo, projeto.descricao, projeto.custo)
            if not self.__projetos:
                self.__tela_projeto.lista_vazia()

    def voltar(self):
        self.__exibindo_tela = False

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_projeto,
                        2: self.remover_projeto,
                        3: self.verifica_projeto,
                        0: self.voltar}

        while self.__exibindo_tela:
            opcao_escolhida = self.__tela_projeto.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
