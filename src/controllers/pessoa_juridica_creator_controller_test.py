import pytest
from .pessoa_juridica_creator_controller import PessoaJuridicaCreatorController 

class MockPeopleRepository:
    def insert_person(self, faturamento: str, idade: str, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: str, ):
        pass


# @pytest.mark.skip(reason="Erro não concertado")
def test_create():
    person_infor = {
        "faturamento": 100000,
        "idade": 28,
        "nome_fantasia": "Empresa XYZ",
        "celular": "9999-9999",
        "email_corporativo": "contato@empresa.com",
        "categoria": "2",
        "saldo": 9000
    }

    controller = PessoaJuridicaCreatorController(MockPeopleRepository())
    response = controller.create(person_infor)

    # print(response)
    assert response["data"]["type"] == "Perssoa Juridica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infor

def test_create_error():
    person_infor = {
        "faturamento": 2000,
        "idade": 28,
        "nome_fantasia": "Empresa XYZ",
        "celular": "9999-9999",
        "email_corporativo": "johndoe",
        "categoria": "2",
        "saldo": 9000
    }

    controller = PessoaJuridicaCreatorController(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(person_infor) 