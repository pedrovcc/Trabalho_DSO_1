from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario


class ControladorUsuario:
  def __init__(self, controlador_principal):
    self.__controlador = controlador_principal
    self.__tela_usuario = TelaUsuario(self)
    self.__exibindo_tela = True
    self.__usuarios = []

  def adicionar_usuario(self):
    dados_usuario = self.__tela_usuario.solicita_dados_usuario()
    novo_usuario = Usuario(dados_usuario["nome_usuario"], dados_usuario["id_usuario"])
    self.__usuarios.append(novo_usuario)

  def remover_usuario(self):
    info_usuario = self.__tela_usuario.qual_usuario_remover()
    outro_usuario = info_usuario["nome_usuario"]
    if not self.__usuarios:
      self.__tela_usuario.lista_vazia()
    else:
      for nome in self.__usuarios:
        if nome.nome_usuario != outro_usuario:
          self.__tela_usuario.nome_diferente()
          break
        elif nome.nome_usuario == outro_usuario:
          self.__usuarios.remove(nome)
          self.__tela_usuario.usuario_removido()

  def listar_usuarios(self):
    if not self.__usuarios:
      self.__tela_usuario.lista_vazia()
    for usuario in self.__usuarios:
      self.__tela_usuario.mostra_dados_usuario(usuario.nome_usuario, usuario.id_usuario)

  def voltar(self):
    self.__exibindo_tela = False

  def abre_tela(self):
    lista_opcoes = {1: self.adicionar_usuario,
						        2: self.remover_usuario,
						        3: self.listar_usuarios, 
						        0: self.voltar}
    while self.__exibindo_tela:
      opcao_escolhida = self.__tela_usuario.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()

  def buscar_nome_usuario(self):
    info_usuario = self.__tela_usuario.qual_usuario_agregar()
    outro_usuario = info_usuario["nome_usuario"]
    for nome in self.__usuarios:
      if nome.nome_usuario == outro_usuario:
        return nome
