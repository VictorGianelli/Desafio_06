import pytest
from src.models.sqlite.repositories.cliente_repository import ClienteRepositoryInterface
from src.models.sqlite.settings.connection import db_connection_handler
from .cliente_repository import ClientesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_sacar_dinheiro_pessoa_fisica():
    quantia = 11000
    tipo_pessoa = "fisica"

    repo = ClientesRepository(db_connection_handler)
    response = repo.sacar_dinheiro(quantia,tipo_pessoa)
    print("\n", response[0],response[1])

@pytest.mark.skip(reason="interacao com o banco")
def test_realizar_extrato_pessoa_fisica():
    pessoa = "João da Silva"
    tipo_nome = "completo"

    repo = ClientesRepository(db_connection_handler)
    response = repo.realizar_extrato(pessoa, tipo_nome)
    print("\n","O saldo é igual a", int(response))

@pytest.mark.skip(reason="interacao com o banco")
def test_sacar_dinheiro_pessoa_juridica():
    quantia = 11000
    tipo_pessoa = "juridica"

    repo = ClientesRepository(db_connection_handler)
    response = repo.sacar_dinheiro(quantia,tipo_pessoa)
    print("\n", response[0],response[1])

@pytest.mark.skip(reason="interacao com o banco")
def test_realizar_extrato_pessoa_juridica():
    pessoa = "Empresa XYZ"
    tipo_nome = "fantasia"

    repo = ClientesRepository(db_connection_handler)
    response = repo.realizar_extrato(pessoa, tipo_nome)
    print("\n","O saldo é igual a", int(response))
