from typing import Dict, List
from src.controllers.interfaces.pessoa_fisica_lister_controller import PessoaFisicaListerControllerInterface
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaListerController(PessoaFisicaListerControllerInterface):
    def __init__(self, pessoa_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_repository = pessoa_repository

    def list_pessoas_fisicas(self) -> Dict:
        pessoas = self.__get_pessoas_in_db()
        response = self.__format_response(pessoas)
        return response

    def __get_pessoas_in_db(self) -> List[PessoaFisicaTable]:
        pessoas = self.__pessoa_repository.list_pessoas_fisicas()
        return pessoas

    def __format_response(self, pessoas: List[PessoaFisicaTable]) -> Dict:
        formatted_pessoas = []
        for pessoa in pessoas:
            formatted_pessoas.append({ "name": pessoa.nome_completo, "id": pessoa.id })

        return {
            "data": {
                "type": "pessoas",
                "count": len(formatted_pessoas),
                "attributes": formatted_pessoas
            }
        }
    