from limite.tela_abstrata import TelaAbstrata


class TelaProjeto(TelaAbstrata):
    def __init__(self, controlador_projeto):
        super().__init__(controlador_projeto)

    def tela_opcoes(self):
        print()
        print(" ----------- Adicionar Projeto -----------")
        print()
        print("Escolha a opção:")
        print()
        print("1: Adicionar Projeto")
        print("2: Remover Projeto")
        print("3: Verificar Projeto")
        print("0: Voltar")
        print()
        opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 0])
        return opcao

    def solicita_dados_projeto(self):
        print()
        print("Adicionar Projeto")
        print()
        titulo = input("Titulo do Projeto: ")
        codigo = int(input("Codigo do Projeto: "))
        descricao = input("Descrição do Projeto: ")
        custo = input("Custo do Projeto: ")
        print()
        print("O Projeto foi Criado!")
        return {"titulo": titulo, 
                "codigo": codigo, 
                "descricao": descricao, 
                "custo": custo}

    def mostra_dados_projeto(self, titulo: str, codigo: int, descricao: str, custo: str):
        print()
        print("----- Lista de Projetos -----")
        print()
        print("Titulo do Projeto: ", titulo)
        print()
        print("Codigo do Projeto: ", codigo)
        print()
        print("Descrição do Projeto: ", descricao)
        print()
        print("Custo do Projeto: R$ ", custo)
        print()


    def qual_projeto_remover(self):
        print()
        print("Remover projeto")
        print()
        codigo = int(input("Codigo do Projeto: "))
        return {"codigo": codigo}
    
    def mensagem_sucesso(self):
        print()
        print(" O Projeto foi removido! ")
        print()

    def mensagem_erro(self):
        print()
        print(" O Projeto não foi encontrado! ")
        print()

    def projeto_especifico(self, titulo: str, codigo: int, descricao: str, custo: str):
        print()
        print("Titulo do Projeto: ", titulo)
        print()
        print("Codigo do Projeto: ", codigo)
        print()
        print("Descrição do Projeto: ", descricao)
        print()
        print("Custo do Projeto: R$ ", custo)
        print()

    def buscar_projeto(self):
        print()
        print("Buscar Projeto")
        print()
        codigo = int(input("Codigo do Projeto: "))
        print()
        return {"codigo": codigo}

    def lista_vazia(self):
        print()
        print("Não existem projetos nessa lista!")
        print()        
