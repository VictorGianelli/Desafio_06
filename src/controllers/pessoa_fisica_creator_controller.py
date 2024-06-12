import re
from typing import Dict
from src.models.sqlite.interfaces.cliente_repository import (
    ClienteRepositoryInterface
)
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.pessoa_fisica_creator_controller import PessoaFisicaCreatorControllerInterface


class PessoaFisicaCreatorController(PessoaFisicaCreatorControllerInterface):
    def __init__(self, cliente_repository: ClienteRepositoryInterface) -> None:
        self.__cliente_repository = cliente_repository

    def create(self, cliente_info: Dict) -> Dict:
        first_name = cliente_info["first_name"]
        last_name = cliente_info["last_name"]
        age = cliente_info["age"] 
        pet_id = cliente_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formated_response = self.__format_response
        return formated_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressão regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise HttpBadRequestError("Nome inválido")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__cliente_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, cliente_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": cliente_info
            }
        }
    