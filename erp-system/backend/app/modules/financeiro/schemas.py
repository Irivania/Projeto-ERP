# schemas.py: Define os modelos Pydantic para o módulo financeiro.

from pydantic import BaseModel
from datetime import date

class TransacaoCreate(BaseModel):
    tipo: str
    valor: float
    descricao: str
    data: date

class TransacaoResponse(BaseModel):
    id: int
    tipo: str
    valor: float
    descricao: str
    data: date

    class Config:
        from_attributes = True  # Pydantic v2 para integração com ORM
