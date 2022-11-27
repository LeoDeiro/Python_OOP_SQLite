#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

#Quero mostrar só o nome
print(poyatos.nome)
print(45*("-"))
#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Carregar lista do banco de dados
pessoas = pessoaDAO.getAll(True)

for pessoa in pessoas:
  print(pessoa)
  
#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = input("Informe o nome do ator/atriz: ")  
novo = Pessoa(0, novo)

#Olha que simples...
novo = pessoaDAO.save(novo)
print(5*"-"+"*Pessoa Adicionada*"+5*"-")
pessoas = pessoaDAO.getAll()

for pessoa in pessoas:
  print(pessoa)
  