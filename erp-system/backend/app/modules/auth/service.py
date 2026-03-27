# service.py: Implementa as regras de negócio do módulo de autenticação.

from app.core.security import gerar_hash_senha, verificar_senha, criar_token_acesso

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core.config import SECRET_KEY
from app.modules.auth.model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(db, token: str = Depends(oauth2_scheme)):
	from app.core.security import ALGORITHM
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Não autenticado",
		headers={"WWW-Authenticate": "Bearer"},
	)
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception
	except JWTError:
		raise credentials_exception
	user = db.query(User).filter(User.username == username).first()
	if user is None:
		raise credentials_exception
	return user

def require_role(role: str):
	def role_checker(user = Depends(get_current_user)):
		if user.role != role:
			raise HTTPException(status_code=403, detail="Acesso negado")
		return user
	return role_checker

def autenticar_usuario(db, username, senha):
	"""Autentica usuário e retorna token JWT se válido."""
	# Exemplo: buscar usuário no banco (ajuste conforme seu modelo)
	usuario = db.query(User).filter(User.username == username).first()
	if not usuario or not verificar_senha(senha, usuario.senha_hash):
		return None
	token = criar_token_acesso({"sub": usuario.username})
	return token
