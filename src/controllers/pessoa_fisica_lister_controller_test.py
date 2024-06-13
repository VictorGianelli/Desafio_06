from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from .pessoa_fisica_lister_controller import PessoaFisicaListerController

class MockPessoaFisicaRepository:
    def list_pessoas_fisicas(self):
        return [
            PessoaFisicaTable(id= 1,nome_completo = "João da Silva"),
            PessoaFisicaTable(id= 2,nome_completo = "Maria Oliveira"),
        ]

def test_list_pessoas_fisica():
    controller = PessoaFisicaListerController(MockPessoaFisicaRepository())
    response = controller.list_pessoas_fisicas()

    expected_response = {
        "data": {
            "type": "pessoa_fisica",
            "count": 2, 
            "attributes": [
                {"name": "João da Silva", "id": 1}, 
                {"name": "Maria Oliveira", "id": 2}
                ]
            }
        }
    

    assert response == expected_response
    