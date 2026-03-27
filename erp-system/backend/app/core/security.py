# Configurações de segurança do sistema ERP


from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import SECRET_KEY

# Configurações do JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para hash de senha
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def verificar_senha(senha_plana, senha_hash):
	return pwd_context.verify(senha_plana, senha_hash)

def gerar_hash_senha(senha):
	return pwd_context.hash(senha)

def criar_token_acesso(data: dict, expires_delta: timedelta = None):
	to_encode = data.copy()
	expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
	to_encode.update({"exp": expire})
	return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		return payload
	except JWTError:
		return None
