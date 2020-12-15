from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa
from controle.controlador_projeto import ControladorProjeto


class ControladorTarefa:
    def __init__(self, controlador_principal):
        self.__controlador = controlador_principal
        self.__tela_tarefa = TelaTarefa(self)
        self.__exibindo_tela = True
        self.__tarefas = []

    def adicionar_tarefa(self):
        projeto_desejado = self.__controlador.controlador_projeto.busca_projeto_pelo_codigo()
        dados_tarefa = self.__tela_tarefa.solicita_dados_tarefa()
        nova_tarefa = Tarefa(dados_tarefa["titulo_tarefa"], 
                             dados_tarefa["descricao_tarefa"], 
                             dados_tarefa["prazo_tarefa"], 
                             dados_tarefa["situacao_tarefa"])
        self.__tarefas.append(nova_tarefa)

    def listar_tarefa(self):
        for tarefa in self.__tarefas:
            self.__tela_tarefa.mostrar_dados_tarefa(tarefa.titulo_tarefa, 
                                                    tarefa.descricao_tarefa, 
                                                    tarefa.prazo_tarefa, 
                                                    tarefa.situacao_tarefa)

    def remover_tarefa(self):
        info_tarefa = self.__tela_tarefa.qual_tarefa_remover()
        outra_tarefa = info_tarefa["titulo_tarefa"]
        for i in self.__tarefas:
            if i.titulo_tarefa == outra_tarefa:
                self.__tarefas.remove(i)

    def voltar(self):
        self.__exibindo_tela = False

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_tarefa,
                        2: self.remover_tarefa,
                        3: self.listar_tarefa,
                        0: self.voltar}

        while self.__exibindo_tela:
            opcao_escolhida = self.__tela_tarefa.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
