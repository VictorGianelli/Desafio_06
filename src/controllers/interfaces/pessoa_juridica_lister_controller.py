from abc import ABC, abstractmethod
from typing import Dict
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaListerControllerInterface(ABC):

    @abstractmethod
    def list_pessoas_juridicas(self) -> Dict:
        pass