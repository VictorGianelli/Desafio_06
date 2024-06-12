from abc import ABC, abstractmethod


class ClienteRepositoryInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, quantia) -> None:
        pass

    @abstractmethod
    def realizar_extrato(self, pessoa)-> None:
        pass