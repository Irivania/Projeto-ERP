# controller.py: Define as rotas e controladores da API do módulo dashboard.

from fastapi import APIRouter
from app.database.connection import SessionLocal
from .service import gerar_dashboard, gerar_alertas
from app.core.audit import registrar_acao

router = APIRouter()

@router.get("/")
def dashboard():
	db = SessionLocal()

	dados = gerar_dashboard(db)
	alertas = gerar_alertas(dados)
	registrar_acao("usuario", "acesso_dado_pessoal", detalhes="dashboard")
	return {
		"dados": dados,
		"alertas": alertas
	}
