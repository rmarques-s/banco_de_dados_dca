from db import SessionLocal
from models.exemplar import Exemplar

class ExemplarService:

    @staticmethod
    def criar_exemplar(exemplar: Exemplar):
        session = SessionLocal()
        session.add(exemplar)
        session.commit()
        session.close()

    @staticmethod
    def listar_exemplares():
        session = SessionLocal()
        exemplares = session.query(Exemplar).all()
        session.close()
        return exemplares

    @staticmethod
    def buscar_por_id(tombo):
        session = SessionLocal()
        exemplar = session.query(Exemplar).get(tombo)
        session.close()
        return exemplar

    @staticmethod
    def atualizar_exemplar(tombo, novos_dados: dict):
        session = SessionLocal()
        exemplar = session.query(Exemplar).get(tombo)
        if exemplar:
            for chave, valor in novos_dados.items():
                setattr(exemplar, chave, valor)
            session.commit()
        session.close()

    @staticmethod
    def remover_exemplar(tombo):
        session = SessionLocal()
        exemplar = session.query(Exemplar).get(tombo)
        if exemplar:
            session.delete(exemplar)
            session.commit()
        session.close()