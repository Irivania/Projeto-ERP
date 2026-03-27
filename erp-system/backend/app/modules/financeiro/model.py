# model.py: Define os modelos de dados (banco de dados) do módulo financeiro.

from sqlalchemy import Column, Integer, Float, String, Date
from app.database.base import Base

class Transacao(Base):
	__tablename__ = "transacoes"

	id = Column(Integer, primary_key=True)
	tipo = Column(String)  # entrada / saída
	valor = Column(Float)
	descricao = Column(String)
	data = Column(Date)
