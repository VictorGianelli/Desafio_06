import pytest
from src.models.sqlite.repositories.cliente_repository import ClienteRepositoryInterface
from src.models.sqlite.settings.connection import db_connection_handler
from .cliente_repository import ClientesRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interacao com o banco")
def test_list_pets():
    repo = ClientesRepository(db_connection_handler)
    response = repo.list_pets()
    print("\n" , response)

@pytest.mark.skip(reason="interacao com o banco")
def test_delete_pet():
    name = "belinha"
    repo = ClientesRepository(db_connection_handler)
    repo.delete_pets(name)

def test_sacar_dinheiro_pessoa_fisica():
    quantia = 700

    repo = ClientesRepository(db_connection_handler)
    response = repo.sacar_dinheiro(quantia)
    print("\n","O saldo restante apos o saque é igual a", int(response))

# @pytest.mark.skip(reason="interacao com o banco")
def test_realizar_extrato_pessoa_fisica():
    pessoa = 1

    repo = ClientesRepository(db_connection_handler)
    response = repo.realizar_extrato(pessoa)
    print("\n","O saldo é igual a", int(response))

@pytest.mark.skip(reason="interacao com o banco")
def test_get_person():
    person_id = 1

    repo = ClientesRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print(response)
    print(response.pet_name)