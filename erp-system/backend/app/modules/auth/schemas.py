# schemas.py: Define os modelos Pydantic para o módulo de autenticação.

from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
