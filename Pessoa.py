# Classe endereco
from datetime import date


class Endereco:
  def __init__(self, logradouro = '', numero = '', enderecoComercial = False):
    # Inicializar atributos com valores padrao
    self.logradouro = logradouro
    self.numero = numero
    self.endereco_comercial = enderecoComercial
    
# Classe pessoa
class Pessoa:
  def __init__(self, nome = '', rendimento = 0.0, endereco = None):
    self.nome = nome
    self.rendimento = rendimento
    self.endereco = endereco

  def calcular_imposto(self, rendimento):
    return rendimento

# Classe pessoa fisica
class PessoaFisica(Pessoa):

  def __init__(self, nome = '', rendimento = 0.0, endereco= None, cpf = '', dataNascimento = None):
    if endereco is None:
      # Se nenhum endereco for fornecido, cria um objeto padrão
      endereco = Endereco()
    
    if dataNascimento is None:
      dataNascimento = date.today()

    super().__init__(nome, rendimento, endereco)
    # Chamar o construtor da superclasse Pessoa para inicializar os atributos herdados
    # Atributos da propria classe
    self.cpf = cpf
    self.data_nascimento = dataNascimento

  def calcular_imposto(self, rendimento: float) -> float:
    # Sem imposto para rendimento ate 1500
    if rendimento <= 1500:
      return 0
    # 2% de imposto para rendimento entre 1500 e 3500
    elif 1500 < rendimento <= 3500:
      return rendimento * 0.02
    # 3.5% de imposto para rendimento entre 3500 e 6000
    elif 3500 < rendimento <= 6000:
      return rendimento * 0.035
    # 5% de imposto para rendimento acima de 6000
    else:
      return rendimento * 0.05
    
# Classe pessoa juridica
class PessoaJuridica(Pessoa):

  def __init__(self, nome = '', rendimento = 0.0, endereco= None, cnpj = '', nome_empresa = ''):
    if endereco is None:
      # Se nenhum endereco for fornecido, cria um objeto padrão
      endereco = Endereco()

    super().__init__(nome, rendimento, endereco)
    # Chamar o construtor da superclasse Pessoa para inicializar os atributos herdados
    # Atributos da propria classe
    self.cnpj = cnpj
    self.nome_empresa = nome_empresa

  def calcular_imposto(self, rendimento: float) -> float:
    # Sem imposto para rendimento ate 1500
    if rendimento <= 100000:
      return 0
    # 2% de imposto para rendimento entre 1500 e 3500
    elif 100000 < rendimento <= 200000:
      return rendimento * 0.02
    # 3.5% de imposto para rendimento entre 3500 e 6000
    elif 200000 < rendimento <= 300000:
      return rendimento * 0.035
    # 5% de imposto para rendimento acima de 6000
    else:
      return rendimento * 0.05
