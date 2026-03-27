# service.py: Implementa as regras de negócio do módulo financeiro.

def criar_transacao(db, tipo, valor, descricao):
	"""Cria uma nova transação financeira e adiciona ao banco de dados."""
	from .model import Transacao

	transacao = Transacao(
		tipo=tipo,
		valor=valor,
		descricao=descricao
	)

	db.add(transacao)
	return transacao
