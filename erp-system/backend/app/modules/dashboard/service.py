# service.py: Implementa as regras de negócio do módulo dashboard.

from app.modules.financeiro.model import Transacao
from app.modules.estoque.model import Produto
from app.modules.vendas.model import Venda
from sqlalchemy import func
from datetime import date

def gerar_dashboard(db):
	"""Gera dados consolidados para o dashboard do ERP."""

	hoje = date.today()

	# 💰 financeiro
	entradas = db.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "entrada").scalar() or 0
	saidas = db.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "saida").scalar() or 0

	saldo = entradas - saidas

	# 🛒 vendas do dia
	vendas_hoje = db.query(func.sum(Venda.total)).scalar() or 0

	# 📦 estoque baixo
	estoque_baixo = db.query(Produto).filter(Produto.quantidade < 5).all()

	return {
		"financeiro": {
			"entradas": entradas,
			"saidas": saidas,
			"saldo": saldo
		},
		"vendas_hoje": vendas_hoje,
		"estoque_baixo": [
			{"nome": p.nome, "quantidade": p.quantidade}
			for p in estoque_baixo
		]
	}


def gerar_alertas(dashboard):
    """Gera alertas automáticos com base nos dados do dashboard."""
    alertas = []

    # 💰 caixa negativo
    if dashboard["financeiro"]["saldo"] < 0:
        alertas.append("⚠️ Seu caixa está negativo!")

    # 📦 estoque baixo
    if len(dashboard["estoque_baixo"]) > 0:
        alertas.append("📦 Produtos com estoque baixo!")

    # 🛒 vendas baixas
    if dashboard["vendas_hoje"] < 100:
        alertas.append("📉 Vendas baixas hoje")

    return alertas


def gerar_sugestoes(dashboard):
	"""Gera sugestões automáticas com base nos dados do dashboard."""
	sugestoes = []

	if dashboard["vendas_hoje"] > 500:
		sugestoes.append("🔥 Alta venda hoje! Considere aumentar estoque.")

	if dashboard["financeiro"]["saldo"] > 1000:
		sugestoes.append("💰 Caixa positivo! Possível investimento.")

	return sugestoes
