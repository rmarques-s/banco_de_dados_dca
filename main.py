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
        print(texto)
    except UnicodeEncodeError:
        print(texto.encode('utf-8', errors='ignore').decode())

def testar_aluno():
    safe_print("\n--- Testando Aluno ---")
    aluno = Aluno(matricula="2023001", nome="Maria Silva", email="maria@ufrn.br", curso="Engenharia da Computacao")
    AlunoService.criar_aluno(aluno)

    alunos = AlunoService.listar_alunos()
    for a in alunos:
        safe_print(f"Aluno: {a.matricula} - {a.nome}")

    AlunoService.atualizar_aluno("2023001", {"curso": "Sistemas de Informacao"})
    aluno_atualizado = AlunoService.buscar_por_id("2023001")
    safe_print(f"Atualizado: {aluno_atualizado.nome} - {aluno_atualizado.curso}")

    AlunoService.remover_aluno("2023001")
    safe_print("Aluno removido.")

def testar_livro():
    safe_print("\n--- Testando Livro ---")
    livro = Livro(codigo=1, titulo="Clean Code", autor="Robert C. Martin", editora="Alta Books", ano_publicacao=2008)
    LivroService.criar_livro(livro)

    livros = LivroService.listar_livros()
    for l in livros:
        safe_print(f"Livro: {l.codigo} - {l.titulo}")

    LivroService.atualizar_livro(1, {"ano_publicacao": 2010})
    livro_atualizado = LivroService.buscar_por_id(1)
    safe_print(f"Atualizado: {livro_atualizado.titulo} - {livro_atualizado.ano_publicacao}")

    LivroService.remover_livro(1)
    safe_print("Livro removido.")

def testar_exemplar():
    safe_print("\n--- Testando Exemplar ---")
    exemplar = Exemplar(tombo=101, codigo_livro=1)
    ExemplarService.criar_exemplar(exemplar)

    exemplares = ExemplarService.listar_exemplares()
    for e in exemplares:
        safe_print(f"Exemplar: {e.tombo} - Livro: {e.codigo_livro}")

    ExemplarService.atualizar_exemplar(101, {"codigo_livro": 1})
    ExemplarService.remover_exemplar(101)
    safe_print("Exemplar removido.")

def testar_emprestimo():
    safe_print("\n--- Testando Emprestimo ---")
    emprestimo = Emprestimo(
        id_emprestimo=1001,
        matricula_aluno="2023001",
        data_emprestimo=date.today(),
        data_prevista_devolucao=date(2025, 7, 10)
    )
    EmprestimoService.criar_emprestimo(emprestimo)

    emprestimos = EmprestimoService.listar_emprestimos()
    for e in emprestimos:
        safe_print(f"Emprestimo {e.id_emprestimo} para {e.matricula_aluno}")

    EmprestimoService.remover_emprestimo(1001)
    safe_print("Emprestimo removido.")

def testar_item_emprestimo():
    safe_print("\n--- Testando ItemEmprestimo ---")
    item = ItemEmprestimo(
        id_emprestimo=1001,
        tombo_exemplar=101,
        data_devolucao=None,
        dias_atraso=0
    )
    ItemEmprestimoService.criar_item(item)

    itens = ItemEmprestimoService.listar_itens()
    for i in itens:
        safe_print(f"Item: Emprestimo {i.id_emprestimo}, Tombo {i.tombo_exemplar}")

    ItemEmprestimoService.remover_item(1001, 101)
    safe_print("ItemEmprestimo removido.")

if __name__ == "__main__":
    try:
        testar_aluno()
        testar_livro()
        testar_exemplar()
        testar_emprestimo()
        testar_item_emprestimo()
    except Exception as e:
        print("❌ ERRO DURANTE A EXECUÇÃO:")
        print(e)