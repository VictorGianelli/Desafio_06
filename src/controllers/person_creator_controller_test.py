
import pytest
from .pessoa_fisica_creator_controller import PessoaFisicaCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

# @pytest.mark.skip(reason="Erro não concertado")
# def test_create():
#     person_infor = {
#         "first_name": "Fulano",
#         "last_name": "deTal",
#         "age": 30,
#         "pet_id": 123
#     }

#     controller = PessoaFisicaCreatorController(MockPeopleRepository())
#     response = controller.create(person_infor)

#     assert response["data"]["type"] == "Person"
#     assert response["data"]["count"] == 1
#     assert response["data"]["attributes"] == person_infor

# def test_create_error():
#     person_infor = {
#         "first_name": "Fulano123",
#         "last_name": "deTal",
#         "age": 30,
#         "pet_id": 123
#     }

#     controller = PessoaFisicaCreatorController(MockPeopleRepository())

#     with pytest.raises(Exception):
#         controller.create(person_infor)
