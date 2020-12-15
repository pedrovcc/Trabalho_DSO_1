from limite.tela_abstrata import TelaAbstrata


class TelaSetor(TelaAbstrata):
  def __init__(self, controlador_setor):
    super().__init__(controlador_setor)

  def tela_opcoes(self):
    print(" ----------- Adicionar Setor -----------")
    print("Escolha a opção")
    print()
    print("1: Adicionar Setor")
    print("2: Remover Setor")
    print("3: Lista Setores")
    print("4: Agrega Usuario")
    print("5: Listar Usuario(s) Agredado(s)")
    print("0: Voltar")
    print()
    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
    return opcao

  def solicita_dados_setor(self):
    print()
    print("Adicionar Setor")
    print()
    nome_setor = input("Nome do Setor: ")
    print()
    print("Setor foi adicionado")
    print()
    return {"nome_setor": nome_setor}

  def qual_setor_remover(self):
    print()
    print("Remover Setor")
    print()
    nome_setor = input("Nome do Setor: ")
    print()
    return {"nome_setor": nome_setor}

  def mostra_dados_setor(self, nome_setor: str):
    print()
    print("Setor: ", nome_setor)
    print()

  def solicita_nome_setor(self):
    print()
    print("Nome do setor")
    print()
    nome_setor = input("Nome do Setor: ")
    print()
    return {"nome_setor": nome_setor}

  def mostra_dados_usuario(self, nome_usuario: str):
    print()
    print("Usuario ", nome_usuario, "foi adicionado no setor")
    print()

  def lista_vazia(self):
    print()
    print("Essa lista esta vazia!")
    print()

  def nome_diferente(self):
    print()
    print("Esse nome nao se encontra na lista!")
    print()

  def setor_removido(self):
    print()
    print("Setor Removido")
    print()
