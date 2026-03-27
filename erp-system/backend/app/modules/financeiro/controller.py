# controller.py: Define as rotas e controladores da API do módulo financeiro.

from fastapi import APIRouter, Depends, HTTPException
from app.modules.financeiro.schemas import TransacaoCreate, TransacaoResponse
from app.modules.financeiro.service import criar_transacao
from app.core.audit import registrar_acao
from app.database.connection import SessionLocal

router = APIRouter()

@router.post("/transacoes", response_model=TransacaoResponse)
def criar(transacao: TransacaoCreate):
	db = SessionLocal()
	nova = criar_transacao(db, **transacao.dict())
	db.commit()
	db.refresh(nova)
	registrar_acao("usuario", "acesso_dado_pessoal", detalhes="criar_transacao")
	return nova
