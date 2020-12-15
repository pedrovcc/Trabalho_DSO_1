from limite.tela_abstrata import TelaAbstrata


class TelaUsuario(TelaAbstrata):
  def __init__(self, controlador_usuario):
    super().__init__(controlador_usuario)

  def tela_opcoes(self):
    print(" ----------- Usuario -----------")
    print("Escolha a opção")
    print()
    print("1: Adicionar Usuario")
    print("2: Remover Usuario")
    print("3: Lista Usuarios")
    print("0: Voltar")
    print()
    opcao = self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 0])
    return opcao

  def solicita_dados_usuario(self):
    print()
    print("Adicionar Usuario")
    print()
    nome_usuario = input("Nome do Usuario: ")
    id_usuario = input("Id do Usuario: ")
    print()
    print("Usuario foi adicionado")
    print()
    return {"nome_usuario": nome_usuario, "id_usuario": id_usuario}

  def qual_usuario_remover(self):
    print()
    print("Remover Usuario")
    print()
    nome_usuario = input("Nome do Usuario: ")
    return {"nome_usuario": nome_usuario}

  def mostra_dados_usuario(self, nome_usuario: str, id_usuario: str):
    print()
    print("Nome Usuario: ", nome_usuario)
    print("Id do Usuario: ", id_usuario)
    print()

  def qual_usuario_agregar(self):
    print()
    print("Nome do Usuario")
    print()
    nome_usuario = input("Nome do Usuario: ")
    print()
    return {"nome_usuario": nome_usuario}

  def lista_vazia(self):
    print()
    print("Essa lista esta vazia!")
    print()

  def nome_diferente(self):
    print()
    print("Esse nome nao se encontra na lista!")
    print()

  def usuario_removido(self):
    print()
    print("Usuario Removido")
    print()
