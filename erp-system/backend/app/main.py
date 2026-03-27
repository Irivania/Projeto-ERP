# Ponto de entrada da aplicação FastAPI


from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.modules.dashboard.controller import router as dashboard_router

app = FastAPI(title="ERP Inteligente")

# Configuração do rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(dashboard_router, prefix="/dashboard")

@app.get("/")
def home():
	return {"msg": "ERP rodando"}


# Endpoint público para política de privacidade
@app.get("/privacidade")
def politica_privacidade():
	return {
		"titulo": "Política de Privacidade",
		"descricao": "Seus dados são tratados conforme a LGPD. Você pode solicitar anonimização, exclusão ou obter informações sobre seus dados a qualquer momento. Para mais detalhes, consulte o DPO da empresa."
	}
