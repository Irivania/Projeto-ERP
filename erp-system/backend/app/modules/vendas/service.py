# service.py: Implementa as regras de negócio do módulo de vendas.

from app.modules.estoque.service import baixar_estoque
from app.modules.financeiro.service import criar_transacao

def processar_venda(db, produto, quantidade, total):
	"""Processa uma venda: baixa estoque e registra transação financeira."""

	# estoque
	baixar_estoque(db, produto, quantidade)

	# financeiro
	criar_transacao(
		db,
		tipo="entrada",
		valor=total,
		descricao="Venda realizada"
	)
