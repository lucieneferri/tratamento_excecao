#Tratando exceções
from paciente import Paciente, NameIsEmptyError

try:
    nome = input ('Digite o nome do seu animalzinho: ')
    p=Paciente(nome)
except TypeError:
    print('O nome deve ser uma string, tente novamente...')
except NameIsEmptyError:
    print('O nome não pode ser uma string vazia, preencha um valor...')
except Exception as e:
    print('Ocorreu um erro inesperado ao criar o objeto de Paciente')
    print('Informações do erro:', e)
else:
    print('Se chegou até aqui é porque não deu erro no TRY')
finally:
    print('Sempre será executado')