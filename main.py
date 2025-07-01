from db import SessionLocal
from models.aluno import Aluno
from models.livro import Livro
from models.exemplar import Exemplar
from models.emprestimo import Emprestimo
from models.item_emprestimo import ItemEmprestimo

from services.aluno_service import AlunoService
from services.livro_service import LivroService
from services.exemplar_service import ExemplarService
from services.emprestimo_service import EmprestimoService
from services.item_emprestimo_service import ItemEmprestimoService

from datetime import date

def safe_print(texto):
    try:
        print(texto.encode('latin-1', errors='replace').decode('latin-1'))
    except Exception as e:
        print(f"[Erro ao imprimir]: {e}")

def criar_dados():
    safe_print("\n--- Criando Dados ---")

    aluno = Aluno(matricula="2023001", nome="Maria Silva", email="maria@ufrn.br", curso="Engenharia da Computacao")
    AlunoService.criar_aluno(aluno)

    livro = Livro(codigo=1, titulo="Clean Code", autor="Robert C. Martin", editora="Alta Books", ano_publicacao=2008)
    LivroService.criar_livro(livro)

    exemplar = Exemplar(tombo=101, codigo_livro=1)
    ExemplarService.criar_exemplar(exemplar)

    emprestimo = Emprestimo(
        id_emprestimo=1001,
        matricula_aluno="2023001",
        data_emprestimo=date.today(),
        data_prevista_devolucao=date(2025, 7, 10)
    )
    EmprestimoService.criar_emprestimo(emprestimo)

    item = ItemEmprestimo(
        id_emprestimo=1001,
        tombo_exemplar=101,
        data_devolucao=None,
        dias_atraso=0
    )
    ItemEmprestimoService.criar_item(item)

def testar_tudo():
    safe_print("\n--- Testando Aluno ---")
    aluno = AlunoService.buscar_por_id("2023001")
    safe_print(f"Aluno: {aluno.nome} - {aluno.curso}")
    AlunoService.atualizar_aluno("2023001", {"curso": "Sistemas de Informacao"})
    aluno_atualizado = AlunoService.buscar_por_id("2023001")
    safe_print(f"Atualizado: {aluno_atualizado.nome} - {aluno_atualizado.curso}")

    safe_print("\n--- Testando Livro ---")
    livro = LivroService.buscar_por_id(1)
    safe_print(f"Livro: {livro.codigo} - {livro.titulo}")
    LivroService.atualizar_livro(1, {"ano_publicacao": 2010})
    atualizado = LivroService.buscar_por_id(1)
    safe_print(f"Atualizado: {atualizado.titulo} - {atualizado.ano_publicacao}")

    safe_print("\n--- Testando Exemplar ---")
    exemplares = ExemplarService.listar_exemplares()
    for e in exemplares:
        safe_print(f"Exemplar: {e.tombo} - Livro: {e.codigo_livro}")
    ExemplarService.atualizar_exemplar(101, {"codigo_livro": 1})

    safe_print("\n--- Testando Emprestimo ---")
    emprestimos = EmprestimoService.listar_emprestimos()
    for e in emprestimos:
        safe_print(f"Emprestimo {e.id_emprestimo} para {e.matricula_aluno}")

    safe_print("\n--- Testando ItemEmprestimo ---")
    itens = ItemEmprestimoService.listar_itens()
    for i in itens:
        safe_print(f"Item: Emprestimo {i.id_emprestimo}, Tombo {i.tombo_exemplar}")

def deletar_tudo():
    safe_print("\n--- Removendo Dados ---")
    ItemEmprestimoService.remover_item(1001, 101)
    EmprestimoService.remover_emprestimo(1001)
    ExemplarService.remover_exemplar(101)
    LivroService.remover_livro(1)
    AlunoService.remover_aluno("2023001")
    safe_print("Todos os dados foram removidos com sucesso.")

if __name__ == "__main__":
    try:
        criar_dados()
        testar_tudo()
        deletar_tudo()
    except Exception as e:
        print("❌ ERRO DURANTE A EXECUÇÃO:")
        print(e)