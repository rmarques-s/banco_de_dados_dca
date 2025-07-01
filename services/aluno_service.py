from db import SessionLocal
from models.aluno import Aluno

class AlunoService:

    @staticmethod
    def criar_aluno(aluno: Aluno):
        session = SessionLocal()
        session.add(aluno)
        session.commit()
        session.close()

    @staticmethod
    def listar_alunos():
        session = SessionLocal()
        alunos = session.query(Aluno).all()
        session.close()
        return alunos

    @staticmethod
    def buscar_por_id(matricula):
        session = SessionLocal()
        aluno = session.query(Aluno).get(matricula)
        session.close()
        return aluno

    @staticmethod
    def atualizar_aluno(matricula, novos_dados: dict):
        session = SessionLocal()
        aluno = session.query(Aluno).get(matricula)
        if aluno:
            for chave, valor in novos_dados.items():
                setattr(aluno, chave, valor)
            session.commit()
        session.close()

    @staticmethod
    def remover_aluno(matricula):
        session = SessionLocal()
        aluno = session.query(Aluno).get(matricula)
        if aluno:
            session.delete(aluno)
            session.commit()
        session.close()