from db import SessionLocal
from models.item_emprestimo import ItemEmprestimo

class ItemEmprestimoService:

    @staticmethod
    def criar_item(item: ItemEmprestimo):
        session = SessionLocal()
        session.add(item)
        session.commit()
        session.close()

    @staticmethod
    def listar_itens():
        session = SessionLocal()
        itens = session.query(ItemEmprestimo).all()
        session.close()
        return itens

    @staticmethod
    def buscar_por_id(id_emprestimo, tombo_exemplar):
        session = SessionLocal()
        item = session.query(ItemEmprestimo).get((id_emprestimo, tombo_exemplar))
        session.close()
        return item

    @staticmethod
    def atualizar_item(id_emprestimo, tombo_exemplar, novos_dados: dict):
        session = SessionLocal()
        item = session.query(ItemEmprestimo).get((id_emprestimo, tombo_exemplar))
        if item:
            for chave, valor in novos_dados.items():
                setattr(item, chave, valor)
            session.commit()
        session.close()

    @staticmethod
    def remover_item(id_emprestimo, tombo_exemplar):
        session = SessionLocal()
        item = session.query(ItemEmprestimo).get((id_emprestimo, tombo_exemplar))
        if item:
            session.delete(item)
            session.commit()
        session.close()