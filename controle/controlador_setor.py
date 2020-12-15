from limite.tela_setor import TelaSetor
from entidade.setor import Setor
from controle.controlador_usuario import ControladorUsuario


class ControladorSetor:
  def __init__(self, controlador_principal):
    self.__controlador = controlador_principal
    self.__tela_setor = TelaSetor(self)
    self.__setores = []
    self.__usuarios = []
    self.__exibindo_tela = True

  def adicionar_setor(self):
    dados_setor = self.__tela_setor.solicita_dados_setor()
    novo_setor = Setor(dados_setor["nome_setor"])
    self.__setores.append(novo_setor)

  def remover_setor(self):
    info_setor = self.__tela_setor.qual_setor_remover()
    outro_setor = info_setor["nome_setor"]
    if not self.__setores:
      self.__tela_setor.lista_vazia()
    else:
      for nome in self.__setores:
        if nome.nome_setor != outro_setor:
          self.__tela_setor.nome_diferente()
        elif nome.nome_setor == outro_setor:
          self.__setores.remove(nome)
          self.__tela_setor.setor_removido()

  def listar_setor(self):
    if not self.__setores:
      self.__tela_setor.lista_vazia()
    for setor in self.__setores:
      self.__tela_setor.mostra_dados_setor(setor.nome_setor)

  def voltar(self):
    self.__exibindo_tela = False

  def agrega_usuario(self):
    info_setor = self.__tela_setor.solicita_nome_setor()
    outro_setor = info_setor["nome_setor"]
    for setor in self.__setores:
      if setor.nome_setor == outro_setor:
        usuario = self.__controlador.controlador_usuario.buscar_nome_usuario()
        self.__usuarios.append(usuario)

  def listar_usuarios_agregados(self):
    for usuario in self.__usuarios:
      self.__tela_setor.mostra_dados_usuario(usuario.nome_usuario)

  def abre_tela(self):
    lista_opcoes = {1: self.adicionar_setor,
						        2: self.remover_setor,
						        3: self.listar_setor, 
						        0: self.voltar,
                    4: self.agrega_usuario,
                    5: self.listar_usuarios_agregados}
    while self.__exibindo_tela:
      opcao_escolhida = self.__tela_setor.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()
