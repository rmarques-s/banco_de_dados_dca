from db import SessionLocal
from models.livro import Livro

class LivroService:

    @staticmethod
    def criar_livro(livro: Livro):
        session = SessionLocal()
        session.add(livro)
        session.commit()
        session.close()

    @staticmethod
    def listar_livros():
        session = SessionLocal()
        livros = session.query(Livro).all()
        session.close()
        return livros

    @staticmethod
    def buscar_por_id(codigo):
        session = SessionLocal()
        livro = session.query(Livro).get(codigo)
        session.close()
        return livro

    @staticmethod
    def atualizar_livro(codigo, novos_dados: dict):
        session = SessionLocal()
        livro = session.query(Livro).get(codigo)
        if livro:
            for chave, valor in novos_dados.items():
                setattr(livro, chave, valor)
            session.commit()
        session.close()

    @staticmethod
    def remover_livro(codigo):
        session = SessionLocal()
        livro = session.query(Livro).get(codigo)
        if livro:
            session.delete(livro)
            session.commit()
        session.close()