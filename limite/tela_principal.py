from limite.tela_abstrata import TelaAbstrata


class TelaPrincipal(TelaAbstrata):
  def __init__(self, controlador_principal):
    super().__init__(controlador_principal)

  def tela_opcoes(self):
    print()
    print(" ----------- Gerenciador de Projetos -----------")
    print()
    print("Escolha a opção:")
    print()
    print("1: Cadastrar Projeto")
    print("2: Cadastrar Tarefa")
    print("3: Cadastrar Usuario")
    print("4: Cadastrar Setor")
    print("5: Visualizar Relatorios")
    print("0: Encerrar Sistema")
    print()
    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
    return opcao
