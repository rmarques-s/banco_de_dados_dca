from sqlalchemy import Column, Integer, Date, ForeignKey
from models import Base

class ItemEmprestimo(Base):
    __tablename__ = "ItemEmprestimo"

    id_emprestimo = Column(Integer, ForeignKey("emprestimo.id_emprestimo"), primary_key=True)
    tombo_exemplar = Column(Integer, ForeignKey("exemplar.tombo"), primary_key=True)
    data_devolucao = Column(Date)
    dias_atraso = Column(Integer)