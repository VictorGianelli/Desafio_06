import re
from typing import Dict
from src.models.sqlite.interfaces.pessoa_fisica_repository import (
    PessoaFisicaRepositoryInterface
)
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.pessoa_fisica_creator_controller import PessoaFisicaCreatorControllerInterface


class PessoaFisicaCreatorController(PessoaFisicaCreatorControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def create(self, pessoa_fisica_info: Dict) -> Dict:
        renda_mensal = pessoa_fisica_info["renda_mensal"] 
        idade = pessoa_fisica_info["idade"] 
        nome_completo = pessoa_fisica_info["nome_completo"] 
        celular = pessoa_fisica_info["celular"] 
        email = pessoa_fisica_info["email"]
        categoria = pessoa_fisica_info["categoria"] 
        saldo = pessoa_fisica_info["saldo"]

        # print(pessoa_fisica_info.__dict__)
        self.__validate_first_and_last_name(nome_completo)
        self.__insert_person_in_db(renda_mensal,idade,nome_completo,celular,email,categoria,saldo)
        formated_response = self.__format_response(pessoa_fisica_info)
        return formated_response

    def __validate_first_and_last_name(self, nome_completo: str) -> None:
        # Expressão regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')
        try:
            nome_completo = nome_completo.split(" ")

            first_name = nome_completo[0]
            last_name = nome_completo[1]
            if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
                raise HttpBadRequestError("Nome inválido")
        except Exception:
            raise HttpBadRequestError("Nome inválido")

    def __insert_person_in_db(self, renda_mensal: int,idade:int, nome_completo: str, celular: str, email:str, categoria:str, saldo:int) -> None:
        self.__pessoa_fisica_repository.insert_person(renda_mensal,idade, nome_completo, celular, email, categoria, saldo)

    def __format_response(self, pessoa_fisica_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Perssoa Fisica",
                "count": 1,
                "attributes": pessoa_fisica_info
            }
        }
    