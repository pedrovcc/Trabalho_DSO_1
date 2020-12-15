from limite.tela_abstrata import TelaAbstrata


class TelaRelatorio(TelaAbstrata):
    def __init__(self, controlador_relatorio):
        super().__init__(controlador_relatorio)

    def tela_opcoes(self):
        print()
        print(" ----------- Adquirir de Relatórios -----------")
        print()
        print("Escolha a opção")
        print()
        print("1: Visualizar Relatório")
        print("2: Gerar Relatório")
        print("0: Voltar")
        print()
        opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 0])
        return opcao

    def mostra_dados_relatório(self):
        print()
        print("------- Visualizar Projeto -------")
        print()
        codigo = int(input("Código do Projeto: "))
        print()
        return {"codigo": codigo}

    def dados_relatorio_texto(self):
        print()
        print("---- Relatório Gerado ----")
        print()