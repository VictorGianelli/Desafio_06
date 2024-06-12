from sqlalchemy import BIGINT, INTEGER, REAL, Column, String
from  ..settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"
    id = Column(BIGINT, primary_key=True) 
    faturamento = Column(REAL, nullable=False)
    idade = Column(INTEGER, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"PessoaJuridicaTable(id={self.id}, faturamento={self.faturamento}, idade={self.idade}, nome_fantasia={self.nome_fantasia}, celular={self.celular}, email_corporativo={self.email_corporativo}, categoria={self.categoria}, saldo={self.saldo})"