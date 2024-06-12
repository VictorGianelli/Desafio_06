from typing import List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.cliente_repository import ClienteRepositoryInterface  


class ClientesRepository(ClienteRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def sacar_dinheiro(self, quantia:int,tipo_pessoa:str) -> None:
        pessoa_id = 1
        if tipo_pessoa == "fisica":
            tipo_pessoa = PessoaFisicaTable
        elif tipo_pessoa == "juridica":
            tipo_pessoa = PessoaJuridicaTable
        with self.__db_connection as database:
            try:
                pessoa = (database.session
                          .query(tipo_pessoa)
                          .filter(tipo_pessoa.id == pessoa_id)
                          .with_entities(tipo_pessoa.saldo)
                          .one()
                        )
                total = pessoa.saldo - quantia
                if total >= 0:
                    total = "O saldo restante após o saque é igual a", total
                else:
                    total = "Saldo insuficiente, valor superior a", pessoa.saldo
                
                return total
                
            except Exception as exception:
                database.session.rollback()
                raise exception  

    def realizar_extrato(self, nome_pessoa: int,tipo_nome:str) -> PessoaFisicaTable:
            try:
                with self.__db_connection as database:
                    if tipo_nome == "completo":
                        pessoa = (database.session
                                .query(PessoaFisicaTable)
                                .filter(PessoaFisicaTable.nome_completo == nome_pessoa)
                                .with_entities(PessoaFisicaTable.saldo)
                                .one()
                                )
                    elif tipo_nome == "fantasia":
                        pessoa = (database.session
                                .query(PessoaJuridicaTable)
                                .filter(PessoaJuridicaTable.nome_fantasia == nome_pessoa)
                                .with_entities(PessoaJuridicaTable.saldo)
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
