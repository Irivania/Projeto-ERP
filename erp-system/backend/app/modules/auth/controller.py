from app.modules.auth.model import User
@router.delete("/usuario/anonimizar")
def anonimizar_usuario(username: str):
	db = SessionLocal()
	user = db.query(User).filter_by(username=username).first()
	if not user:
		raise HTTPException(status_code=404, detail="Usuário não encontrado")
	# Log de acesso a dado pessoal
	registrar_acao(username, "acesso_dado_pessoal", detalhes="anonimizacao")
	# Anonimização: remove dados pessoais, mantém registro para auditoria
	user.username = f"anon_{user.id}"
	user.senha_hash = ""
	user.consentimento = 0
	db.commit()
	registrar_acao(username, "anonimizacao_lgpd")
	return {"msg": "Usuário anonimizado conforme LGPD"}
# controller.py: Define as rotas e controladores da API do módulo de autenticação.

from fastapi import APIRouter, Depends, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.extension import Limiter as LimiterExtension
from app.modules.auth.schemas import LoginRequest, TokenResponse
from app.modules.auth.service import autenticar_usuario
from app.core.audit import registrar_acao
from app.database.connection import SessionLocal

from app.main import limiter

router = APIRouter()


@router.post("/consentimento")
def dar_consentimento(username: str):
	db = SessionLocal()
	user = db.query(User).filter_by(username=username).first()
	if not user:
		raise HTTPException(status_code=404, detail="Usuário não encontrado")
	# Log de acesso a dado pessoal
	registrar_acao(username, "acesso_dado_pessoal", detalhes="consentimento")
	user.consentimento = 1
	db.commit()
	registrar_acao(username, "consentimento_lgpd")
	return {"msg": "Consentimento registrado"}



@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
def login(request: LoginRequest, req: Request):
	db = SessionLocal()
	token = autenticar_usuario(db, request.username, request.password)
	if not token:
		registrar_acao(request.username, "login_falha")
		raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
	registrar_acao(request.username, "login_sucesso")
	return TokenResponse(access_token=token)
