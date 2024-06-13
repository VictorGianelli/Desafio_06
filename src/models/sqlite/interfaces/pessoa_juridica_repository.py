from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, faturamento: int, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: int) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> PessoaJuridicaTable:
        pass
