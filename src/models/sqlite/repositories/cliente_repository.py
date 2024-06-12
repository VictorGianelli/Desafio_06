from typing import List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface  


class ClientesRepository(ClienteRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def sacar_dinheiro(self, quantia) -> None:
        pessoa_id = 1
        with self.__db_connection as database:
            try:
                pessoa = (database.session
                          .query(PessoaFisicaTable)
                          .filter(PessoaFisicaTable.id == pessoa_id)
                          .with_entities(PessoaFisicaTable.saldo)
                          .one()
                        )
                total = pessoa.saldo - quantia
                return total
            except Exception as exception:
                database.session.rollback()
                raise exception  

    def realizar_extrato(self, pessoa_id: int) -> PessoaFisicaTable:
        with self.__db_connection as database:
            try:
                pessoa = (database.session
                          .query(PessoaFisicaTable)
                          .filter(PessoaFisicaTable.id == pessoa_id)
                          .with_entities(PessoaFisicaTable.saldo)
                          .one()
                        )
                total = pessoa.saldo
                return total
            except NoResultFound:
                return []
        # with self.__db_connection as database:
        #     try:
        #         extrato=(database.session.
        #                  query(PessoaFisicaTable).
        #                  filter(PessoaFisicaTable.nome_completo == pessoa).
        #                  with_entities(PessoaFisicaTable.saldo).
        #                  one)

        #         return extrato
        #     except Exception as exception:
        #         database.session.rollback()
        #         raise exception
    # def insert_person(
    #     self,
    #     first_name: str,
    #     last_name: str,
    #     age: int,
    #     pet_id: int
    # ) -> None:
    #     with self.__db_connection as database:
    #         try:
    #             person_data = PeopleTable(
    #                 first_name=first_name,
    #                 last_name=last_name,
    #                 age=age,
    #                 pet_id=pet_id
    #             )
    #             database.session.add(person_data)
    #             database.session.commit()
    #         except Exception as exception:
    #             database.session.rollback()
    #             raise exception
