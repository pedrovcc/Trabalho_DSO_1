from limite.tela_abstrata import TelaAbstrata


class TelaTarefa(TelaAbstrata):
    def __init__(self, controlador_tarefa):
        super().__init__(controlador_tarefa)

    def tela_opcoes(self):
        print()
        print(" ----------- Adicionar Tarefa -----------")
        print()
        print("Escolha a opção")
        print()
        print("1: Adicionar Tarefa")
        print("2: Remover Tarefa")
        print("3: Situação das Tarefas")
        print("0: Voltar")
        print()
        opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 0])
        return opcao

    def solicita_dados_tarefa(self):
        print()
        print("Adicionar Tarefa")
        print()
        titulo_tarefa = input("Título: ")
        descricao_tarefa = input("Descrição: ")
        prazo_tarefa = input("Data de entrega: ")
        situacao_tarefa = input("Situação: ")
        print()
        print("A tarefa foi criada")
        print()
        return {"titulo_tarefa": titulo_tarefa,
                "descricao_tarefa": descricao_tarefa,
                "prazo_tarefa": prazo_tarefa,
                "situacao_tarefa": situacao_tarefa}

    def mostrar_dados_tarefa(self, titulo_tarefa: str, descricao_tarefa: str, 
                             prazo_tarefa: str, situacao_tarefa:str):
        print()
        print("Lista de tarefas:")
        print()
        print("Titulo: ", titulo_tarefa)
        print()
        print("Descrição: ", descricao_tarefa)
        print()
        print("Data de entrega: ", prazo_tarefa)
        print()
        print("Situação: ", situacao_tarefa)
        print()

    def qual_tarefa_remover(self):
        print()
        print("Remover Tarefa")
        print()
        titulo_tarefa = input("Titulo da Tarefa: ")
        print()
        print("Tarefa Removida")
        print()
        return {"titulo_tarefa": titulo_tarefa}

    def edita_situacao(self):
        print()
        print("Editar a Tarefa")
        print()
