from typing import Dict
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: ClienteRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> PessoaFisicaTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Pessoa nao encontrada!")

        return person

    def __format_response(self, person: PessoaFisicaTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type
                }
            }
        }
    