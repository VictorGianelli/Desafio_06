from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaRepository():
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(
        self, 
        faturamento: int, 
        idade:int, 
        nome_fantasia: str, 
        celular: str, 
        email_corporativo:str,
        categoria:str, 
        saldo:int
    ) -> None:
        with self.__db_connection as database:
            try:
                person_data = PessoaJuridicaTable(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_pessoas_juridicas(self) -> List:
        with self.__db_connection as database:
            try:
                pessoas = database.session.query(PessoaJuridicaTable).all()
                return pessoas
            except NoResultFound:
                return []