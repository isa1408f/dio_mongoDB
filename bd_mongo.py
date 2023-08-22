import pymongo as pym
import pprint

client = pym.MongoClient(
    "mongodb+srv://[user]:[password]@cluster0.nrh13ab.mongodb.net/?retryWrites=true&w=majority")

db = client.test

# collection = db["Clientes"]

clientes = [
    {
        "id": 1,
        "nome": "Antonio Santos",
        "cpf": "45789674125",
        "endereco": "antonio@gmail.com",
    },

    {
        "id": 2,
        "nome": "Maria Nascimento",
        "cpf": "14796358714",
        "endereco": "maria@gmail.com",
     },

    {
        "id": 3,
        "nome": "Marcelo Oliveira",
        "cpf": "74568952427",
        "endereco": "marcelo@gmail.com",
     },
]

contas = [
    {
        "tipo": "Pessoa Física",
        "agencia": "001",
        "nr.conta": "0001-1",
        "saldo": 500,
        "id_cliente": 1
    },

    {
        "tipo": "Pessoa Física",
        "agencia": "001",
        "nr.conta": "0002-1",
        "saldo": 1000,
        "id_cliente": 2

     },

    {
        "tipo": "Pessoa Física",
        "agencia": "001",
        "nr.conta": "0003-1",
        "saldo": 1500,
        "id_cliente": 3
     },
]

print("==> Clientes -----")
db.clientes.insert_many(clientes)
for cliente in db.clientes.find():
    pprint.pprint(cliente)
    print("--------------------------")

print("===> Contas --------")
db.contas.insert_many(contas)
for conta in db.contas.find():
    pprint.pprint(conta)
    print("--------------------------")
