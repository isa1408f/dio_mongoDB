from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    cpf = Column(String(11))
    endereco = Column(String(30))

    conta = relationship(
        "Conta", back_populates="cliente"
    )

    def __repr__(self):
        return f"(Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco}"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(30), nullable=False)
    agencia = Column(String(30), nullable=False)
    num = Column(String(30), nullable=False)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    saldo = Column(Float(12))

    cliente = relationship(
        "Cliente", back_populates="conta"
    )

    def __repr__(self):
        return f"Conta (id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero={self.num}, saldo={self.saldo})"


# conexao com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

inspector = inspect(engine)

with Session(engine) as session:
    Antonio = Cliente(
        nome='Antonio Santos',
        cpf="45789674125",
        endereco='antonio@gmail.com')

    Maria = Cliente(
        nome='Maria Nascimento',
        cpf="14796358714",
        endereco='maria@gmail.com')

    Marcelo = Cliente(
        nome='Marcelo Oliveira',
        cpf="74568952427",
        endereco='marcelo@gmail.com')

    # enviando para o BD
    session.add_all([Antonio, Maria, Marcelo])
    session.commit()

clientes = session.query(Cliente).all()
for cliente in clientes:
    print(cliente)

