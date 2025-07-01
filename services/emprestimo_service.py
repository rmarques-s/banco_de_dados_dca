from db import SessionLocal
from models.emprestimo import Emprestimo

class EmprestimoService:

    @staticmethod
    def criar_emprestimo(emprestimo: Emprestimo):
        session = SessionLocal()
        session.add(emprestimo)
        session.commit()
        session.close()

    @staticmethod
    def listar_emprestimos():
        session = SessionLocal()
        emprestimos = session.query(Emprestimo).all()
        session.close()
        return emprestimos

    @staticmethod
    def buscar_por_id(id_emprestimo):
        session = SessionLocal()
        emprestimo = session.query(Emprestimo).get(id_emprestimo)
        session.close()
        return emprestimo

    @staticmethod
    def atualizar_emprestimo(id_emprestimo, novos_dados: dict):
        session = SessionLocal()
        emprestimo = session.query(Emprestimo).get(id_emprestimo)
        if emprestimo:
            for chave, valor in novos_dados.items():
                setattr(emprestimo, chave, valor)
            session.commit()
        session.close()

    @staticmethod
    def remover_emprestimo(id_emprestimo):
        session = SessionLocal()
        emprestimo = session.query(Emprestimo).get(id_emprestimo)
        if emprestimo:
            session.delete(emprestimo)
            session.commit()
        session.close()