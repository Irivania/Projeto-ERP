# service.py: Implementa as regras de negócio do módulo de estoque.

def baixar_estoque(db, produto, quantidade):
	"""Baixa a quantidade de um produto no estoque."""
	if produto.quantidade < quantidade:
		raise Exception("Estoque insuficiente")

	produto.quantidade -= quantidade
