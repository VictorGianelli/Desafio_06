import pytest
from .pessoa_fisica_creator_controller import PessoaFisicaCreatorController 

class MockPeopleRepository:
    def insert_person(self, renda_mensal: str, idade: str, nome_completo: str, celular: str, email: str, categoria: str, saldo: str, ):
        pass


# @pytest.mark.skip(reason="Erro não concertado")
def test_create():
    person_infor = {
        "renda_mensal": 2000,
        "idade": 28,
        "nome_completo": "John Doe",
        "celular": "9999-9999",
        "email": "john@doe.com",
        "categoria": "2",
        "saldo": 9000
    }

    controller = PessoaFisicaCreatorController(MockPeopleRepository())
    response = controller.create(person_infor)

    # print(response)
    assert response["data"]["type"] == "Perssoa Fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infor

def test_create_error():
    person_infor = {
        "renda_mensal": 2000,
        "idade": 28,
        "nome_completo": "John123 Doe",
        "celular": "9999-9999",
        "email": "john@doe.com",
        "categoria": "2",
        "saldo": 9000
    }

    controller = PessoaFisicaCreatorController(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(person_infor) 