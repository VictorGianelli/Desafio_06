from typing import Dict, List
from src.controllers.interfaces.pessoa_juridica_lister_controller import PessoaJuridicaListerControllerInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaListerController(PessoaJuridicaListerControllerInterface):
    def __init__(self, pessoa_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_repository = pessoa_repository

    def list_pessoas_juridicas(self) -> Dict:
        pessoas = self.__get_pessoas_in_db()
        response = self.__format_response(pessoas)
        return response

    def __get_pessoas_in_db(self) -> List[PessoaJuridicaTable]:
        pessoas = self.__pessoa_repository.list_pessoas_juridicas()
        return pessoas

    def __format_response(self, pessoas: List[PessoaJuridicaTable]) -> Dict:
        formatted_pessoas = []
        for pessoa in pessoas:
            formatted_pessoas.append({ "name": pessoa.nome_fantasia, "id": pessoa.id })

        return {
            "data": {
                "type": "pessoa_juridica",
                "count": len(formatted_pessoas),
                "attributes": formatted_pessoas
            }
        }
    