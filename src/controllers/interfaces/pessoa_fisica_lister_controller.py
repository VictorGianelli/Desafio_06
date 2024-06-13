from abc import ABC, abstractmethod
from typing import Dict
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaListerControllerInterface(ABC):

    @abstractmethod
    def list_pessoas_fisicas(self) -> Dict:
        pass