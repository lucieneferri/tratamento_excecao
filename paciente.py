class NameIsEmptyError(Exception):#esta excessão foi criada e ela herda da classe mãe EXCEPTION os comportamentos.
  pass

class Paciente:
  def __init__(self, nome):
       self.paciente = nome

  @property #faz o papel de um getter,apenas para vizualizar o que o argumento retorna o valor da variável NOME.
  def paciente(self):
    return self._paciente

  @paciente.setter
  def paciente(self,nome):
    if not isinstance(nome, str):
      raise TypeError ("'nome' inválido")
    if nome == '':
      raise NameIsEmptyError("'Name' é obrigatório")
    self._paciente = nome #se as condições acima não acontecerem, então é atribuido ao argumento o valor da variável NOME.