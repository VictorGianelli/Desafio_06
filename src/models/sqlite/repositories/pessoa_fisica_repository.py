from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepository():
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(
        self, 
        renda_mensal: int, 
        idade:int, 
        nome_completo: str, 
        celular: str, 
        email:str,
        categoria:str, 
        saldo:int
    ) -> None:
        with self.__db_connection as database:
            try:
                person_data = PessoaFisicaTable(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
