from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_lister_controller import PessoaJuridicaListerController

class MockPessoaJuridicaRepository:
    def list_pessoas_juridicas(self):
        return [
            PessoaJuridicaTable(id= 1,nome_fantasia = "Empresa ABC"),
            PessoaJuridicaTable(id= 2,nome_fantasia = "Empresa XYZ"),
        ]

def test_list_pessoas_juridica():
    controller = PessoaJuridicaListerController(MockPessoaJuridicaRepository())
    response = controller.list_pessoas_juridicas()

    expected_response = {
        'data': {
            'type': 'pessoa_juridica', 
            'count': 2, 
            'attributes': [
                {'name': 'Empresa ABC', 'id': 1}, 
                {'name': 'Empresa XYZ', 'id': 2}
                ]
            }
        }
    

    assert response == expected_response
    