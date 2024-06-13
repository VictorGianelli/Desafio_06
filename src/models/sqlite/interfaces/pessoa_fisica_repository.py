from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, renda_mensal: int, idade:int, nome_completo: str, celular: str, email:str,categoria:str, saldo:int) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> PessoaFisicaTable:
        pass

    # @abstractmethod
    # def list_pessoas_fisicas(self) -> List[PessoaFisicaTable]:
    #     pass