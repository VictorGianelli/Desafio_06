import re
from typing import Dict
from src.models.sqlite.interfaces.pessoa_juridica_repository import (
    PessoaJuridicaRepositoryInterface
)
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.pessoa_juridica_creator_controller import PessoaJuridicaCreatorControllerInterface


class PessoaJuridicaCreatorController(PessoaJuridicaCreatorControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def create(self, pessoa_juridica_info: Dict) -> Dict:
        faturamento = pessoa_juridica_info["faturamento"] 
        idade = pessoa_juridica_info["idade"] 
        nome_fantasia = pessoa_juridica_info["nome_fantasia"] 
        celular = pessoa_juridica_info["celular"] 
        email_corporativo = pessoa_juridica_info["email_corporativo"]
        categoria = pessoa_juridica_info["categoria"] 
        saldo = pessoa_juridica_info["saldo"]

        # print(pessoa_juridica_info.__dict__)
        # self.__validate_first_and_last_name(nome_fantasia)
        self.__insert_person_in_db(faturamento,idade,nome_fantasia,celular,email_corporativo,categoria,saldo)
        formated_response = self.__format_response(pessoa_juridica_info)
        return formated_response

    # def __validate_first_and_last_name(self, nome_completo: str) -> None:
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

    def __insert_person_in_db(self, faturamento: int,idade:int, nome_fantasia: str, celular: str, email_corporativo:str, categoria:str, saldo:int) -> None:
        self.__pessoa_juridica_repository.insert_person(faturamento,idade, nome_fantasia, celular, email_corporativo, categoria, saldo)

    def __format_response(self, pessoa_juridica_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Perssoa Juridica",
                "count": 1,
                "attributes": pessoa_juridica_info
            }
        }
    